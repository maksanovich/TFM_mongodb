

from a0_items import * 
from plg_Files import * 
from plg_Folders import * 


##### Must download & install MongoDB software from --> https://www.mongodb.com/try/download/community #######
# https://www.w3schools.com/python/python_mongodb_getstarted.asp


##### plg_TFM_do_task_1 - MongoDB to MongoDB #########################################

### The following code is to be executed on the TFM server side, not from TFM master #######
############################################################################################
##### RAW, COOKED data lists #######


# get a list of raw COLLECTIONS from a MongoDB database 
def get_LIST_raw_ALL (raw_LOLISTS):

   LIST_raw_ALL = raw_LOLIST 
   
   return LIST_raw_ALL 
   
 
#get_LIST_raw_ALL (raw_LOLIST)
 
  
  
def get_LIST_cooked_ALL (cooked_LOLISTS):

   LIST_cooked_ALL = cooked_LOLISTS
   
   return LIST_cooked_ALL 
   


# get selected lists by index
def get_LIST_raw_SELECTED (raw_LOLISTS, raw_start_list_index, raw_end_list_index):

   LIST_raw_ALL = get_LIST_raw_ALL (raw_LOLISTS)

   LIST_raw_selected = []
   
   for raw_list in LIST_raw_ALL(raw_LOLISTS):
   
      LIST_raw_selected.append(raw_list)
           
   return LIST_raw_selected
   
   
# get selected collections by index
def get_LIST_cooked_SELECTED (cooked_LOLISTS, cooked_start_list_index, cooked_end_list_index):

   LIST_cooked_ALL = get_LIST_cooked_ALL (cooked_LOLISTS=cooked_LOLISTS)

   LIST_cooked_selected = []
   
   for cooked_list in LIST_cooked_ALL(cooked_start_list_index=cooked_start_list_index, cooked_end_list_index= cooked_end_list_index):
   
      LIST_cooked_selected.append(cooked_list)
           
   return LIST_cooked_selected



############################################################
##### RAW, COOKED, TO_BE Data items #######

def get_raw_DATA_ITEMS (raw_list):
  
   LIST_raw_data_item = raw_list
   
   return LIST_raw_data_item
   
 
 
#### Select data with log status = Completed, In progress, Not completed within allowed task duration
def get_cooked_DATA_ITEMS (cooked_list):

   LIST_cooked_data_item = cooked_list
   
   return LIST_cooked_data_item


#get_cooked_DATA_ITEMS (cooked_list = '')



def get_TO_BE_DATA_ITEMS (raw_list, cooked_list):

   LIST_raw = get_raw_DATA_ITEMS (raw_list = raw_list)
   LIST_cooked = get_cooked_DATA_ITEMS (cooked_list = cooked_list)
   
   LIST_to_be = []
       
   for raw in LIST_raw:
    
      if raw in LIST_cooked:
       
         #print (raw + ' in cooked')
         pass
          
      else:
          
         #print (raw + ' NOT in cooked')
         LIST_to_be.append(raw)
   
   #print ('LIST to be => ' + str(LIST_test_to_be))   
   return LIST_to_be 
   
   
   
# split data item to get data chunk   
def split_to_be_DATA_ITEMS (raw_list, cooked_list, start_index, items_per_list):
 
   LIST_to_be_DATA_ITEM = get_TO_BE_DATA_ITEMS (raw_list = raw_list, cooked_list = cooked_list)
   
   return list_SPLIT_1 (LIST_to_split = LIST_to_be_DATA_ITEM, start_index = start_index, items_per_list = items_per_list)



'''
# do the task on 1 data item, eg send email, post comment   
## this method needs to be created from scratch to be used by CF_data_chunk (LIST_item)
def do_one_DATA_ITEM (data_item):

   print (data_item) 
'''   
   

#####################################################################
##### Selected TO_BE data lists with TO_BE data items 

