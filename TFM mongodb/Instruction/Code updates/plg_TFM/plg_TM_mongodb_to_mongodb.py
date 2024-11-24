

from a0_items import * 
import pymongo 
from pymongo import MongoClient
from pprint import pprint
import bson
from plg_DB_MongoDB_2 import * 


##### Must download & install MongoDB software from --> https://www.mongodb.com/try/download/community #######
# https://www.w3schools.com/python/python_mongodb_getstarted.asp


##### Task mode - MongoDB to MongoDB #########################################


def get_LIST_raw_ALL (raw_conn_str, raw_db_name):

   LIST_raw_ALL = get_ALL_collection_in_db (conn_str=raw_conn_str, db_name=raw_db_name)
   
   return LIST_raw_ALL 
   
 
#get_LIST_raw_ALL (conn_str="mongodb://localhost:27017/", raw_db_name="Country_language")
 
  
  
def get_LIST_cooked_ALL (cooked_conn_str, cooked_db_name):

   LIST_cooked_ALL = get_ALL_collection_in_db (conn_str=cooked_conn_str, db_name=cooked_db_name)
   
   return LIST_cooked_ALL 
   


# get selected collections by index
def get_LIST_raw_SELECTED (raw_conn_str, raw_start_coll_index, raw_end_coll_index):

   LIST_raw_ALL = get_LIST_raw_ALL (raw_conn_str=raw_conn_str, raw_db_name=raw_db_name)

   LIST_raw_selected = []
   
   for raw_collection in LIST_raw_ALL(raw_start_coll_index=raw_start_coll_index, raw_end_coll_index=raw_end_coll_index):
   
      LIST_raw_selected.append(raw_collection)
           
   return LIST_raw_selected
   
   
   
# get selected collections by index
def get_LIST_cooked_SELECTED (cooked_conn_str, cooked_db_name, cooked_start_coll_index, cooked_end_coll_index):

   LIST_cooked_ALL = get_LIST_cooked_ALL (cooked_conn_str=cooked_conn_str, cooked_db_name=cooked_db_name)

   LIST_cooked_selected = []
   
   for cooked_collection in LIST_cooked_ALL(cooked_start_coll_index=cooked_start_coll_index, cooked_end_coll_inde=cooked_end_coll_index):
   
      LIST_cooked_selected.append(cooked_collection)
           
   return LIST_cooked_selected



############################################################
##### RAW, COOKED, TO_BE documents #######

def get_raw_DOCS (raw_conn_str, raw_db_name, raw_coll):

   LIST_all_doc = get_ALL_docs_in_collection (conn_str=raw_conn_str, db_name=raw_db_name,  coll_name=raw_coll)
  
   print (LIST_all_doc)
   return LIST_all_doc
   
  
  
def get_cooked_DOCS (cooked_conn_str, cooked_db_name, cooked_coll):

   LIST_all_doc = get_ALL_docs_in_collection (conn_str=cooked_conn_str, db_name=cooked_db_name,  coll_name=cooked_coll)   
   
   print (LIST_all_doc)  
   return LIST_all_doc
   


#### Select data with status = Completed, In progress, Not completed within allowed task duration
def get_cooked_DOCS_by_status (cooked_conn_str, cooked_db_name, cooked_coll, cooked_doc_key_1):

   LIST_all_cooked_doc = get_cooked_DOCS (conn_str= cooked_conn_str, cooked_db_name=cooked_db_name, cooked_coll=cooked_coll)
   
   LIST_selected_doc = []
      
   for doc in LIST_all_doc:
   
      doc_value = doc[cooked_doc_key_1]
      
      # If the doc status = Completed, In progress, or not completed within allowed task duration, don't select the doc
      if 'Completed' in doc_value and 'In progress' in doc_value and 'Not completed within allowed task duration'  in doc_value:
         
         pass
      
      else:
   
         LIST_selected_doc.append (doc)
         print (doc)    
   
   
   return LIST_selected_doc   
   
   
#doc_key_1 = 'Status'



