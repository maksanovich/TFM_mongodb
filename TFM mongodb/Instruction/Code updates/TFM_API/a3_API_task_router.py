
from a0_items import * 
from a2_API_update_logs import *


#https://www.codeproject.com/Questions/5339935/How-do-I-pass-multiple-variables-from-PHP-to-Pytho
TFM_task = sys.argv[1] #name of TFM_task = LOG database name  
TFM_task_action = sys.argv[2] #name of TFM_task_action => trans_start_date, trans_end_date


TFM_task = 'DB_LOG_update_1' #just an example


#get trans_start_date and trans_end_date from TFM_task_action 
def EXTRACT_task_action (TFM_task_action):

  trans_start_date = re.sub(r'^.*?FROM', '', TFM_task_action.partition("TO")[0]).strip()
  trans_end_date = re.sub(r'^.*?TO', '', TFM_task_action).strip()
 
  return trans_start_date, trans_end_date 

#print (EXTRACT_task_action (TFM_task_action)[0])
#print (EXTRACT_task_action (TFM_task_action)[1])



Database folder = 'LOG_' + node_ip.replace('.', '_')
Database name = 'TASK_' + TFM_task full name + '.db'
TFM_task_action = TFM_task_action 

LOG_task => function that logs the task
LOG_item => date time now



def select_DB_LOG_task():

   match LOG_task:

   case 'DB_LOG_update_0':
   
      print ("FIRST UPDATE")
      DB_LOG_update_0 (LOG_DB, TFM_task_action)
      
      
   case 'DB_LOG_update_1':
   
      print ("SECOND UPDATE")
      DB_LOG_update_1 (LOG_DB, TFM_task_action)
      
      
   case 'DB_LOG_update_2':
   
      print ("THIRD UPDATE")
      DB_LOG_update_2 (LOG_DB, LOG_task_action)
   
   
   case 'DB_LOG_update_3':
   
      print ('LAST UPDATE')
      DB_LOG_update_3 (LOG_DB, TFM_task_action)
   
 


if __name__ == "__main__":
   select_DB_LOG_task()