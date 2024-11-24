

from a0_items import * 
from plg_Folders import * 
from plg_DB_Sqlite import * 
from plg_Files import * 
from plg_Regex import * 
from plg_Date_time import * 


######################################################################################
########## DB sharding by date time ##################################################

### JAN - DEC
def DB_folder_months (folder_path):

   LIST_month = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
   
   for month in LIST_month:
   
      create_folder (folder_path)
   


def SQLITE_file_per_day (folder_path, num_of_files, year):

   for num in range(file_count = num_of_files):
   
      sqlite_create_file (sqlite_path = folder_path + year + '_' + num + '.db', sql='')


## SQLITE_file_per_number (folder_path, num_of_files=365, year = '2024')



def SQLITE_file_per_calender_day (folder_path, start_date, end_date):

   LIST_day_of_year = get_dt_every_day(start_date, end_date)[1]
   
   for day in LIST_day:
   
      sqlite_create_file (sqlite_path = folder_path + day + '.db', sql='')
   
   
    
def SQLITE_file_per_hour (folder_path, start_date, end_date):

   LIST_60m_of_year = get_dt_every_60m(start_date, end_date)
   
   for hour in LIST_60m_of_year:
   
      sqlite_create_file (sqlite_path = folder_path + hour + '.db', sql='')   
   
   
   
def SQLITE_file_per_30_min (folder_path, start_date, end_date):

   LIST_30m_of_year = get_dt_every_30m(start_date, end_date) 
   
   for min_30 in LIST_30m_of_year:
   
      sqlite_create_file (sqlite_path = folder_path + min_30 + '.db', sql='')  




####################################################################################
########## DB sharding by letter ###################################################

### a-z
def DB_folder_letters (folder_path):

   LIST_letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
   
   for letter in LIST_letter:
   
      create_folder (folder_path)



def SQLITE_file_per_letter ():

   LIST_letter_1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
   LIST_letter_2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
   
   for letter_1 in LIST_letter_1:
   
      for letter_2 in LIST_letter_2:
      
         print (letter_1 + letter_2)
         
         folder_name = folder_path.replace('', '')
         
         if letter_1 in folder_name:
         
            print (letter_1 + ' in ' + folder_name)
            sqlite_create_file (sqlite_path = folder_path + letter_1 + letter_2 + '.db', sql='') 
         
                        
         else:
         
            print (letter_1 + ' NOT in ' + folder_name)
            
                
#SQLITE_file_per_letter ()         
         



###################################################################################
########## DB sharding by name ####################################################

#from TXT or CSV
def get_names ():

   LIST_name = []
   
   if 'txt' in file_type:
   
      pass
     
   if 'csv' in file_type:
   
      pass
      
   else:
        
      return LIST_name



### eg country names 
def DB_folder_names (folder_path, option):


   if option == 1:
   
      print ("do NOT create folders by name")
      
   if option == 2:
   
      #create names folders
      LIST_name = 'get name from txt' 

      for name in LIST_name:
   
         create_folder (folder_path)



def SQLITE_file_per_name ():

   LIST_name = 'read from a TXT file or CSV file' 
   
   for name in LIST_name:
   
      sqlite_create_file (sqlite_path = folder_path + min_30 + '.db', sql='') 




################################################################################################
####### get data lists after sharding DB files #################################################
  
# List item splitter --> for each line, eg, >>> or <<<   

def get_DB_folder_list (folder_path):

   LIST_db_folder = get_ALL_in_folder (folder_path)
   
   return LIST_db_folder 
   

   
def get_DB_file_list (folder_path):

   LIST_db_file = get_ALL_in_folder (folder_path)

   return LIST_db_file 
   
   
   
def get_DB_data_list (folder_path, DB_file_path):

   LIST_data = sqlite_select_ALL_data (sqlite_path, sql)

   return LIST_data
   


# Unique item identifier -->  for each list, eg, #_a0, #_a1  
def get_list_from_DB_data (sqlite_path, sql, before_symbol, after_symbol):

   LIST_data = sqlite_select_ALL_data (sqlite_path, sql)

   LIST_parent_data = remove_all_before_and_after_texts (before_text = before_symbol, after_text = after_symbol, text_main= str(LIST_data))
   
   return LIST_parent_data
  
