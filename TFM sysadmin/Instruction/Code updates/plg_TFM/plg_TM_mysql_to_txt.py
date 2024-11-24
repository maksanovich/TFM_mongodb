

from a0_items import * 
from plg_Files import * 
from plg_Folders import * 
from plg_DB_Mysql import *


from concurrent.futures import ThreadPoolExecutor, wait
import concurrent.futures
import time 
import datetime


def get_LIST_raw_ALL (raw_My_host, raw_My_user, raw_My_pass):

   LIST_raw_ALL = Mysql_get_ALL_DB (My_host= raw_My_host, My_user=raw_My_user, My_pass=raw_My_pass)
   
   return LIST_raw_ALL 
   
 
#get_LIST_raw_ALL (raw_My_host, raw_My_user, raw_My_pass)
 
  
  
def get_LIST_cooked_ALL (cooked_folder_path):

   LIST_cooked_ALL =  get_ALL_in_folder (folder_path=cooked_folder_path)
   
   return LIST_cooked_ALL 
   


# get selected collections by index
def get_LIST_raw_SELECTED (raw_start_db_index, raw_end_db_index,raw_My_host, raw_My_user, raw_My_pass ):

   LIST_raw_ALL = get_LIST_raw_ALL (raw_My_host, raw_My_user, raw_My_pass)

   LIST_raw_selected = []
   
   for raw_collection in LIST_raw_ALL(raw_start_db_index, raw_end_db_index):
   
      LIST_raw_selected.append(raw_collection)
           
   return LIST_raw_selected
   
   
# get selected collections by index
def get_LIST_cooked_SELECTED (cooked_folder_path, cooked_start_file_index, raw_end_file_index):

   LIST_cooked_ALL = get_LIST_cooked_ALL (folder_path=cooked_folder_path)

   LIST_cooked_selected = []
   
   for cooked_file in LIST_cooked_ALL(cooked_start_file_index=cooked_start_file_index, cooked_end_file_index=cooked_end_file_index):
   
      LIST_raw_selected.append(cooked_file)
           
   return LIST_cooked_selected



############################################################
##### RAW, COOKED, TO_BE data #######

def get_raw_DATA_ITEMS (raw_My_host, raw_My_user, raw_My_pass, raw_My_db_name, raw_My_select_query):

   LIST_raw_data_item = Mysql_select_tb_data (My_host=raw_My_host, My_user=raw_My_user, My_pass=raw_My_pass , My_db_name=raw_My_db_name, My_select_query=raw_My_select_query)
   
   print (LIST_raw_data_item)
   return LIST_raw_data_item
  
   
  
  
#### Select data with log status = Completed, In progress, Not completed within allowed task duration
def get_cooked_DATA_ITEMS (cooked_file_path):

   LIST_cooked_data_item = File_read_lines (file_path = cooked_file_path)
   
   print (LIST_cooked_data_item)
   return LIST_cooked_data_item



def get_TO_BE_DATA_ITEMS (raw_My_host, raw_My_user, raw_My_pass, raw_My_db_name, raw_My_select_query,cooked_file_path ):

   LIST_raw_data = get_raw_DATA_ITEMS (raw_My_host=raw_My_host, raw_My_user=raw_My_user, raw_My_pass=raw_My_pass, raw_My_db_name=raw_My_db_name, raw_My_select_query=raw_My_select_query)
   LIST_cooked_data = get_cooked_DATA_ITEMS (cooked_file_path=cooked_file_path)
   
   LIST_to_be_data_item = []
   
   #need to match raw & cooked data_items by using data_item key = data_item title 
        
   for raw_data_item in LIST_raw_data_item:
    
      for cooked_data_item in LIST_cooked_data_item:
      
       
         if raw_data in cooked_data:
          
            print (raw_data + ' in ' + cooked_data)
            
         else:
         
            print (raw_data + ' NOT in ' + cooked_data)
            LIST_to_be_data_item.append(raw_data_item)
   
   #print ('LIST to be data_itemuments => ' + str(LIST_test_to_be_data_item))   
   return LIST_to_be_data_item 
   
   
   
# each data_item is a list item of a list, split list into separate lists
def split_to_be_DATA_ITEMS (raw_My_host, raw_My_user, raw_My_pass, raw_My_db_name, raw_My_select_query,cooked_file_path):
 
   LIST_to_be_DATA_ITEMS = get_TO_BE_DATA_ITEMS (raw_My_host=raw_My_host, raw_My_user=raw_My_user, raw_My_pass=raw_My_pass, raw_My_db_name=raw_My_db_name, raw_My_select_query=raw_My_select_query,cooked_file_path=cooked_file_path )
   
   
   return list_SPLIT_1 (LIST_to_split = LIST_to_be_DATA_ITEM, start_index = start_index, data_items_per_list = data_items_per_list)



'''
# do the task on 1 data item, eg send email, post comment   
## this method needs to be created from scratch to be used by CF_data_chunk (LIST_item)
def do_task_DATA_ITEMS (data_item):

   #To insert or update data_items here
   print (data_item)   
'''   
   

