
import sys, os
from plg_Regex import * 
from a2_test_CORE_TASK import * 



#####################################################
##### remove html tags to read it #########
#####################################################
LOG_tfm_task_request = sys.argv[1]
TFM_task_action = sys.argv[2]

str_LOG_tfm_task_request = LOG_tfm_task_request.replace('<br>', '').replace("</br>", '')
str_TFM_task_action = TFM_task_action.replace('<br>', '').replace("</br>", '')



def LOG_task_request ():

   #str_val =  extract_from_TFM_task_action ()[1]
   #print ("<br>" + str(str_val) + "</br>")


   #only 1 request url can run at a time, the url must not be in progress, completed or not complete within allowed duration 
   if 'one_unique' in str_LOG_tfm_task_request:
   
      check_LOG_1 ()
      TFM_task_action ()#must call this inside the LOG_task_request function, not outside it
      
   else:
   
      print ("<br> NOT one_unique </br>", flush=True)
      TFM_task_action ()#must call this inside the LOG_task_request function, not outside it
   
   
   #only 1 same request url without status = 'in progress', 'completed', 'Not completed withitn allowed duration' can run at a time, but other different request urls can run at the same time
   if 'many_unique' in LOG_tfm_task_request:
   
      pass
   
   
   #many request urls can run at the same time regardless of their statuses 
   if 'many' in LOG_tfm_task_request:
   
      pass
   


def TFM_task_action ():

   core_task_func = remove_all_after_text (after_text='#1', text_main=str_TFM_task_action).strip()
   conn_str = remove_all_before_and_after_texts (before_text='=', after_text='#2', text_main=str_TFM_task_action)
   db_name = remove_all_before_text (before_text='db_name=', text_main=str_TFM_task_action)
  
   
   if 'func_1' == core_task_func:

      check_LOG_2 (msg=db_name)
      
      
   else:
   
      print ("<br> NOT FOUND --> " + msg + "</br>")
      

   
LOG_task_request ()

 


