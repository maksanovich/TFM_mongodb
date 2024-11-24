

from a0_items import * 
import schedule

import time

from datetime import date


#https://plainenglish.io/blog/5-ways-to-schedule-jobs-in-python-99de8a80f28e

def task_1():
   
   print ("starting")
   
   for x in range (5):
   
      now = datetime.now()
   
      print (now, flush=True)
      time.sleep(3)
     
      
   
   


def run_task_LOOP (time_pause, run_count):

   for x in range (run_count):
   
      task ()
         
      time.sleep(time_pause)
      
             
#run_task_LOOP (time_pause = 5, run_count = 5)   



# https://schedule.readthedocs.io/en/stable/
def run_task_EVERY (run_every, time_value, end_datetime, task):

   match run_every:
   
      case "s":
         print ("run task every " + str(time_value) + " SECONDS")

         task_schedule=schedule.every(time_value).seconds.until(end_datetime).do(task)
   
         while True:
            schedule.run_pending()
            time.sleep(1)  

      case "m":
         print ("run task every " + str(time_value) + " MINUTES")
      
         task_schedule=schedule.every(time_value).minutes.until(end_datetime).do(task)
   
         while True:
            schedule.run_pending()
            time.sleep(1)

      case "h":
         print ("run task every " + str(time_value) + " HOURS")
      
         task_schedule=schedule.every(time_value).hours.until(end_datetime).do(task)
   
         while True:
            schedule.run_pending()
            time.sleep(1)  
                     
      case "d":
         print ("run task every " + str(time_value) + " DAYS")
      
         task_schedule=schedule.every(time_value).days.until(end_datetime).do(task)
   
         while True:
            schedule.run_pending()
            time.sleep(1)  

      case "w":
         print ("run task every " + str(time_value) + " WEEKS")
      
         task_schedule=schedule.every(time_value).weeks.until(end_datetime).do(task)
   
         while True:
            schedule.run_pending()
            time.sleep(1)  
                                             
            
#run_task_EVERY (run_every= 's', time_value= 3, end_datetime="2024-10-10 15:08", task = task_1)




def run_task_EVERY_WEEKDAY_AT (run_every, time_value, task):


   match run_every:
   
      case "mon":
         print ("run task every MONDAY")

         schedule.every().monday.at(time_value).do(task)
   
         while True:
            schedule.run_pending()
            time.sleep(1)  

      case "tues":
         print ("run task every TUESDAY")
      
         schedule.every().tuesday.at(time_value).do(task)
   
         while True:
            schedule.run_pending()
            time.sleep(1)

      case "wedn":
         print ("run task every WEDNESDAY")
      
         schedule.every().wednesday.at(time_value).do(task)
   
         while True:
            schedule.run_pending()
            time.sleep(1)  
                     
      case "thurs":
         print ("run task every THURSDAY")
      
         schedule.every().thursday.at(time_value).do(task)
   
         while True:
            schedule.run_pending()
            time.sleep(1)  

      case "fri":
         print ("run task every FRIDAY")
      
         schedule.every().friday.at(time_value).do(task)
   
         while True:
            schedule.run_pending()
            time.sleep(1)  
            
            
      case "sat":
         print ("run task every sATURDAY")
      
         schedule.every().saturday.at(time_value).do(task)
   
         while True:
            schedule.run_pending()
            time.sleep(1)              
                     
      case "sun":
         print ("run task every SUNDAY")
      
         schedule.every().sunday.at(time_value).do(task)
   
         while True:
            schedule.run_pending()
            time.sleep(1)              
            
            
#run_task_EVERY_WEEKDAY_AT (run_every="mon", time_value="13:30", task=task_1)            




