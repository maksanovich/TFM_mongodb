

from a0_items import * 
import pymongo 
from pymongo import MongoClient
from pprint import pprint
import bson
from plg_DB_MongoDB_2 import * 

from plg_Files import * 
from plg_Folders import * 

from concurrent.futures import ThreadPoolExecutor, wait
import concurrent.futures
import time 
import datetime

##### Must download & install MongoDB software from --> https://www.mongodb.com/try/download/community #######
# https://www.w3schools.com/python/python_mongodb_getstarted.asp


##### CSV to MongoDB #########################################


def get_LIST_raw_ALL (raw_folder_path):

   LIST_raw_ALL = get_ALL_in_folder (folder_path=raw_folder_path)
   
   return LIST_raw_ALL 
   
 
#get_LIST_raw_ALL (folder_path)
 
  
  
def get_LIST_cooked_ALL (cooked_conn_str, cooked_db_name):

   LIST_cooked_ALL = get_ALL_collection_in_db (conn_str=cooked_conn_str, cooked_db_name=cooked_db_name)
   
   return LIST_cooked_ALL 
   


# get selected csvs by index
def get_LIST_raw_SELECTED (raw_folder_path, raw_raw_start_csv_index, raw_raw_end_csv_index):

   LIST_raw_ALL = get_LIST_raw_ALL (raw_folder_path=raw_folder_path)

   LIST_raw_selected = []
   
   for raw_csv in LIST_raw_ALL(raw_start_csv_index=raw_start_csv_index, raw_end_csv_index=raw_end_csv_index):
   
      LIST_raw_selected.append(raw_csv)
           
   return LIST_raw_selected
   
   
   
# get selected collections by index
def get_LIST_cooked_SELECTED (cooked_conn_str, cooked_db_name, cooked_start_coll_index, cooked_end_coll_index):

   LIST_cooked_ALL = get_LIST_cooked_ALL (cooked_conn_str=cooked_conn_str, cooked_db_name=cooked_db_name)

   LIST_cooked_selected = []
   
   for cooked_collection in LIST_cooked_ALL(cooked_start_coll_index=cooked_start_coll_index, cooked_end_coll_index=cooked_end_coll_index):
   
      LIST_cooked_selected.append(cooked_collection)
           
   return LIST_cooked_selected



############################################################
##### RAW, COOKED, TO_BE documents #######

def get_raw_DATA_ITEMS (raw_csv_path):
  
   LIST_raw_data_item = CSV_dict_reader ( path_CSV)
   
   return LIST_raw_data_item
   
  
  
#### Select data with log status = Completed, In progress, Not completed within allowed task duration
def get_cooked_DOCS (cooked_conn_str, cooked_db_name, cooked_coll):

   LIST_all_doc = get_ALL_docs_in_collection (conn_str=cooked_conn_str, db_name=cooked_db_name,  coll_name=cooked_coll)
     
   print (LIST_all_doc)
   return LIST_all_doc



def get_TO_BE_DATA_ITEMS (raw_csv_path, cooked_conn_str, cooked_db_name, cooked_coll):

   LIST_raw = get_raw_DATA_ITEMS (raw_csv_path = raw_csv_path)
   LIST_cooked = get_cooked_DOCS(cooked_conn_str=cooked_conn_str, cooked_db_name=cooked_db_name, cooked_coll=cooked_coll)
   
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
def split_to_be_DATA_ITEMS (raw_csv_path, cooked_csv_path, start_index, items_per_list):
 
   LIST_to_be_DATA_ITEM = get_TO_BE_DATA_ITEMS (raw_csv_path = raw_csv_path, cooked_csv_path = cooked_csv_path)
   
   return list_SPLIT_1 (LIST_to_split = LIST_to_be_DATA_ITEM, start_index = start_index, items_per_list = items_per_list)



'''
# do the task on 1 data item, eg send email, post comment   
## this method needs to be created from scratch to be used by CF_data_chunk (LIST_item)
def do_one_DATA_ITEM (doc):

   #To insert or update docs here
   print (doc)   
'''   
   

#####################################################################
##### Selected TO_BE collections with TO_BE documents

#####################################################################
##### Selected TO_BE data csvs with TO_BE data items 

