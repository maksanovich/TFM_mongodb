

from a0_items import * 
from plg_Folders import *
from plg_Files import *  
from plg_Date_time import * 
from plg_Regex import *

import pymongo 
from pymongo import MongoClient
from pprint import pprint
import bson
from plg_DB_MongoDB_2 import * 



##################################################################################################
### Task request schedule of TFM_master  #########################################################

def get_LIST_date (start_date, end_date):

   LIST_date = get_dt_every_day(start_date=start_date, end_date=end_date)[0]

   print (LIST_date)
   return LIST_date
   
#get_LIST_date (start_date=date(2024, 1, 1), end_date= date(2024, 12, 31))



def create_DB_task_request_schedule (conn_str):
 
   create_DB(conn_str =conn_str, db_name = 'Task_request_schedule',  coll_name='test_1')
   
  

# 1 calendar date per collection. TRS = Task request schedule    
def create_colls_TRS (start_date, end_date, conn_str):

   LIST_date = get_LIST_date (start_date=start_date, end_date=end_date)
   
   LIST_collection = []
   
   for date in LIST_date:
   
      LIST_collection.append(create_collection (conn_str=conn_str, db_name="Task_request_schedule", coll_name='TRS_' + date)) # TRS stands for Task request schedule
      
      
   return LIST_collection 
       
#create_colls_TRS(start_date=date(2024, 1, 1),, end_date= date(2024, 12, 31), conn_str="mongodb://localhost:27017/") 


#############################################################################################################3
#### Prepare data to create DOC for each TFM cluster #####


def get_ALL_cluster_name (folder_path):

   LIST_cluster_name = []
   
   LIST_subfolder_name = get_ALL_in_folder (folder_path=folder_path)
   
   for name in LIST_subfolder_name:
   
      if 'CLU_' in name:
      
         #TFM_name = name.replace('CLU_', 'TFM_')
      
         LIST_cluster_name.append (name)
   
   
   #print (LIST_cluster_name)
   return LIST_cluster_name


#get_ALL_cluster_name (folder_path='../../../../TFM_master/')




# get all server node IP of every TFM cluster (in the CLU_txt_task -> task -> plg_CUSTOM -> a1_nodes_list 
def get_LIST_TFM_cluster_node_ip_file (parent_folder_path, cluster_name,  node_ip_folder_path):

   
   LIST_node_ip_file_2 = []
   
   LIST_node_ip_file= get_ALL_in_folder (folder_path=parent_folder_path + cluster_name+ node_ip_folder_path)     
   #print (LIST_node_ip_file)
      
   LIST_node_ip_file.insert(0, cluster_name)#first element of the list must be the cluster name
   #print (LIST_node_ip_file)
      
   LIST_node_ip_file_2.append(LIST_node_ip_file)
      
      
   #print (LIST_node_ip_file_2)    
   return LIST_node_ip_file_2


#get_LIST_TFM_cluster_node_ip_file (parent_folder_path='../../../../TFM_master/', cluster_name=CLU_folder_task, node_ip_folder_path='/task/plg_CUSTOM/a1_nodes_list/')



# get TFM task request urls to be added to each server doc (in the CLU_txt_task -> task -> plg_CUSTOM -> a2_node_task_request
def get_LIST_TFM_task_request_file (parent_folder_path, cluster_name, request_url_folder_path):
  
   #List of list 
   LIST_url_file_2 = []
   
   LIST_url_file = get_ALL_in_folder (folder_path = parent_folder_path  + cluster_name + request_url_folder_path)
    
   LIST_url_file.insert(0, cluster_name)#first element of the list must be the cluster name
   #print (LIST_node_url_file)
      
   LIST_url_file_2.append(LIST_url_file)
         
   #print (LIST_url_file_2)    
   return LIST_url_file_2  
   
