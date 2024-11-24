

from a0_items import * 


import psutil 

###################################################################################################
### plugins - Check if a Python process is already running 
####################################################################################################


# https://www.tutorialspoint.com/how-to-get-the-list-of-running-processes-using-python
def get_ALL_process ():

   LIST_process = []

   processes = psutil.process_iter()
   
   for process in processes:
   
      #print(f"Process ID: {process.pid}, Name: {process.name()}")
      
      LIST_process.append(process)
          
   COUNT_process = len(LIST_process)
    
   return LIST_process, COUNT_process


#print (get_ALL_process ()[0])



def get_Process_by_name (process_name):

   LIST_found_process = []

   processes = psutil.process_iter()
   
   for process in processes:
   
      if process_name in process.name().lower():
      
         print ('Process found --> ' + str(process))
         
         LIST_found_process.append(process)
         
      else:
         
         pass
         #print ('Process NOT found --> ' + str(process))
         
         
   return LIST_found_process
         
         
get_Process_by_name (process_name='python')         





# https://superfastpython.com/processpoolexecutor-task-status/

