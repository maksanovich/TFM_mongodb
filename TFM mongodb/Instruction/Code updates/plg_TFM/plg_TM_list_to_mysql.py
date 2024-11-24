

from a0_items import * 
from plg_Files import * 
from plg_Folders import * 
from plg_DB_Mysql import *




##### Txt to Mysql #########################################

### The following code is to be executed on the TFM server side, not from TFM master #######
############################################################################################
##### RAW, COOKED data files #######


# get a list of raw files from a folder 
def get_LIST_raw_ALL (raw_folder_path):

   LIST_raw_ALL = get_ALL_in_folder (folder_path=raw_folder_path)
   
   return LIST_raw_ALL 
   
 
#get_LIST_raw_ALL (folder_path)
 
  
# a a list of databases from mysql server   
def get_LIST_cooked_ALL (cooked_My_host, cooked_My_user, cooked_My_pass):

   LIST_cooked_ALL = Mysql_get_ALL_DB (My_host=cooked_My_host, My_user=cooked_My_user, My_pass=cooked_My_pass)
   
   return LIST_cooked_ALL 
   


# get selected files by index
def get_LIST_raw_SELECTED (raw_folder_path, raw_start_file_index, raw_end_file_index):

   LIST_raw_ALL = get_LIST_raw_ALL (folder_path=raw_folder_path)

   LIST_raw_selected = []
   
   for raw_file in LIST_raw_ALL(raw_start_file_index=raw_start_file_index, raw_end_file_index=raw_end_file_index):
   
      LIST_raw_selected.append(raw_file)
           
   return LIST_raw_selected
   
   
# get selected database by index
def get_LIST_cooked_SELECTED (cooked_My_host, cooked_My_user, cooked_My_pass, cooked_start_db_index, cooked_end_db_index ):

   LIST_cooked_ALL = get_LIST_cooked_ALL (cooked_My_host=cooked_My_host, cooked_My_user=cooked_My_user, cooked_My_pass=cooked_My_pass)

   LIST_cooked_selected = []
   
   for cooked_db in LIST_cooked_ALL(cooked_start_db_index=cooked_start_db_index, cooked_end_db_index=cooked_end_db_index):
   
      LIST_cooked_selected.append(cooked_db)
           
   return LIST_cooked_selected



############################################################
##### RAW, COOKED, TO_BE Data items #######

def get_raw_DATA_ITEMS (raw_file_path):
  
   LIST_raw_data_item = File_read_lines (file_path = raw_file_path)
   
   print (LIST_raw_data_item)
   return LIST_raw_data_item
   
 
 
#### Select data with log status = Completed, In progress, Not completed within allowed task duration
def get_cooked_DATA_ITEMS (cooked_My_host, cooked_My_user, cooked_My_pass , cooked_My_db_name, cooked_My_select_query):

   LIST_cooked_data_item = Mysql_select_tb_data (cooked_My_host=cooked_My_host, cooked_My_user=cooked_My_user, cooked_My_pass=cooked_My_pass , cooked_My_db_name=cooked_My_db_name, cooked_My_select_query=cooked_My_select_query)
   
   return LIST_cooked_data_item


#get_cooked_DATA_ITEMS (cooked_My_host, cooked_My_user, cooked_My_pass , cooked_My_db_name, cooked_My_select_query)



def get_TO_BE_DATA_ITEMS (raw_file_path, cooked_My_host, cooked_My_user, cooked_My_pass , cooked_My_db_name, cooked_My_select_query):

   LIST_raw = get_raw_DATA_ITEMS (raw_file_path = raw_file_path)
   LIST_cooked = get_cooked_DATA_ITEMS (cooked_My_host=cooked_My_host, cooked_My_user=cooked_My_user, cooked_My_pass=cooked_My_pass , cooked_My_db_name=cooked_My_db_name, cooked_My_select_query=cooked_My_select_query)
   
   LIST_to_be = []
       
   for raw in LIST_raw:
    
      if raw in LIST_cooked:
       
         #print (raw + ' in cooked')
         pass
          
      else:
          
         #print (raw + ' NOT in cooked')
         LIST_to_be.append(raw)
   
   #print ('LIST to be => ' + str(LIST_test_to_be))   
   return LIST_to_be 
   
   
   
# split data item to get data chunk   
def split_to_be_DATA_ITEMS (raw_file_path, cooked_My_host, cooked_My_user, cooked_My_pass , cooked_My_db_name, cooked_My_select_query, start_index, items_per_list):
 
   LIST_to_be_DATA_ITEM = get_TO_BE_DATA_ITEMS (raw_file_path=raw_file_path, cooked_My_host=cooked_My_host, cooked_My_user=cooked_My_user, cooked_My_pass=cooked_My_pass , cooked_My_db_name=cooked_My_db_name, cooked_My_select_query=cooked_My_select_query)
   
   return list_SPLIT_1 (LIST_to_split = LIST_to_be_DATA_ITEM, start_index = start_index, items_per_list = items_per_list)


