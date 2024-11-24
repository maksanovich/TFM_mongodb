

from a0_items import * 
import pymongo 
from pymongo import MongoClient
from pprint import pprint
import bson
from plg_DB_MongoDB_2 import * 

from plg_Files import * 
from plg_Folders import * 


##### Must download & install MongoDB software from --> https://www.mongodb.com/try/download/community #######
# https://www.w3schools.com/python/python_mongodb_getstarted.asp



def get_LIST_raw_ALL (raw_conn_str, raw_db_name):

   LIST_raw_ALL = get_ALL_collection_in_db (raw_conn_str, raw_db_name)
   
   return LIST_raw_ALL 
   
 
#get_LIST_raw_ALL (raw_conn_str="mongodb://localhost:27017/", raw_db_name="Country_language")
 
  
  
# get a list of cooked files 
def get_LIST_cooked_ALL (cooked_folder_path):

   LIST_cooked_ALL = get_ALL_in_folder (folder_path=cooked_folder_path)
   
   return LIST_cooked_ALL 
   
 
#get_LIST_cooked_ALL (folder_path)
   


# get selected collections by index
def get_LIST_raw_SELECTED (raw_conn_str, raw_start_coll_index, raw_end_coll_index):

   LIST_raw_ALL = get_LIST_raw_ALL (raw_conn_str=raw_conn_str, raw_db_name=raw_db_name)

   LIST_raw_selected = []
   
   for raw_collection in LIST_raw_ALL(raw_start_coll_index=raw_start_coll_index, raw_end_coll_index=raw_end_coll_index):
   
      LIST_raw_selected.append(raw_collection)
           
   return LIST_raw_selected
   
   
   
# get selected files by index
def get_LIST_cooked_SELECTED (cooked_folder_path, cooked_start_file_index, cooked_end_file_index):

   LIST_cooked_ALL = get_LIST_cooked_ALL (folder_path=cooked_folder_path)

   LIST_cooked_selected = []
   
   for cooked_file in LIST_cooked_ALL(cooked_start_file_index=cooked_start_file_index, cooked_end_file_index=cooked_end_file_index):
   
      LIST_raw_selected.append(cooked_file)
           
   return LIST_cooked_selected



############################################################
##### RAW, COOKED, TO_BE documents #######

def get_raw_DOCS (raw_conn_str, raw_db_name, raw_coll):

   LIST_all_doc = get_ALL_docs_in_collection (raw_conn_str=raw_conn_str, db_name=db_name,  coll_name=raw_coll)
  
   print (LIST_all_doc)
   return LIST_all_doc
   
  
  
#### Select data with log status = Completed, In progress, Not completed within allowed task duration
def get_cooked_DATA_ITEMS (cooked_file_path):
  
   LIST_cooked_data_item = File_read_lines (file_path = cooked_file_path)
   
   return LIST_cooked_data_item



def get_TO_BE_DOCS (raw_conn_str, raw_coll, cooked_coll, raw_doc_key, cooked_doc_key, cooked_file_path):

   LIST_raw_doc = get_raw_DOCS (raw_conn_str=raw_conn_str, raw_db_name=raw_db_name, raw_coll = raw_coll)
   LIST_cooked_data_tiem = get_cooked_DATA_ITEMS (cooked_file_path = cooked_file_path)
   
   LIST_to_be_doc = []
   
   #need to match raw & cooked docs by using doc key = doc title 
        
   for raw_doc in LIST_raw_doc:
    
      for cooked_data_item in LIST_cooked_data_item:
      
         raw_data=raw_doc[raw_doc_key]
       
         if raw_data in cooked_data:
          
            print (raw_data + ' in ' + cooked_data)
            
         else:
         
            print (raw_data + ' NOT in ' + cooked_data)
            LIST_to_be_doc.append(raw_doc)
   
   #print ('LIST to be documents => ' + str(LIST_test_to_be_doc))   
   return LIST_to_be_doc 
   
   
   
# each doc is a list item of a list, split list into separate lists
def split_to_be_DOCS (raw_conn_str, raw_db_name, raw_coll, raw_doc_key, cooked_folder_path,cooked_file_path start_index, docs_per_list):
 
   LIST_to_be_DOC = get_TO_BE_DOCS (raw_conn_str=raw_conn_str, raw_coll=raw_coll, raw_doc_key=raw_doc_key, cooked_file_path)
   
   
   return list_SPLIT_1 (LIST_to_split = LIST_to_be_DOC, start_index = start_index, docs_per_list = docs_per_list)


'''
# do the task on 1 data item, eg send email, post comment   
## this method needs to be created from scratch to be used by CF_data_chunk (LIST_item)
def do_one_DOC (doc):

   #To insert or update docs here
   print (doc)   
'''   
   

