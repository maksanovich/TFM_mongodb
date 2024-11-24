

from a0_items import * 
from plg_DB_Mysql import * 

from concurrent.futures import ThreadPoolExecutor, wait
import concurrent.futures
import time 
import datetime



def get_LIST_raw_ALL (raw_My_host, raw_My_user, raw_My_pass):

   LIST_raw_ALL = Mysql_get_ALL_DB (My_host=raw_My_host, My_user=raw_My_user, My_pass=raw_My_pass)
   
   return LIST_raw_ALL 
   
   
   
def get_LIST_cooked_ALL (cooked_My_host, cooked_My_user, cooked_My_pass):

   LIST_cooked_ALL = Mysql_get_ALL_DB (My_host=cooked_My_host, My_user=cooked_My_user, My_pass=cooked_My_pass)
   
   return LIST_cooked_ALL 
   



def get_LIST_raw_SELECTED (raw_start_db_index, raw_end_db_index, raw_My_host, raw_My_user, raw_My_pass):

   LIST_raw_ALL = get_LIST_raw_ALL (raw_My_host=raw_My_host, raw_My_user=raw_My_user, raw_My_pass=raw_My_pass)

   LIST_raw_selected = []
   
   for raw_db in LIST_raw_ALL(raw_start_db_index=raw_start_db_index, raw_end_db_index=raw_end_db_index):
   
      LIST_raw_selected.append(raw_db)
           
   return LIST_raw_selected
   
   

def get_LIST_cooked_SELECTED (cooked_start_db_index, cooked_end_db_index, cooked_My_host, cooked_My_user, cooked_My_pass):

   LIST_cooked_ALL = get_LIST_cooked_ALL (cooked_My_host=cooked_My_host, cooked_My_user=cooked_My_user, cooked_My_pass=cooked_My_pass)

   LIST_cooked_selected = []
   
   #must use index to select database
   for cooked_db in LIST_cooked_ALL(cooked_start_db_index=cooked_start_db_index, cooked_end_db_index=cooked_end_db_index):
   
      LIST_cooked_selected.append(cooked_db)
           
   return LIST_cooked_selected



############################################################
##### RAW, COOKED, TO_BE Data items #######

def get_raw_DATA_ITEMS (raw_My_host, raw_My_user, raw_My_pass , raw_My_db_name, raw_My_select_query):
  
   LIST_raw_data_item = Mysql_select_tb_data (My_host=raw_My_host, My_user=raw_My_user, My_pass=raw_My_pass , My_db_name=raw_My_db_name, My_select_query=raw_My_select_query)
   
   return LIST_raw_data_item
   
  
#### Select data with log status = Completed, In progress, Not completed within allowed task duration
def get_cooked_DATA_ITEMS (cooked_My_host, cooked_My_user, cooked_My_pass , cooked_My_db_name, cooked_My_select_query):

   LIST_cooked_data_item = Mysql_select_tb_data (My_host=cooked_My_host, My_user=cooked_My_user, My_pass=cooked_My_pass , My_db_name=cooked_My_db_name, My_select_query=cooked_My_select_query)
      
   return LIST_cooked_data_item 



#get_cooked_DATA_ITEMS (cooked_My_host, cooked_My_user, cooked_My_pass , cooked_My_db_name, cooked_My_select_query)



def get_TO_BE_DATA_ITEMS (raw_My_host, raw_My_user, raw_My_pass , raw_My_db_name, raw_My_select_query, cooked_My_host, cooked_My_user, cooked_My_pass , cooked_My_db_name, cooked_My_select_query):

   LIST_raw =  get_raw_DATA_ITEMS (raw_My_host=raw_My_host, raw_My_user=raw_My_user, raw_My_pass = raw_My_pass , raw_My_db_name=raw_My_db_name, raw_My_select_query=raw_My_select_query)
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
def split_to_be_DATA_ITEMS (raw_My_host, raw_My_user, raw_My_pass , raw_My_db_name, raw_My_select_query, cooked_My_host, cooked_My_user, cooked_My_pass , cooked_My_db_name, cooked_My_select_query, start_index, items_per_list):
 
   LIST_to_be_DATA_ITEM = get_TO_BE_DATA_ITEMS (raw_My_host=raw_My_host, raw_My_user=raw_My_user, raw_My_pass=raw_My_pass , raw_My_db_name=raw_My_db_name, raw_My_select_query=raw_My_select_query, cooked_My_host=cooked_My_host, cooked_My_user=cooked_My_user, cooked_My_pass=cooked_My_pass , cooked_My_db_name=cooked_My_db_name, cooked_My_select_query=cooked_My_select_query)
   
   return list_SPLIT_1 (LIST_to_split = LIST_to_be_DATA_ITEM, start_index = start_index, items_per_list = items_per_list)




# do the task on 1 data item, eg send email, post comment   
## this method needs to be created from scratch to be used by CF_data_chunk (LIST_item)
def do_task_DATA_ITEM (data_item):

   print (data_item)   
   
   

#####################################################################
##### Selected TO_BE data dbs with TO_BE data items 

