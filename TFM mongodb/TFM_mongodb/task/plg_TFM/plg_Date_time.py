

from a0_items import *

from datetime import timedelta, date



def get_date_today ():

   date_today = date.today()
   
   return date_today
   


# https://www.programiz.com/python-programming/datetime/strftime     
def get_date_time_now (dt_format):
   
   # datetime object containing current date and time
   now = datetime.now()
 
 
   match dt_format:
   
      case "1":
         # dd-mm-YY H:M:S
         dt_string = now.strftime("%d-%m-%Y %H:%M:%S %p")  
         print("date and time =", dt_string)
         
         return dt_string
         
      case "2": 
         # dd_mm_YY_H_M_S
         dt_string = now.strftime("%d_%m_%Y_%H_%M_%S_%p")  
         print("date and time =", dt_string)
         
         return dt_string  

      case "3":
         # dd_mm_YY_H_M_S
         dt_string = now.strftime("%d_%b_%Y_%H_%M_%S_%p")  
         print("date and time =", dt_string)
         
         return dt_string        
         
     
get_date_time_now (dt_format='3')




#calculate ALL dates between two dates - https://www.tutorjoes.in/Python_example_programs/get_list_of_dates_between_two_dates_in_python
def get_date_range(start_date, end_date):

    LIST_date = []

    for n in range(int ((end_date - start_date).days)+1):
         
        date_value = start_date + timedelta(n)
        #print (date_value.strftime("%d_%b_%Y"))
        
        LIST_date.append (date_value.strftime("%d_%b_%Y"))
        
    return LIST_date
        
#get_date_range(start_date= date(2024, 1, 1), end_date= date(2024, 12, 31) )



import pandas as pd

#print (pd.date_range(start="2018-09-09",end="2019-02-02").to_pydatetime().tolist())



def get_24_hour ():

   LIST_hour = []
   
   for x in range (24):
   
      LIST_hour.append(x+1)
            
   return LIST_hour
  
  
#print (get_24_hour ())


LIST_30m_range = ['00', 29, 30, 59] #every 30m
LIST_60m_range = ['00', 59] #every 60m or 1 hour

def get_dt_every_30m (start_date, end_date):

   LIST_date = get_date_range (start_date, end_date)
   LIST_hour = get_24_hour ()
   
   LIST_dt_every_30m = []

   for date in LIST_date: 
   
      for hour in LIST_hour:
            
         dt_name_1 = ('FROM_' + date + '_' + str(hour) + '_' + str(LIST_30m_range[0]) + '_TO_' + str(hour) + '_' + str(LIST_30m_range[1])).replace('-', '_')
         dt_name_2 = ('FROM_' + date + '_' + str(hour) + '_' + str(LIST_30m_range[2]) + '_TO_' + str(hour) + '_' + str(LIST_30m_range[3])).replace('-', '_')
      
         LIST_dt_every_30m.append (dt_name_1 )
         LIST_dt_every_30m.append (dt_name_2 )
      
   
   return LIST_dt_every_30m
   

'''   
LIST_test = get_dt_every_30m (start_date= date(2024, 1, 1), end_date= date(2024, 12, 31))

for x in LIST_test:

   print (x)
'''


def get_dt_every_60m(start_date, end_date):

   LIST_dt_every_60m = []
   
   LIST_date = get_date_range (start_date, end_date)
   LIST_hour = get_24_hour ()
 
   for date in LIST_date: 
   
      for hour in LIST_hour:
            
         dt_name_1 = ('FROM_' + date + '_' + str(hour) + '_' + str(LIST_60m_range[0]) + '_TO_' + str(hour) + '_' + str(LIST_60m_range[1])).replace('-', '_')
      
         LIST_dt_every_60m.append (dt_name_1 )
       
   return LIST_dt_every_60m
   
''' 
LIST_test = get_dt_every_60m(start_date=date(2024, 1, 1), end_date= date(2024, 12, 31))
for x in LIST_test:

   print (x)
'''
 
   
def get_dt_every_day(start_date, end_date): 

   LIST_day = []
   
   LIST_date = get_date_range (start_date, end_date)

   for date in LIST_date: 
   
      dt_name_1 = ( 'FROM_TO_' + date ).replace('-', '_')
   
      LIST_day.append (dt_name_1)
       
   return LIST_day
   
   
'''
LIST_test = get_dt_every_day(start_date=date(2024, 1, 1), end_date= date(2024, 12, 31))
for x in LIST_test:

   print (x)
'''  
   