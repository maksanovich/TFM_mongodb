

from a0_items import * 
from plg_Date_time import * 
import pymongo 
from pymongo import MongoClient
from pprint import pprint
import bson
from plg_DB_MongoDB_2 import * 



def get_LIST_date (start_date, end_date):

   LIST_date = get_dt_every_day(start_date=start_date, end_date=end_date)[0]

   print (LIST_date)
   return LIST_date
   
#get_LIST_date (start_date=date(2024, 1, 1), end_date= date(2024, 12, 31))



########################################################################################################
#### MASTER task request log 

def create_DB_MASTER_log_request (conn_str):
 
   create_DB(conn_str =conn_str, db_name = 'LOG_master_task_request',  coll_name='test_1')



# date per collection    
def create_colls_master_log (start_date, end_date, conn_str):

   LIST_date = get_LIST_date (start_date=start_date, end_date=end_date)
   
   for date in LIST_date:
   
      create_collection (conn_str=conn_str, db_name="LOG_master_task_request", coll_name='L_MASTER_' + date)
       
#create_colls_master_log (start_date=date(2024, 1, 1),, end_date= date(2024, 12, 31), conn_str="mongodb://localhost:27017/") 



# 1 server ip per doc 
def create_servers_doc ():

   pass





# 1 server doc can have a list of TFM. Each TFM can have a list of task request urls 
def create_LIST_tfm ():

   pass




def create_LIST_tfm_task_request ():

   pass




def update_LIST_tfm_task_request ():

   pass






########################################################################################################
#### TFM task request log - only 1 TFM task request log per server 

# create a log request DB for a TFM
def create_DB_TFM_log_request (conn_str ):

     create_DB(conn_str =conn_str, db_name = 'LOG_tfm_task_request',  coll_name='test_1')
   


# 1 calender date per collection    
def create_colls_tfm_log (start_date, end_date, conn_str):

   LIST_date = get_LIST_date (start_date=start_date, end_date=end_date)
   
   for date in LIST_date:
   
      create_collection (conn_str=conn_str, db_name="LOG_tfm_task_request", coll_name='L_TFM' + date)
       
#create_colls_tfm_log (start_date=date(2024, 1, 1),, end_date= date(2024, 12, 31), conn_str="mongodb://localhost:27017/") 


   
# 1 doc per log    
def create_log_DOC ():

   pass   
   
   
   
    

def DB_get_ALL_log_request ():

   pass
   
   
   
   
def DOC_get_log_request_by_status ():


   pass




def DOC_insert_log_request ():

   pass
   # get server date time now
   # use date time to find the correct folder & sqlite file
   # check rows before insert 
   # insert data into the correct sqlite file 
   
   
   
# update log task request status (completed, in progress, not completed within allowed duration)   
def DOC_update_log_request ():

   pass
   
   
   
   
def DOC_delete_log_request ():

   pass   
   
   
   
   
def check_task_status_before_run_task (task_name, conn_str, log_db_name, log_coll):

   LIST_log_doc = get_log_DOCS (conn_str, log_db_name, log_coll)
   
   task_name = task_name
   doc_key_1 = 'task name'
   doc_key_2 = 'task status'
      
   for doc in LIST_all_doc:
          
      doc_task_name = doc[doc_key_1]
      doc_task_status = doc[doc_key_2]
   
      if (task_name in doc_task_name and 'Completed' in doc_task_status 
      and 'In progress' in doc_task_status 
      and 'Not completed within allowed task duration'  in doc_task_status):
         
         print ("Task NOT run because its completed, in progress, or not completed within allowed task duration")
      
      else:
   
        print ("Start the task") 

        #start the task
        #Log task on completion         
   
   
   
 
####################################################################################
###### TFM task item log - 1 task item log for each TFM 


# create a log request DB for a TFM
def create_DB_TFM_log_task_item (conn_str ):

     create_DB(conn_str =conn_str, db_name = 'LOG_tfm_task_item',  coll_name='test_1')   
     
     
     
# 1 calender date per collection    
def create_colls_tfm_task_item (start_date, end_date, conn_str):

   LIST_date = get_LIST_date (start_date=start_date, end_date=end_date)
   
   for date in LIST_date:
   
      create_collection (conn_str=conn_str, db_name="LOG_tfm_task_item", coll_name='LTI_' + date) # LTI stands for Log task item 
       
#create_colls_tfm_item (start_date=date(2024, 1, 1),, end_date= date(2024, 12, 31), conn_str="mongodb://localhost:27017/")      




# 1 log per tfm item doc, eg 1 email sent per item doc 
def create_docs_tfm_task_item ():

   pass