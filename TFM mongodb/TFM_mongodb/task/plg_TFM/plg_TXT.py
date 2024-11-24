

from a0_items import *



def read_TXT_file (path_TXT):

   with open(path_TXT, 'r' ,  encoding='UTF-8') as file:
   
      LIST_line = file.readlines()
           
   return LIST_line
   
   
# print(read_TXT_file (path_TXT='shaneTXT.txt')  ) 



def create_TXT_file (path_TXT):

   if os.exists(path_TXT):
   
      print (path_TXT + ' alraedy exists')
      
   else:
  
      with open(path_TXT, 'w') as f: 
         pass #create an empty text file 
     
      print (path_TXT + ' NOT exists, is created!')


#create_TXT_file (path_TXT='shaneHELLO.txt')




# write 1 line only 
def write_to_TXT_file_1 (path_TXT, line_to_write):

   with open(path_TXT, "a+") as file:
      
      #write 1 line only
      file.write(line_to_write)




#write multiple lines at once 
def write_to_TXT_file_2 (path_TXT, LIST_to_write):

   with open(path_TXT, "a+") as file:

      #Use writelines() to write the list of strings to the file
      file.writelines(LIST_to_write)

'''
# Step 2: Create a list of strings, where each string represents a line
LIST_lines = [
     "This is the first line \n",
     "This is the second line \n",
     "This is the third line \n"
    ]
    
write_to_TXT_file_2 (path_TXT='shaneTXT.txt', lines_to_write = LIST_lines)
'''


def delete_TXT_file (path_TXT):

   if os.path.exists(path_TXT):
      os.remove(path_TXT)
      
      
   else:
     print(path_TXT + " NOT exists")
   
   
#delete_TXT_file (path_TXT)   
   