# Use get_cooked_docs_by_status is better 
def get_TO_BE_DOCS (raw_conn_str, raw_db_name, raw_coll, cooked_conn_str, cooked_db_name, cooked_coll, raw_doc_key, cooked_doc_key):

   LIST_raw_doc = get_raw_DOCS (raw_conn_str=raw_conn_str, raw_db_name=raw_db_name, raw_coll = raw_coll)
   LIST_cooked_doc = get_cooked_DOCS_by_status (cooked_conn_str=cooked_conn_str, cooked_db_name=cooked_db_name, cooked_coll=cooked_coll, cooked_doc_key_1=cooked_doc_key)
   
   LIST_to_be_doc = []
   
   #need to match raw & cooked docs by using doc key = doc title 
        
   for raw_doc in LIST_raw_doc:
    
      for cooked_doc in LIST_cooked_doc:
      
         raw_doc=raw_doc[raw_doc_key=raw_doc_key]
         cooked_doc=cooked_doc[cooked_doc_key=cooked_doc_key]
       
         if raw_doc in cooked_doc:
          
            print (raw_doc + ' in ' + cooked_doc)
            
         else:
         
            print (raw_doc + ' NOT in ' + cooked_doc)
            LIST_to_be_doc.append(raw_doc)
   
   #print ('LIST to be documents => ' + str(LIST_test_to_be_doc))   
   return LIST_to_be_doc 
   
   
   
# each doc is a list item of a list, split list into separate lists or chunks
def split_to_be_DOCS (raw_conn_str, raw_db_name, raw_coll, cooked_conn_str, cooked_db_name, cooked_coll, raw_doc_key, cooked_doc_key, start_index, docs_per_list):
 
   LIST_to_be_DOC = get_TO_BE_DOCS (raw_conn_str=raw_conn_str, raw_db_name=raw_db_name, raw_coll=raw_coll, cooked_conn_str=cooked_conn_str, cooked_db_name=cooked_db_name, cooked_coll=cooked_coll, raw_doc_key=raw_doc_key, cooked_doc_key=cooked_doc_key)
   
   
   return list_SPLIT_1 (LIST_to_split = LIST_to_be_DOC, start_index = start_index, docs_per_list = docs_per_list)



'''
# do the task on 1 data item, eg send email, post comment   
## this method needs to be created from scratch to be used by CF_data_chunk (LIST_item)
def do_one_DOC (task_func):

   #task_func is the variable to wrap the function, eg task_func = send_email (email)
   do_task = task_func

   return do_task    
'''   
   
   

#####################################################################
##### Selected TO_BE collections with TO_BE documents

def get_LIST_to_be_SELECTED_with_doc(raw_conn_str, raw_start_coll_index, raw_end_coll_index, raw_db_name, raw_doc_key, cooked_conn_str, cooked_db_name, cooked_start_coll_index, cooked_end_coll_index, cooked_doc_key):

   LIST_raw_coll_SELECTED =  get_LIST_raw_SELECTED (conn_str = raw_conn_str, start_coll_index = raw_start_coll_index, end_coll_index = raw_end_coll_index)
   LIST_cooked_coll_SELECTED = get_LIST_cooked_SELECTED (conn_str = cooked_conn_str, start_coll_index = cooked_start_coll_index, end_coll_index = cooked_end_coll_index)
   
   #TO_BE docs & data 
   LIST_to_be_coll_doc_SELECTED = []
   
   # get_TO_BE_DOCS returns a list of TO_BE docs 
   for raw_coll, cooked_coll in zip(LIST_raw_collection_SELECTED, LIST_cooked_collection_SELECTED):

      LIST_to_be_coll_doc_SELECTED.append( raw_coll + ' #_0 ' + get_TO_BE_DOCS (raw_conn_str=raw_conn_str, raw_db_name=raw_db_name, raw_coll=raw_coll, raw_doc_key = raw_doc_key, cooked_conn_str=cooked_conn_str, cooked_db_name=cooked_db_name, cooked_coll=cooked_coll, cooked_doc_key=cooked_doc_key) )

   return LIST_to_be_coll_doc_SELECTED