'''  
sqlite_path_1=''
sql_1 = '' 
get_list_from_DB_data (sqlite_path=sqlite_path_1, sql=sql_1, before_symbol='#_a0', after_symbol='#_a1') 
'''

####################################################################################################################
######## LIST to string, String to list ################################################################################


def create_list_from_string (string, symbol):

   LIST = list(string.split(symbol))
   
   return LIST  

'''
string_1 = "hello my name >>> not sure >>> man"
LIST_new = create_list_from_string (string = string_1, symbol='>>>')
print (LIST_new)
''' 


def create_string_from_list (LIST_item ):

   String_item = ''.join(str(x) for x in LIST_item)
   
   return String_item
   
'''   
LIST_new = create_list_from_string (string = string_1, symbol='>>>')   
Str_items = create_string_from_list (LIST_item = LIST_new )  
print (Str_items)
'''


############################################################################################# 
##### Find DB files by date time, by name, by letter 


# Log request from TFM_master       
def find_LOG_folder_by_month():

   # get server date time now
   Date_time = get_date_time_now (dt_format='3')
   
   # Extract month from date time to find the parent folder
   Parent_folder_name = remove_all_before_and_after_texts (before_text='#0', after_text='#1', text_main=Date_time)
   
   return Parent_folder_name 



def find_LOG_file_by_date():

   # get server date time now
   Date_time = get_date_time_now (dt_format='3')

   # Extract month and day from date time to find the LOG file 
   LOG_file_name = remove_all_after_text (after_text='#1', text_main=Date_time).replace ('#0', '')

 
   return LOG_file_name  




def find_DB_folder_by_letter ():

   pass
   
   
   
 
def find_DB_file_by_letter ():

   pass

 
   
   
def find_DB_file_by_name ():

   pass






##################################################################################################################
##### check row count & file size before insert data #############################################################
   
# DB row must be equal to or less than a number
# DB file size must be equal to or less than a number  

def get_LAST_db_file (folder_path):

   LIST_db_file = get_DB_file_list (folder_path)
   
   last_INDEX_of_list = LIST_db_file[-1:]

   last_ITEM_of_list = LIST_db_file[-1]
   
   
   return last_INDEX_of_list, last_ITEM_of_list 



def get_DB_row_count (db_file, DB_table):

    LIST_all_row = sqlite_select_ALL_data (sqlite_path, sql)
    
    row_count = len(LIST_all_row)
    
    return row_count
   
   
   
def get_DB_file_size (db_file):

   DB_file_size = get_file_size_2 (file_path_2)
   
   return DB_file_size
   
   

 
 

def DB_check_ROWS_before_insert (max_rows):

   # get the last db file in the subfolder
   last_db_file = get_LAST_db_file (folder_path)
   
   last_db_file_rows = get_DB_row_count ()

   if rows >= max_rows:
   
      print ("max rows is equal to or greater than " + max_rows + " a new database file is created")
      
      #create new db file AFTER the last db file 
      sqlite_create_file (sqlite_path, sql)
           
   else:
   
      print ("max rows is less than " + max_rows + " data is inserted")
      
      #insert db data
      sqlite_insert_data_multi_columns (sqlite_path, sql, data)
    
 
 
    
def DB_check_SIZE_before_insert (DB_list_folder, max_size):
   
   # get the last db file in the subfolder 
   last_db_file = get_LAST_db_file (folder_path = DB_list_folder)
   
   last_db_file_size = get_DB_file_size ()
   

   if file_size >= max_size:
   
      print ("max size is equal to or greater than " + max_size + " a new database file is created")
      
      #create new db file AFTER the last db file 
      sqlite_create_file (sqlite_path, sql)
      
   else:
   
      print ("max size is less than " + max_size + " data is inserted")
      
      #insert db data
      sqlite_insert_data_multi_columns (sqlite_path, sql, data)
      
      


     
      