def get_LIST_to_be_SELECTED_with_data_items (raw_LOLISTS, raw_start_list_index, raw_end_list_index, cooked_LOLISTS, cooked_start_list_index, cooked_end_list_index):

   LIST_raw_list_SELECTED =  get_LIST_raw_SELECTED (raw_LOLISTS=raw_LOLISTS, raw_start_list_index=raw_start_list_index, raw_end_list_index=raw_end_list_index)
   LIST_cooked_list_SELECTED = get_LIST_cooked_SELECTED (cooked_LOLISTS=cooked_LOLISTS, cooked_start_list_index=cooked_start_list_index, cooked_end_list_index=cooked_end_list_index)
   
   #TO_BE lists & data 
   LIST_to_be_list_data_SELECTED = []
   
   # get_TO_BE_DATA_ITEMS returns a list of TO_BE data 
   for raw_list, cooked_list zip(LIST_raw_list_SELECTED, LIST_cooked_list_SELECTED):

      LIST_to_be_list_data_SELECTED.append( raw_list + ' #_0 ' + get_TO_BE_DATA_ITEMS (raw_list = raw_LOLISTS + raw_list, cooked_list = cooked_LOLISTS + cooked_list) )

   return LIST_to_be_list_data_SELECTED


#get_LIST_to_be_SELECTED_with_data_items (raw_LOLISTS, raw_start_list_index, raw_end_file_index, cooked_LOLISTS, cooked_start_file_index, cooked_end_file_index)



#################################################################
###### Concurrent futures on data chunks ########################


# data list --> data items --> data chunks (or data item chunks) 

## do_task_DATA_ITEM --> CF_data_chunk (LIST_item) --> CF_all_data_chunk (start_list, end_list, raw_LOLISTS, cooked_LOLISTS, start_index, items_per_list)

def CF_data_chunk ( LIST_item):

   with concurrent.futures.ProcessPoolExecutor() as executor:
        
      executor.map(do_one_DATA_ITEM, LIST_item)
        
      t2 = time.perf_counter()
      print (f' finished in {t2} seconds')      




# Concurrent futures on TO_BE data chunks only
def CF_all_data_chunk (raw_list, raw_list, raw_start_list_index, raw_end_list_index, cooked_LOLISTS, cooked_list, cooked_Start_list_index, cooked_end_list_index, start_index, items_per_list, do_one_DATA_ITEM):
  
   # LIST TO_BE list & data
   LIST_to_be_list_data = get_LIST_to_be_SELECTED_with_data_items (raw_LOLISTS=raw_LOLISTS, raw_start_list_index=raw_start_list_index, raw_end_list_index=raw_end_list_index, cooked_LOLISTS=cooked_LOLISTS, cooked_start_list_index=cooked_start_list_index, cooked_end_list_index=cooked_end_list_index)
   
   start_list_index = raw_start_list_index
   end_list_index = raw_end_list_index
   
  
   # Loop through EACH selected to_be data list 
   for data_list in LIST_to_be_list_data[start_list_index:end_list_index]:

      LIST_to_be_list_only = remove_all_after_text (after_text= ' #_0 ' , text_main = data_list)
      LIST_data_item_only = remove_all_before_text (before_text= ' #_0 ', text_main = data_list)
              
      for data_items in LIST_data_item_only:
      
         #LIST_data_item_chunk = split_LIST_data_item  (LIST_to_split=LIST_data_item_only, start_index=start_index, items_per_list=items_per_list)         
         LIST_data_itek_chunk = split_to_be_DATA_ITEMS (raw_list = raw_list, cooked_list = cooked_list, start_index=start_index, items_per_list=items_per_list)
      
         for data_item_chunk in LIST_data_item_chunk    
                  
            CF_data_chunk (do_one_DATA_ITEM = do_one_DATA_ITEM, LIST_item=data_item_chunk)  



#do_task_DATA_ITEM --> need write this function to be used by CF_data_chunk (LIST_item)

raw_LOLISTS = ''
raw_list = ''
raw_start_list_index = ''
raw_end_list_index = ''

cooked_LOLISTS = ''
cooked_list = ''
cooked_start_list_index = ''
cooked_end_list_index = ''

start_index = ''
items_per_list = ''

do_one_DATA_ITEM = ''# this is a function to complete 1 data item 
LIST_item = ''



#CF_all_data_chunk (raw_LOLISTS, raw_list, raw_start_list_index, raw_end_list_index, cooked_LOLISTS, cooked_list, cooked_Start_list_index, cooked_end_list_index, start_index, items_per_list)