#get_LIST_to_be_SELECTED_with_doc(raw_conn_str, raw_start_coll_index, raw_end_coll_index, raw_db_name, raw_doc_key, cooked_conn_str, cooked_db_name, cooked_start_coll_index, cooked_end_coll_index, cooked_doc_key)



#################################################################
###### Concurrent futures on document chunks ########################


# data doc --> data items --> data chunks (or data item chunks) 

## do_task_DOC --> CF_data_chunk (LIST_item) --> CF_all_doc_chunk (start_coll_index , end_coll_index , raw_db_name, cooked_db_name, start_index, docs_per_list)

def CF_doc_chunk (LIST_doc):

   with concurrent.futures.ProcessPoolExecutor() as executor:
        
      executor.map(do_one_DOC, LIST_doc)
        
      t2 = time.perf_counter()
      print (f' finished in {t2} seconds')      



# Concurrent futures on TO_BE data chunks only
def CF_all_doc_chunk (raw_conn_str, raw_db_name, raw_coll, raw_start_coll_index, raw_end_coll_index, raw_doc_key, cooked_conn_str, cooked_db_name, cooked_coll, cooked_start_coll_index, cooked_end_coll_index, cooked_doc_key, start_index, docs_per_list, do_one_DOC):
  
   # LIST TO_BE doc & data
   LIST_to_be_doc_data = get_LIST_to_be_SELECTED_with_doc(raw_conn_str=raw_conn_str, raw_start_coll_index=raw_start_coll_index, raw_end_coll_index=raw_end_coll_index, raw_db_name=raw_db_name, raw_doc_key=raw_doc_key, cooked_conn_str=cooked_conn_str, cooked_db_name=cooked_db_name, cooked_start_coll_index=cooked_start_coll_index, cooked_end_coll_index=cooked_end_coll_index, cooked_doc_key=cooked_doc_key )
   
   start_coll_index = raw_start_coll_index
   end_coll_index = raw_end_coll_index
    
   # Loop through EACH selected to_be data doc 
   for doc in LIST_to_be_coll_data[start_coll_index:end_coll_index]:

      LIST_to_be_doc_only = remove_all_after_text (after_text= ' #_0 ' , text_main = data_doc)
      LIST_doc_item_only = remove_all_before_text (before_text= ' #_0 ', text_main = data_doc)
              
      for doc_items in LIST_doc_item_only:
      
         #LIST_data_item_chunk = split_LIST_data_item  (LIST_to_split=LIST_data_item_only, start_index=start_index, items_per_list=items_per_list)         
         LIST_doc_item_chunk = split_to_be_DOCS (raw_conn_str=raw_conn_str, raw_db_name=raw_db_name, raw_coll=raw_coll,  cooked_conn_str, cooked_db_name=cooked_db_name, cooked_coll=cooked_coll, raw_doc_key=raw_doc_key, cooked_doc_key=cooked_doc_key, start_index, docs_per_list)
      
         for doc_chunk in LIST_doc_item_chunk:    
                  
            CF_doc_chunk (do_one_DATA_ITEM, LIST_doc=doc_chunk)   


#do_task_DOC --> need write this function to be used by CF_data_chunk (LIST_item)

raw_conn_str = ''
raw_db_name = ''
raw_coll = ''
raw_doc_key = ''
raw_start_coll_index = ''
raw_end_coll_index = ''

cooked_conn_str = ''
cooked_db_name = ''
cooked_coll = ''
cooked_doc_key = ''
cooked_start_coll_index = ''
cooked_end_coll_index = ''

start_index = ''
docs_per_list = ''

do_one_DOC = ''# this is a function to complete 1 document
LIST_item = ''



#CF_all_doc_chunk (raw_conn_str, raw_db_name, raw_coll, raw_start_coll_index, raw_end_coll_index, raw_doc_key, cooked_conn_str, cooked_db_name, cooked_coll, cooked_start_coll_index, cooked_end_coll_index, cooked_doc_key, start_index, docs_per_list)