'''
LIST_cluster_name = get_ALL_cluster_name (folder_path=parent_folder_path)

for cluster_name in LIST_cluster_name:   
   #get_LIST_TFM_task_request_file (parent_folder_path='../../../../TFM_master/' + cluster_name + request_url_folder_path='/task/plg_CUSTOM/a2_nodes_task_request/')
   pass
'''


#create list for each round of request url 
def create_LIST_task_request_url (parent_folder_path, cluster_name, request_url_folder_path):

   # List of list 
   LIST_task_request_url_file = get_LIST_TFM_task_request_file (parent_folder_path=parent_folder_path, cluster_name=cluster_name, request_url_folder_path=request_url_folder_path)
   
   LIST_request_url_2 = []
   
   LOLIST_task_request_url = []
   
   for LIST_cluster_file in LIST_task_request_url_file: #list cluster + list file
   
      #print (LIST_cluster_file)
      pass
      
      for file in LIST_cluster_file[1:]:#file name starts from the 2nd index, the 1st index is the TFM name
      
         LIST_request_url = File_read_lines (file_path =parent_folder_path + LIST_cluster_file[0] + request_url_folder_path + file)
         
         cluster_name =  LIST_cluster_file[0]
         #print (cluster_name)
          
         LIST_request_url.insert(0, cluster_name)
         #print(LIST_request_url)
         
         LIST_request_url_2.append(LIST_request_url)
  
   #print (LIST_request_url_2 ) 
   return LIST_request_url_2
    
    
#create_LIST_task_request_url (parent_folder_path='../../../../TFM_master/', cluster_name='CLU_folder_tasks', request_url_folder_path='/task/plg_CUSTOM/a2_nodes_task_request/')   
   
'''   
LIST_cluster_name = get_ALL_cluster_name (folder_path='../../../../TFM_master/')

for cluster_name in LIST_cluster_name:   

   LIST_url = create_LIST_task_request_url (parent_folder_path='../../../../TFM_master/', cluster_name=cluster_name, request_url_folder_path='/task/plg_CUSTOM/a2_nodes_task_request/')   
   
   print (LIST_url)
 '''  
   
#################################################################################################################################################
######## create cluster doc profile data    

'''
def create_LIST_cluster_doc_data (parent_folder_path, cluster_name, node_ip_folder_path, request_url_folder_path):

   LIST_cluster_name = get_ALL_cluster_name (folder_path=parent_folder_path, cluster_name=cluster_name)
   LIST_cluster_node_ip =  get_LIST_TFM_cluster_node_ip_file (parent_folder_path, cluster_name=cluster_name, node_ip_folder_path)
   LIST_task_request_url = create_LIST_task_request_url (parent_folder_path, cluster_name=cluster_anem, request_url_folder_path)
   
   LIST_doc_value = []
   LOLIST_doc_value = []
   
   
   for cluster_name in LIST_cluster_name:
   
      LIST_cluster_node_ip =  get_LIST_TFM_cluster_node_ip_file (parent_folder_path=parent_folder_path, cluster_name=cluster_name, node_ip_folder_path)
      LIST_task_request_url = create_LIST_task_request_url (parent_folder_path, cluster_name, request_url_folder_path=request_url_folder_path)
   
      LIST_doc_value.insert(0,cluster_name=cluster_name) #doc title
      LIST_doc_value.insert (1, LIST_cluster_node_ip ) #LIST cluster node ip 
      LIST_doc_value.insert(2, datetime.now()) #created date time
      LIST_doc_value.insert(3, TFM_name=cluster_name) #TFM name 
      LIST_doc_value.insert(4, LIST_task_request_url) #TFM name 
      
      print (LIST_doc_value)
      
      LOLIST_doc_value.append(LIST_doc_value)
      LIST_doc_value.clear() #must clear to avoid duplicate values     
      #print (LOLIST_doc_value)
      
      #print (LOLIST_doc_value)
      
   return LOLIST_doc_value

'''