def get_LIST_to_be_SELECTED_with_data_items ( raw_folder_path, raw_raw_start_csv_index, raw_raw_end_csv_index, cooked_conn_str, cooked_db_name, cooked_start_coll_index, cooked_end_coll_index):

   LIST_raw_csv_SELECTED =  get_LIST_raw_SELECTED (raw_folder_path=raw_folder_path, raw_raw_start_csv_index=raw_start_csv_index, raw_raw_end_csv_index=raw_end_csv_index)
   LIST_cooked_csv_SELECTED = get_LIST_cooked_SELECTED (cooked_conn_str=cooked_conn_str, cooked_db_name=cooked_db_name, cooked_start_coll_index=cooked_start_coll_index, cooked_end_coll_index=cooked_end_coll_index)
   
   #TO_BE csvs & data 
   LIST_to_be_csv_data_SELECTED = []
   
   # get_TO_BE_DATA_ITEMS returns a list of TO_BE data 
   for raw_csv, cooked_coll zip(LIST_raw_csv_SELECTED, LIST_cooked_coll_SELECTED):

      LIST_to_be_csv_data_SELECTED.append( raw_csv + ' #_0 ' +  get_TO_BE_DATA_ITEMS (raw_csv_path=raw_csv_path, cooked_conn_str=cooked_conn_str, cooked_db_name=cooked_db_name, cooked_coll=cooked_coll))

   return LIST_to_be_csv_data_SELECTED


#get_LIST_to_be_SELECTED_with_data_items (raw_start_csv, raw_end_csv, raw_folder_path, cooked_folder_path )



#################################################################
###### Concurrent futures on data chunks ########################


# data csv --> data items --> data chunks (or data item chunks) 

## do_one_DATA_ITEM --> CF_data_chunk (LIST_item) --> CF_all_data_chunk (raw_start_csv, raw_end_csv, raw_folder_path, cooked_folder_path, start_index, items_per_list)

def CF_data_chunk (do_one_DATA_ITEM, LIST_item):

   with concurrent.futures.ProcessPoolExecutor() as executor:
        
      executor.map(do_one_DATA_ITEM, LIST_item)
        
      t2 = time.perf_counter()
      print (f' finished in {t2} seconds')      



# Concurrent futures on TO_BE data chunks only
def CF_all_data_chunk (raw_folder_path, raw_csv_path, raw_start_csv_index, raw_end_csv_index, cooked_conn_str, cooked_db_name, cooked_coll, cooked_doc_key, cooked_start_coll_index, cooked_end_coll_iondex, start_index, items_per_list, do_one_DATA_ITEM):
  
   # LIST TO_BE csv & data
   LIST_to_be_csv_data = get_LIST_to_be_SELECTED_with_data_items (raw_start_csv = raw_start_csv, raw_end_csv = raw_end_csv, raw_folder_path = raw_folder_path, cooked_folder_path = cooked_folder_path )
   
   start_csv_index = raw_start_csv_index
   end_csv_index = raw_end_csv_index
   
   # Loop through EACH selected to_be data csv 
   for data_csv in LIST_to_be_csv_data[start_csv_index:end_csv_index]:

      LIST_to_be_csv_only = remove_all_after_text (after_text= ' #_0 ' , text_main = data_csv)
      LIST_data_item_only = remove_all_before_text (before_text= ' #_0 ', text_main = data_csv)
              
      for data_items in LIST_data_item_only:
      
         #LIST_data_item_chunk = split_LIST_data_item  (LIST_to_split=LIST_data_item_only, start_index=start_index, items_per_list=items_per_list)         
         LIST_data_item_chunk = split_to_be_DATA_ITEMS (raw_csv_path = raw_csv_path, cooked_csv_path = cooked_csv_path, start_index=start_index, items_per_list=items_per_list)
      
         for data_item_chunk in LIST_data_item_chunk    
                  
            CF_data_chunk (do_one_DATA_ITEM = do_one_DATA_ITEM, LIST_item=data_item_chunk)   



#do_one_DATA_ITEM --> need write this function to be used by CF_data_chunk (LIST_item)

raw_folder_path = ''
raw_csv_path = ''
raw_start_csv_index = ''
raw_end_csv_index = ''

cooked_conn_str = ''
cooked_db_name = ''
cooked_coll = ''
cooked_doc_key = ''
cooked_start_coll_index = ''
cooked_end_coll_index = ''

start_index = ''
items_per_list = ''

do_one_DATA_ITEM = ''# this is a function to complete 1 data item 
LIST_item = ''


#CF_all_data_chunk (raw_folder_path, raw_csv_path, raw_start_csv_index, raw_end_csv_index, cooked_conn_str, cooked_db_name, cooked_coll, cooked_doc_key, cooked_start_coll_index, cooked_end_coll_iondex, start_index, items_per_list)