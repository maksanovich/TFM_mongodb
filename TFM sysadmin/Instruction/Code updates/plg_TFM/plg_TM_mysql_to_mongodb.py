

from a0_items import * 
import pymongo 
from pymongo import MongoClient
from pprint import pprint
import bson
from plg_DB_MongoDB_2 import * 


from concurrent.futures import ThreadPoolExecutor, wait
import concurrent.futures
import time 
import datetime


##### Must download & install MongoDB software from --> https://www.mongodb.com/try/download/community #######
# https://www.w3schools.com/python/python_mongodb_getstarted.asp



def get_LIST_raw_ALL (raw_My_host, raw_My_user, raw_My_pass):

   LIST_raw_ALL = Mysql_get_ALL_DB (My_host=raw_My_host, My_user=raw_My_user, My_pass=raw_My_pass)
   
   return LIST_raw_ALL 
   
 
#get_LIST_raw_ALL (raw_My_host, raw_My_user, raw_My_pass)
 
  
  
 # get a list of raw COLLECTIONS from a MongoDB database 
def get_LIST_cooked_ALL (cooked_conn_str, cooked_db_name):

   LIST_cooked_ALL = get_ALL_collection_in_db (conn_str, cooked_db_name)
   
   return LIST_cooked_ALL 
   



def get_LIST_raw_SELECTED ( raw_My_host, raw_My_user, raw_My_pass,raw_start_db_index, raw_end_db_index,):

   LIST_raw_ALL = get_LIST_raw_ALL (raw_My_host=raw_My_host, raw_My_user=raw_My_user, raw_My_pass=raw_My_pass)

   LIST_raw_selected = []
   
   for raw_db in LIST_raw_ALL(raw_start_db_index=raw_start_db_index, raw_end_db_index=raw_end_db_index):
   
      LIST_raw_selected.append(raw_db)
           
   return LIST_raw_selected
   
   
   
   
# get selected collections by index
def get_LIST_cooked_SELECTED (cooked_conn_str, cooked_db_name, cooked_start_coll_index, cooked_end_coll_index):

   LIST_cooked_ALL = get_LIST_cooked_ALL (cooked_conn_str=cooked_conn_str, cooked_db_name=cooked_db_name)

   LIST_cooked_selected = []
   
   for cooked_collection in LIST_cooked_ALL(cooked_start_coll_index=cooked_start_coll_index, cooked_end_coll_index=ciooked_end_coll_index)::
   
      LIST_cooked_selected.append(cooked_collection)
           
   return LIST_cooked_selected



############################################################
##### RAW, COOKED, TO_BE documents #######

def get_raw_DATA_ITEMS (raw_My_host, raw_My_user, raw_My_pass , raw_My_db_name, raw_My_select_query):
  
   LIST_raw_data_item = Mysql_select_tb_data (My_host=raw_My_host, My_user=raw_My_user, My_pass=raw_My_pass , My_db_name=raw_My_db_name, My_select_query=raw_My_select_query)
   
   return LIST_raw_data_item
   
  
  
#### Select data with log status = Completed, In progress, Not completed within allowed task duration
def get_cooked_DOCS (cooked_conn_str, cooked_db_name, cooked_coll):

   LIST_all_doc = get_ALL_docs_in_collection (cooked_conn_str=cooked_conn_str, db_name=db_name,  coll_name=cooked_coll)
     
   print (LIST_all_doc)
   return LIST_all_doc



def get_TO_BE_DATA_ITEMS (raw_My_host, raw_My_user, raw_My_pass , raw_My_db_name, raw_My_select_query, cooked_conn_str, cooked_db_name, cooked_coll, cooked_doc_key):

   LIST_raw_data_item = get_raw_DATA_ITEMS (raw_My_host=raw_My_host, raw_My_user=raw_My_user, raw_My_pass=raw_My_pass , raw_My_db_name=raw_My_db_name, raw_My_select_query=raw_My_select_query)
   LIST_cooked_doc = get_cooked_DOCS (cooked_conn_str=cooked_conn_str, cooked_db_name=cooked_db_name, cooked_coll = cooked_collection)
   
   LIST_to_be_data_item = []
   
   #need to match raw & cooked docs by using doc key = doc title 
        
   for raw_data in LIST_raw_data_item:
    
      for cooked_doc in LIST_cooked_doc:
            
         if raw_data in cooked_doc:
          
            print (raw_data + ' in ' + cooked_doc)
            
         else:
         
            print (raw_data + ' NOT in ' + cooked_doc)
            LIST_to_be_data_item.append(raw_data_item)
   
   #print ('LIST to be documents => ' + str(LIST_test_to_be_doc))   
   return LIST_to_be_data_item
   
   
   
# each doc is a list item of a list, split list into separate lists
def split_to_be_DATA_ITEMS (raw_My_host, raw_My_user, raw_My_pass , raw_My_db_name, raw_My_select_query, cooked_conn_str, cooked_db_name, cooked_coll, cooked_doc_key, start_index, items_per_list ):
 
   LIST_to_be_DATA_ITEM = get_TO_BE_DATA_ITEMS (raw_My_host=raw_My_host, raw_My_user=raw_My_user, raw_My_pass=raw_My_pass , raw_My_db_name=raw_My_db_name, raw_My_select_query=raw_My_select_query, cooked_conn_str=cooked_conn_str, cooked_db_name=cooked_db_name, cooked_coll=cooked_coll, cooked_doc_key=cooked_doc_key)
   
   
   return list_SPLIT_1 (LIST_to_split = LIST_to_be_DATA_ITEM, start_index = start_index, items_per_list = items_per_list)