def get_LIST_to_be_SELECTED_with_data_items ( raw_My_user, raw_My_pass , raw_My_db_name, raw_start_db_index, raw_end_db_index, raw_My_host, raw_My_select_query, cooked_start_db_index, cooked_end_db_index, cooked_My_host, cooked_My_user, cooked_My_pass , cooked_My_db_name, cooked_My_select_query ):

   LIST_raw_db_SELECTED =  get_LIST_raw_SELECTED (raw_start_db_index=raw_start_db_index, raw_end_db_index=raw_end_db_index, raw_My_host=raw_My_host, raw_My_user=raw_My_user, raw_My_pass=raw_My_pass)
   LIST_cooked_db_SELECTED = get_LIST_cooked_SELECTED (cooked_start_db_index=cooked_start_db_index, cooked_end_db_index=cooked_end_db_index, cooked_My_host=cooked_My_host, cooked_My_user=cooked_My_user, cooked_My_pass=cooked_My_pass)
   
   #TO_BE dbs & data 
   LIST_to_be_db_data_SELECTED = []
   
   # get_TO_BE_DATA_ITEMS returns a list of TO_BE data 
   for raw_db, cooked_db zip(LIST_raw_db_SELECTED, LIST_cooked_db_SELECTED):

      LIST_to_be_db_data_SELECTED.append( raw_db + ' #_0 ' + get_TO_BE_DATA_ITEMS (raw_My_host=raw_My_host, raw_My_user=raw_My_user, raw_My_pass=raw_My_pass , raw_My_db_name=raw_My_db_name, raw_My_select_query=raw_My_select, cooked_My_host=cooked_My_host, cooked_My_user=cooked_My_user, cooked_My_pass=cooked_My_pass , cooked_My_db_name=cooked_My_db_name, cooked_My_select_query=cooked_My_select_query) )

   return LIST_to_be_db_data_SELECTED


#get_LIST_to_be_SELECTED_with_data_items (start_db, end_db, raw_folder_path, cooked_folder_path, DB_db_name )



#################################################################
###### Concurrent futures on data chunks ########################


# data db --> data items --> data chunks (or data item chunks) 

## do_task_DATA_ITEM --> CF_data_chunk (LIST_item) --> CF_all_data_chunk (start_db, end_db, raw_folder_path, cooked_folder_path, DB_db_name, start_index, items_per_list)

def CF_data_chunk (LIST_item):

   with concurrent.futures.ProcessPoolExecutor() as executor:
        
      executor.map(do_task_DATA_ITEM, LIST_item)
        
      t2 = time.perf_counter()
      print (f' finished in {t2} seconds')      



# Concurrent futures on TO_BE data chunks only
def CF_all_data_chunk (raw_start_db_index, raw_end_db_index, raw_My_host, raw_My_user, raw_My_pass , raw_My_db_name, raw_My_select_query, cooked_start_db_index, cooked_end_db_index, cooked_My_host, cooked_My_user, cooked_My_pass , cooked_My_db_name, cooked_My_select_query, start_index, items_per_list, do_one_DATA_ITEM):
  
   # LIST TO_BE db & data
   LIST_to_be_db_data = get_LIST_to_be_SELECTED_with_data_items (raw_start_db_index=raw_start_db_index, raw_end_db_index=raw_end_db_index, raw_My_host=raw_My_host, raw_My_user=raw_My_user, raw_My_pass=raw_My_pass, raw_My_db_name=raw_My_db_name, raw_My_select_query=raw_My_select_query, cooked_start_db_index=cooked_start_db_index, cooked_end_db_index=cooked_end_db_index, cooked_My_host=cooked_My_host, cooked_My_user=cooked_My_user, cooked_My_pass=cooked_My_pass , cooked_My_db_name=cooked_My_db_name, cooked_My_select_query=cooked_My_select_query, start_index, items_per_list )
   
   start_db_index = raw_start_db_index
   end_db_index = raw_end_db_index
   
   
   # Loop through EACH selected to_be data db 
   for data_db in LIST_to_be_db_data[start_db_index:end_db_index]:

      LIST_to_be_db_only = remove_all_after_text (after_text= ' #_0 ' , text_main = data_db)
      LIST_data_item_only = remove_all_before_text (before_text= ' #_0 ', text_main = data_db)
              
      for data_items in LIST_data_item_only:
      
         #LIST_data_item_chunk = split_LIST_data_item  (LIST_to_split=LIST_data_item_only, start_index=start_index, items_per_list=items_per_list)         
         LIST_data_itek_chunk = split_to_be_DATA_ITEMS (raw_My_host=raw_My_host, raw_My_user=raw_My_user, raw_My_pass=raw_My_pass , raw_My_db_name=raw_My_db_name, raw_My_select_query=raw_My_select_query, cooked_My_host=cooked_My_host, cooked_My_user=cooked_My_user, cooked_My_pass=cooked_My_pass , cooked_My_db_name=cooked_My_db_name, cooked_My_select_query=cooked_My_selected_query, start_index=start_index, items_per_list=items_per_list)
      
         for data_item_chunk in LIST_data_item_chunk    
                  
            CF_data_chunk (LIST_item=data_item_chunk)   



#do_task_DATA_ITEM --> need write this function to be used by CF_data_chunk (LIST_item)


raw_My_host = ''
raw_My_user = ''
raw_My_pass = ''
raw_My_db_name = ''
raw_My_select_query = ''
raw_My_start_db_index = ''
raw_My_end_db_index = ''


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



#CF_all_data_chunk (raw_My_host, raw_My_user, raw_My_pass , raw_My_db_name, raw_My_select_query, cooked_My_host, cooked_My_user, cooked_My_pass , cooked_My_db_name, cooked_My_select_query, start_index, items_per_list)