

from a0_items import * 
from plg_Sqlite import * 

import socket


#send date time of a task action back to TFM_master 

#TFM task name = Log database name
#TFM task action = task action to be logged

def get_DB_LOG_node_IP ():

   #read from DB_LOG_nodes.csv to get the IP of the LOG db (most likely TFM_master's ip)
   with open ('../data/raw/a0_LOG_db_nodes.csv') as f:
   
      CSV_rows = csv.DictReader(f)
      
      for row in CSV_rows: 
      
         print (row['LOG_db_node_ip'])
      
   
#get_DB_LOG_node_IP ()


   

# LOG database folder should be the node's ip
def get_DB_LOG_folder ():

   hostname=socket.gethostname()   
   IPAddr=socket.gethostbyname(hostname)   
   #print("Your Computer Name is:"+hostname)   
   #print("Your Computer IP Address is:"+IPAddr) 
   
   LOG_db_folder = 'LOG_' + IPAddr.replace('.', '_')
   
   return LOG_db_folder

#get_DB_LOG_folder()


#print (get_DB_LOG_folder())




# save log result to LOCAL data/cooked/ log database
def DB_LOG_to_local (TFM_name, TFM_task, TFM_task_action, update_count):

   # datetime object containing current date and time
   LOG_date_time = datetime.now()
   
   # insert into sqlite log db in data/cooked/DB_log.db - TFM_name
   insert_data (sqlite_folder, sqlite_file, table_name, data)
   
   #After insert, update the columns 
   update_data (sqlite_folder, sqlite_file, table_name, update_column, ref_column )




# save log result to a REMOTE data/cooked log database
#Log update count could be 1, 2, 3 or 4
def DB_LOG_to_remote (TFM_name, TFM_task, TFM_task_action, update_count ): #pass in TFM task action name to find the TFM task action in the task LOG database

   LOG_node_ip = get_DB_LOG_node_IP ()

   LOG_db_folder = get_DB_LOG_folder ()
   
   # datetime object containing current date and time
   LOG_date_time = datetime.now()
 
   print("now = ", LOG_now, flush=True)

   request.get('http://' + LOG_node_ip + '/' + LOG_DB_folder + 'TFM_name =' + TFM_name + '&TFM_task_action= ' + TFM_task_action  + '&LOG_task=DB_LOG_update_' + update_count + '&Progress_item=' + LOG_date_time)


#DB_LOG_to_remote (TFM_name = "TFM_email", TFM_task="send emails", TFM_task_action ="someaction", LOG_update_count = "1" )