'''
# do the task on 1 data item, eg send email, post comment   
## this method needs to be created from scratch to be used by CF_data_chunk (LIST_item)
def do_one_DATA_ITEM (data_item):

   #This function needs to be rewritten or over-written 
   print (data_item)   
'''   
   

#####################################################################
##### Selected TO_BE data items 

def get_LIST_to_be_SELECTED_with_data_items( raw_My_host, raw_My_user, raw_My_pass, raw_start_db_index, raw_end_db_index, cooked_conn_str, cooked_start_coll_index, cooked_end_coll_index ):

   LIST_raw_data_SELECTED =  get_LIST_raw_SELECTED (raw_start_db_index=raw_start_db_index, raw_end_db_index=raw_end_db_index, raw_My_host=raw_My_host, raw_My_user=raw_My_user, raw_My_pass=raw_My_pass, raw_start_db_index =raw_start_db_index , raw_end_db_index=raw_end_db_index)
   LIST_cooked_coll_SELECTED = get_LIST_cooked_SELECTED (cooked_conn_str = cooked_conn_str, cooked_start_coll_index = cooked_start_coll_index, cooked_end_coll_index = cooked_end_coll_index)
   
   #TO_BE database data
   LIST_to_be_db_data_SELECTED = []
   
   # get_TO_BE_DATA_ITEM returns a list of TO_BE data items 
   for raw_data, cooked_coll in zip(LIST_raw_data_SELECTED, LIST_cooked_collection_SELECTED):

      LIST_to_be_db_data_SELECTED.append( raw_data+ ' #_0 ' + get_TO_BE_DATA_ITEMS (cooked_conn_str=cooked_conn_str, raw_data,raw_My_host=raw_My_host, raw_My_user=raw_My_user, raw_My_pass=raw_My_pass , raw_My_db_name=raw_My_db_name, raw_My_select_query = raw_My_select_query, cooked_coll=cooked_coll, cooked_doc_key=cooked_doc_key) )

   return LIST_to_be_db_data_SELECTED


#get_LIST_to_be_SELECTED_with_data_items (cooked_conn_str, start_collection, end_collection, raw_db_name, cooked_db_name )



#################################################################
###### Concurrent futures on data item chunks ########################


# database --> data items --> data chunks (or data item chunks) 


def CF_data_chunk (LIST_item):

   with concurrent.futures.ProcessPoolExecutor() as executor:
        
      executor.map(do_one_DATA_ITEM, LIST_item)
        
      t2 = time.perf_counter()
      print (f' finished in {t2} seconds')  



# Concurrent futures on TO_BE data chunks only
def CF_all_doc_chunk (raw_My_host, raw_My_user, raw_My_pass , raw_My_db_name, raw_My_select_query, cooked_start_coll_index , cooked_end_coll_index , cooked_db_name, start_index, items_per_list, do_one_DATA_ITEM):
  
   # LIST TO_BE file & data
   LIST_to_be_db_data = get_LIST_to_be_SELECTED_with_data_items (start_collection = start_file, end_collection = end_file, raw_db_name=raw_db_name, cooked_db_name=cooked_db_name )
   
   # Loop through EACH selected to_be data file 
   for db_data in LIST_to_be_db_data[start_collection:end_collection]:

      LIST_to_be_db_only = remove_all_after_text (after_text= ' #_0 ' , text_main = db_data)
      LIST_data_item_only = remove_all_before_text (before_text= ' #_0 ', text_main = db_data)
              
      for data_items in LIST_data_item_only:
      
         #LIST_data_item_chunk = split_LIST_data_item  (LIST_to_split=LIST_data_item_only, start_index=start_index, items_per_list=items_per_list)         
         LIST_data_item_chunk = split_to_be_DATA_ITEMS (raw_My_host=raw_My_host, raw_My_user=raw_My_user, raw_My_pass=raw_My_pass , raw_My_db_name=raw_My_db_name, raw_My_select_query=raw_My_select_query, cooked_conn_str=cooked_conn_str, cooked_db_name=cooked_db_name, cooked_coll=cooked_coll, cooked_doc_key=cooked_doc_key, start_index=start_index, items_per_list=items_per_list )
      
         for data_item_chunk in LIST_data_item_chunk:    
                  
            CF_data_chunk (LIST_item=data_item_chunk)   


#do_task_DOC --> need write this function to be used by CF_data_chunk (LIST_item)

raw_My_host= ''
raw_My_user = ''
raw_My_pass = ''
raw_My_db_name = ''
raw_start_db_index
raw_end_db_index

cooked_conn_str
cooked_start_coll_index = ''
cooked_end_coll_index = ''
cooked_db_name = ''

start_index = ''
docs_per_list = ''

do_one_DATA_ITEM = ''# this is a function to complete 1 data item 
LIST_item = ''


#CF_all_doc_chunk (=raw_My_host, raw_My_user, raw_My_pass , raw_My_db_name, raw_My_select_query, cooked_start_coll_index , cooked_end_coll_index , raw_db_name, cooked_db_name, start_index, items_per_list)