#####################################################################
##### Selected TO_BE collections with TO_BE data_itemuments

def get_LIST_to_be_SELECTED_with_data_items(raw_My_host, raw_My_user, raw_My_pass, raw_start_db_index, raw_end_db_index,cooked_folder_path, cooked_start_file_index, cooked_end_file_index ):

   LIST_raw_data_SELECTED =  get_LIST_raw_SELECTED (raw_My_host=cooked_My_host, raw_My_user=raw_My_user, raw_My_pass=raw_My_pass , raw_start_db_index=raw_start_db_index, raw_end_db_index=raw_end_db_index)
   LIST_cooked_data_SELECTED = get_LIST_cooked_SELECTED (folder_path = cooked_folder_path, start_file = cooked_start_file_index, end_file = cooked_end_file_index)
   
   #TO_BE files & data 
   LIST_to_be_coll_data_item_SELECTED = []
   
   # get_TO_BE_DATA_ITEMS returns a list of TO_BE data_items 
   for raw_data, cooked_data in zip(LIST_raw_collection_SELECTED, LIST_cooked_collection_SELECTED):

      LIST_to_be_data_item_SELECTED.append( raw_data + ' #_0 ' +  get_TO_BE_DATA_ITEMS (raw_My_host=raw_My_host, raw_My_user=raw_My_user, raw_My_pass=raw_My_pass, raw_My_db_name=raw_My_db_name, raw_My_select_query=raw_My_select_query,cooked_file_path=cooked_file_path ) )

   return LIST_to_be_data_item_SELECTED


#get_LIST_to_be_SELECTED_with_data_items (conn_str, start_collection, end_collection, raw_db_name, cooked_db_name )



#################################################################
###### Concurrent futures on data_itemument chunks ########################


# data file --> data items --> data chunks (or data item chunks) 

## do_task_DATA_ITEM --> CF_data_chunk (LIST_item) --> CF_all_data_chunk (start_file, end_file, raw_folder_path, cooked_folder_path, DB_file_name, start_index, items_per_list)

def CF_data_item_chunk (LIST_data_item):

   with concurrent.futures.ProcessPoolExecutor() as executor:
        
      executor.map(do_one_DATA_ITEM, LIST_data_item)
        
      t2 = time.perf_counter()
      print (f' finished in {t2} seconds')      



# Concurrent futures on TO_BE data chunks only
def CF_all_data_item_chunk (raw_My_host, raw_My_user, raw_My_pass, raw_start_db_index, raw_end_db_index,cooked_folder_path, cooked_file_path, cooked_start_file_index, cooked_end_file_index, do_one_DATA_ITEM):
  
   # LIST TO_BE file & data
   LIST_to_be_file_data = get_LIST_to_be_SELECTED_with_data_items(raw_My_host=raw_My_host, raw_My_user=raw_My_user, raw_My_pass=raw_My_pass, raw_start_db_index=raw_start_db_index, raw_end_db_index=raw_end_db_index,cooked_folder_path=cooked_folder_path, cooked_start_file_index=cooked_start_file_index, cooked_end_file_index=cooked_end_file_index, do_one_DATA_ITEM )
   
   start_db_index = raw_start_db_index
   end_db_index = raw_end_db_index
   
   
   # Loop through EACH selected to_be data file 
   for data_item in LIST_to_be_file_data[start_db_index:end_db_index]:

      LIST_to_be_file_only = remove_all_after_text (after_text= ' #_0 ' , text_main = data_file)
      LIST_data_item_only = remove_all_before_text (before_text= ' #_0 ', text_main = data_file)
              
      for data_items in LIST_data_item_only:
      
         #LIST_data_item_chunk = split_LIST_data_item  (LIST_to_split=LIST_data_item_only, start_index=start_index, items_per_list=items_per_list)         
         LIST_data_itek_chunk = split_to_be_DATA_ITEMS (raw_My_host=raw_My_host, raw_My_user=raw_My_user, raw_My_pass=raw_My_pass, raw_My_db_name=raw_My_db_name, raw_My_select_query=raw_My_select_query,cooked_file_path=cooked_folder_path +cooked_file_path)
      
         for data_item_chunk in LIST_data_item_chunk:    
                  
            CF_data_chunk (do_one_DATA_ITEM= do_one_DATA_ITEM, LIST_item=data_item_chunk)   


#do_task_DATA_ITEM --> need write this function to be used by CF_data_chunk (LIST_item)


raw_My_host = ''
raw_My_user = ''
raw_My_pass = ''
raw_My_db_name = ''
raw_My_select_query = ''
raw_My_start_db_index = ''
raw_My_end_db_index = ''

cooked_folder_path = ''
cooked_file_path = ''
cooked_start_file_index = ''
cooked_end_file_index = ''

start_index = ''
items_per_list = ''

do_one_DATA_ITEM = ''# this is a function to complete 1 data item 
LIST_item = ''



#CF_all_data_item_chunk (start_collection, end_collection, raw_db_name, cooked_db_name, start_index, data_items_per_list)