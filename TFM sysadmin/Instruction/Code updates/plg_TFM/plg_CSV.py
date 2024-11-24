

from a0_items import *
import pandas


########################################################################################################################
### Read CSV
########################################################################################################################

#read csv file by list index
def CSV_reader (path_CSV):

   LIST_of_list = []

   with open(path_CSV, 'r', encoding="ascii", errors="ignore") as file:
      
      csvreader = csv.reader(file,delimiter=':')
     
      for row in csvreader:
         
         LIST_of_list.append(row)
         
   return LIST_of_list


''''
#each row is a list of data
for x in CSV_reader (path_CSV='../../data/raw/RAW_country_language/cities.csv'): 

   print (x)
'''

'''
for x in CSV_reader (path_CSV='../../data/raw/RAW_country_language/cities.csv'): 

   for y in x:
   
      y_list = y.split(',') #must convert string back to list first
      
      print (y_list[1])
''' 


# create & read csv file by column name 
def CSV_dict_reader ( path_CSV):

   LIST_data = []

   with open(path_CSV, 'r', encoding="ascii", errors="ignore") as file:
      
      csvreader = csv.DictReader(file)
     
      for row in csvreader:
         
         LIST_data.append(row)
         
   return LIST_data
   
   
'''   
for x in CSV_dict_reader (path_CSV='../../data/raw/RAW_country_language/country_only.csv'): 

   print (x['Name'])   
'''
 

########################################################################################################################
### create CSV header
########################################################################################################################

#https://adamtheautomator.com/read-csv-in-python/
def CSV_create_header_1 (path_CSV, LIST_header):

   if os.path.exists (path_CSV):
   
      print (path_CSV + ' Exists')
      
   else:
   
      print (path_CSV + ' NOT exists, is created')

      with open(path_CSV, 'w', newline='') as outcsv:
   
         writer = csv.writer(outcsv)
      
         writer.writerow(LIST_header)

'''
header_LIST = ["Date", "temperature 1", "Temperature 2"]
CSV_create_header_1 (path_CSV='test_write_header.csv', LIST_header=header_LIST)
'''


def CSV_create_header_2 (path_CSV, LIST_header):

   # read contents of csv file 
   file = pandas.read_csv(path_CSV) 
   print("\n Original file:") 
   print(file) 
  
   # converting data frame to csv 
   file.to_csv(path_CSV, header=LIST_header, index=False) 
  
   # display modified csv file 
   file2 = pandas.read_csv(path_CSV) 
   print('\n Modified file:') 
   print(file2)


#headerList = ['name', 'number', 'skills'] 
#CSV_create_header_2 (path_CSV='test_panda.csv', LIST_header=headerList)


########################################################################################################################
### create CSV data
########################################################################################################################

#https://adamtheautomator.com/read-csv-in-python/
def CSV_create_data_1 (path_CSV, LIST_data):

   if os.path.exists (path_CSV):
   
      print (path_CSV + ' Exists')
      
   else:
   
      print (path_CSV + ' NOT exists, is created')

      with open(path_CSV, 'a', newline='') as outcsv: #use 'a' to allow append of data by looping
   
         writer = csv.writer(outcsv)
     
         writer.writerow(LIST_data)

'''
data_LIST = ["data1", "data2", "data3"]
CSV_create_header_1 (path_CSV='test_write_header.csv', LIST_header=header_LIST, LIST_data=data_LIST)
'''



#List should be created separated to loop through this function 
def CSV_update_data_2 (path_CSV, col_index, col_name, col_value):
 
   # reading the csv file
   df = pandas.read_csv(path_CSV)
  
   # updating the column value/data
   # col_index starts from 0, its the index of the CSV row and must be an integrer 
   df.loc[col_index, col_name.strip()] = str(col_value)
  
   # writing into the file
   df.to_csv(path_CSV, index=False)
  
   print(df) 
   
   
#csv_update_data_2 (path_CSV='test_panda.csv', col_index=2, col_name='Col_2', col_value='brad')   



def CSV_update_by_replace (path_CSV, col_name, col_value, replace_with_value):

   # reading the csv file 
   df = pandas.read_csv(path_CSV) 
  
   # updating the column value/data 
   df[col_name] = df[col_name].replace({col_value : replace_with_value}) 
  
   # writing into the file 
   df.to_csv(path_CSV, index=False) 
  
   print(df) 
   
   
#csv_update_by_replace (path_CSV='test_panda.csv', col_name='', col_value='', replace_with_value='')   