#####################################################################
##### Selected TO_BE collections with TO_BE documents

def get_LIST_to_be_SELECTED_with_doc(raw_conn_str, raw_start_coll_index, raw_end_coll_index, raw_db_name, cooked_folder_path, cooked_file_path, cooked_start_file_index, cooked_end_file_index):

   LIST_raw_coll_SELECTED =  get_LIST_raw_SELECTED (conn_str = raw_conn_str, raw_start_coll_index = raw_start_coll_index, raw_end_coll_index = raw_end_coll_index)
   LIST_cooked_coll_SELECTED = get_LIST_cooked_SELECTED (cooked_folder_path=cooked_folder_path, cooked_start_file_index=cooked_start_file_index, cooked_end_file_index=cooked_end_file_index)
   
   #TO_BE files & data 
   LIST_to_be_coll_doc_SELECTED = []
   
   # get_TO_BE_DOCS returns a list of TO_BE docs 
   for raw_coll, cooked_coll in zip(LIST_raw_collection_SELECTED, LIST_cooked_collection_SELECTED):

      LIST_to_be_coll_doc_SELECTED.append( raw_coll + ' #_0 ' + get_TO_BE_DOCS (raw_conn_str=raw_conn_str, raw_db_name=raw_db_name, raw_coll=raw_coll, raw_doc_key = raw_doc_key, cooked_conn_str=cooked_conn_str, cooked_db_name=cooked_db_name, cooked_coll=cooked_coll, cooked_doc_key=cooked_doc_key)  )

   return LIST_to_be_coll_doc_SELECTED


#get_LIST_to_be_SELECTED_with_doc (raw_conn_str, start_collection, end_collection, raw_db_name, cooked_db_name )



#################################################################
###### Concurrent futures on document chunks ########################


# data file --> data items --> data chunks (or data item chunks) 

## do_task_DOC --> CF_data_chunk (LIST_item) --> CF_all_data_chunk (start_file, end_file, raw_folder_path, cooked_folder_path, DB_file_name, start_index, items_per_list)

def CF_doc_chunk (LIST_doc):

   with concurrent.futures.ProcessPoolExecutor() as executor:
        
      executor.map(do_one_DOC, LIST_doc=LIST_doc)
        
      t2 = time.perf_counter()
      print (f' finished in {t2} seconds')      



# Concurrent futures on TO_BE data chunks only
def CF_all_doc_chunk (raw_conn_str, raw_db_name, raw_coll, raw_start_coll_index, raw_end_coll_index, raw_doc_key, cooked_folder_path, cooked_file_path, start_index, docs_per_list, do_one_DOC):
  
   # LIST TO_BE file & data
   LIST_to_be_file_data = get_LIST_to_be_SELECTED_with_doc(raw_conn_str=raw_conn_str, raw_start_coll_index=raw_start_coll_index, raw_end_coll_index=raw_end_coll_index, raw_db_name=raw_db_name, cooked_folder_path,  cooked_file_path=cooked_file_path)
   
   start_coll_index = raw_start_coll_index
   end_coll_index = raw_end_coll_index
   
   # Loop through EACH selected to_be data file 
   for doc in LIST_to_be_file_data[start_coll_index:end_coll_index]:

      LIST_to_be_file_only = remove_all_after_text (after_text= ' #_0 ' , text_main = data_file)
      LIST_data_item_only = remove_all_before_text (before_text= ' #_0 ', text_main = data_file)
              
      for data_items in LIST_data_item_only:
      
         #LIST_data_item_chunk = split_LIST_data_item  (LIST_to_split=LIST_data_item_only, start_index=start_index, items_per_list=items_per_list)         
         LIST_data_item_chunk = split_to_be_DOCS (raw_conn_str=raw_conn_str, raw_db_name=raw_db_name, raw_coll=raw_coll, raw_doc_key=raw_doc_key, cooked_folder_path=cooked_folder_path,cooked_file_path=cooked_file_path, start_index, docs_per_list)
      
         for data_item_chunk in LIST_data_item_chunk:    
                  
            CF_data_chunk (LIST_item=data_item_chunk)   


#do_task_DOC --> need write this function to be used by CF_data_chunk (LIST_item)

raw_conn_str = ''
raw_db_name = ''
raw_coll = ''
raw_doc_key = ''
raw_start_coll_index = ''
raw_end_coll_index = ''

cooked_folder_path
cooked_file_path
cooked_start_file_index
cooked_end_file_index

start_index = ''
doc_per_list = ''

do_one_DOC = ''# this is a function to complete 1 data item 
LIST_doc = ''


#CF_all_doc_chunk (raw_conn_str, raw_db_name, raw_coll, raw_start_coll_index, raw_end_coll_index, raw_doc_key, cooked_folder_path, cooked_file_path, start_index, docs_per_list)