'''
# do the task on 1 data item, eg send email, post comment   
## this method needs to be created from scratch to be used by CF_data_chunk (LIST_item)
def do_task_DATA_ITEM (data_item):

   print (data_item)   
'''   
  
#####################################################################
##### Selected TO_BE data files with TO_BE data items 

def get_LIST_to_be_SELECTED_with_data_items (raw_folder_path, raw_start_file_index, raw_end_file_index,cooked_My_host, cooked_My_user, cooked_My_pass,  cooked_start_db_index, cooked_end_db_index ):

   LIST_raw_file_SELECTED =  get_LIST_raw_SELECTED (raw_folder_path = raw_folder_path, raw_start_file_index = raw_start_file_index, raw_end_file_index = raw_end_file_index)
   LIST_cooked_file_SELECTED = get_LIST_cooked_SELECTED (cooked_My_host=cooked_My_host, cooked_My_user=cooked_My_user, cooked_My_pass=cooked_My_pass,cooked_start_db_index=cooked_start_db_index, cooked_end_db_index=cooked_end_db_index )
   
   #TO_BE files & data 
   LIST_to_be_file_data_SELECTED = []
   
   # get_TO_BE_DATA_ITEMS returns a list of TO_BE data 
   for raw_file, cooked_file zip(LIST_raw_file_SELECTED, LIST_cooked_file_SELECTED):

      LIST_to_be_file_data_SELECTED.append( raw_file + ' #_0 ' + get_TO_BE_DATA_ITEMS (raw_file_path = raw_folder_path + raw_file, cooked_file_path = cooked_folder_path + cooked_file) )

   return LIST_to_be_file_data_SELECTED


#get_LIST_to_be_SELECTED_with_data_items (raw_folder_path, raw_start_file_index, raw_end_file_index,  cooked_start_db_index, cooked_end_db_index,cooked_My_host, cooked_My_user, cooked_My_pass )



#################################################################
###### Concurrent futures on data chunks ########################


# data file --> data items --> data chunks (or data item chunks) 

## do_task_DATA_ITEM --> CF_data_chunk (LIST_item) --> CF_all_data_chunk (start_file, end_file, raw_folder_path, cooked_folder_path, start_index, items_per_list)

def CF_data_chunk (LIST_item):

   with concurrent.futures.ProcessPoolExecutor() as executor:
        
      executor.map(do_one_DATA_ITEM, LIST_item=LIST_item)
        
      t2 = time.perf_counter()
      print (f' finished in {t2} seconds')      



# Concurrent futures on TO_BE data chunks only
def CF_all_data_chunk (raw_folder_path, raw_file_path, raw_start_file_index, rarw_end_file_index, cooked_My_host, cooked_My_user, cooked_My_pass,  cooked_start_db_index, cooked_end_db_index, do_one_DATA_ITEM):
  
   # LIST TO_BE file & data
   LIST_to_be_file_data = get_LIST_to_be_SELECTED_with_data_items (raw_folder_path, raw_start_file_index, raw_end_file_index,  cooked_start_db_index, cooked_end_db_index,cooked_My_host, cooked_My_user, cooked_My_pass )
   
   start_file_index = raw_start_file_index
   end_file_index = raw_end_file_index
     
   # Loop through EACH selected to_be data file 
   for data_file in LIST_to_be_file_data[start_file_index:end_file_index]:

      LIST_to_be_file_only = remove_all_after_text (after_text= ' #_0 ' , text_main = data_file)
      LIST_data_item_only = remove_all_before_text (before_text= ' #_0 ', text_main = data_file)
              
      for data_items in LIST_data_item_only:
      
         #LIST_data_item_chunk = split_LIST_data_item  (LIST_to_split=LIST_data_item_only, start_index=start_index, items_per_list=items_per_list)         
         LIST_data_itek_chunk = split_to_be_DATA_ITEMS (raw_file_path=raw_folder_path + raw_file_path, cooked_My_host=cooked_My_host, cooked_My_user=cooked_My_user, cooked_My_pass=cooked_My_pass , cooked_My_db_name=cooked_My_db_name, cooked_My_select_query=cooked_My_select_query, start_index=start_index, items_per_list=items_per_list)
      
         for data_item_chunk in LIST_data_item_chunk    
                  
            CF_data_chunk (LIST_item=data_item_chunk)   



#do_task_DATA_ITEM --> need write this function to be used by CF_data_chunk (LIST_item)

raw_folder_path = ''
raw_file_path = ''
raw_start_file_index = ''
raw_end_file_index = ''

cooked_My_host = ''
cooked_My_user = ''
cooked_My_pass = ''
cooked_My_db_name = ''
cooked_My_select_query = ''
cooked_My_start_db_index = ''
cooked_My_end_db_index = ''

start_index = ''
items_per_list = ''

do_one_DATA_ITEM = ''# this is a function to complete 1 data item 
LIST_item = ''



#CF_all_data_chunk (raw_folder_path, raw_file_path, raw_start_file_index, rarw_end_file_index, cooked_My_host, cooked_My_user, cooked_My_pass,  cooked_start_db_index, cooked_end_db_index)