# create 1 doc per TFM cluster. 1 task request url list per round 
def create_DOCS_task_request_schedule (folder_path, conn_str, db_name, coll_name, start_date, end_date, doc_data):

   LIST_collection = create_colls_TRS (start_date, end_date, conn_str)
   LIST_doc_data = create_LIST_cluster_doc_data (parent_folder_path, cluster_name, node_ip_folder_path, request_url_folder_path)
   
        
   for coll in LIST_collection:   
      
      for doc_data in LIST_doc_data:
         
         #check doc title before creating new doc data. 
         if doc_data['doc title'] in doc_data['doc title']:
         
            create_ONE_document (conn_str=conn_str, db_name=db_name, coll_name=coll, doc_data=doc_data)
            
         else:
         
            pass
  


''' 
doc_data = {"doc title":doc_title,
            "LIST cluster node ip": LIST_cluster_node_ip,
            "created date time":created_date_time,
            "last updated": last_updated,
            "description": description,
            
            "TFM name 1": TFM_name_1,
            "start date time": start_date_time,
            "end_date_time": end_date_time,
            "LIST url 1":LIST_url, #["#0 Used = 0 #1 url = http:/www.",]
            "LIST url 2":LIST_url, #["#0 Used = 0 #1 url = http:/www.", ]
            
             }   
'''   


######################################################################################3
##### Start & post task request urls 

def get_collections_ALL (conn_str, db_name):
   
   LIST_coll = get_ALL_collection_in_db (conn_str, db_name)
   
   return LIST_coll
   
   

def get_collections_of_TODAY ():

   dt_NOW = get_date_time_now (dt_format="3")
   
   dt_day = remove_all_after_text (after_text='#0', text_main=dt_NOW)
   dt_month = remove_all_before_and_after_texts (before_text='#0', after_text='#1', text_main=dt_NOW)   
   dt_time =  remove_all_before_text (before_text='#2', text_main=dt_NOW)
   
   LIST_all_coll = get_collections_ALL (conn_str, db_name)
   
   
   LIST_coll_today = []
   
   for coll in LIST_all_coll:
   
      coll_day = ''
      coll_month = ''
   
      if dt_day in coll_day and dt_month in coll_month:
      
         LIST_coll_today.append (coll)
         
      else:
      
         pass
         
   return LIST_coll_today 
   
   
   
   
def get_docs_ALL (conn_str, db_name, coll_name):
   
   LIST_doc = get_ALL_docs_in_collection (conn_str, db_name, coll_name)
   
   return LIST_doc
   
   
   
# Task start date time is now or passed start date time, but not started  
def get_docs_start_dt_NOW (conn_str, db_name, coll_name):
   
   LIST_all_doc = get_docs_ALL (conn_str, db_name, coll_name)   
   LIST_doc_start_dt_NOW = []
   
   dt_NOW = get_date_time_now (dt_format="3")     
   dt_day = remove_all_after_text (after_text='#0', text_main=dt_NOW)
   dt_month = remove_all_before_and_after_texts (before_text='#0', after_text='#1', text_main=dt_NOW)   
   dt_time =  remove_all_before_text (before_text='#2', text_main=dt_NOW)
   dt_hour = '' 
     
   doc_key_1 = "start date time"
   doc_key_hour = ''
   
   for doc in LIST_all_doc:
   
      if dt_hour in doc[doc_key_1]:
      
         LIST_doc_start_dt_NOW.append (doc)       
         
      else:
      
         pass
   
   return LIST_doc_start_dt_NOW 

   
   
# get all lists of a doc (or TFM cluster doc)     
def get_ALL_request_url_lists ():

   LIST_doc_start_dt_now = get_docs_start_dt_NOW (conn_str, db_name, coll_name)

      
    
#get request url not used of each TFM doc   
def get_request_urls_NOT_USED ():

   LIST_url_not_used = []
   
   pass
   
   
   
   
   
   
def post_request_urls_NOT_USED ():
   pass