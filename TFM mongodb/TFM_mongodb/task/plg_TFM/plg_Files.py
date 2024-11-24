
from a0_items import * 



# https://pynative.com/python-rename-file/

# change file name 
def rename_file (old_name, new_name):

   if os.path.isfile(new_name):
   
      print("The file already exists")
      
   else:
   
      # Rename the file
      os.rename(old_name, new_name)



def move_file (src_path, dst_path):

   # absolute path
   shutil.move(src_path, dst_path)



def move_all_files_in_folder ():

   pass



##########################################################################################################
#### copy file 
###########################################################################################################

import os
import shutil
from shutil import SameFileError

# Copy files 

def copy_file (dst_folder_path, src_file_path, dst_file_path):

   try:
      # copy file
      shutil.copyfile(src_file_path, dst_file_path)
      # destination folder after copying
      print("Destination after copying", os.listdir(dst_folder_path))
      
   except SameFileError:
   
      print("We are trying to copy the same File")
      
   except IsADirectoryError:
   
      print("The destination is a directory")
   
   

def copy_every_file_in_folder (src_folder_path, dst_folder_path):

   if os.path.exists(src_folder_path):
   
      shutil.copytree(src_folder_path, dst_folder_path)




##########################################################################################################
#### get file size
###########################################################################################################

# https://www.geeksforgeeks.org/how-to-get-file-size-in-python/

def get_file_size_1 (file_path_1):

   file_stats = os.stat(file_path_1)

   print(file_stats)
   print(f'File Size in Bytes is {file_stats.st_size}')
   print(f'File Size in MegaBytes is {file_stats.st_size / (1024 * 1024)}')

   return file_stats
   
   

def get_file_size_2 (file_path_2):

   file_size = os.path.getsize(file_path_2)
   
   print("File Size is :", file_size, "bytes")   
   
   
   
def get_file_size_3 (file_path_3):

   # open file 
   file = open(file_path_3)
 
   # get the cursor positioned at end
   file.seek(0, os.SEEK_END)
 
   # get the current position of cursor 
   # this will be equivalent to size of file
   print("Size of file is :", file.tell(), "bytes")
   
   
   
from pathlib import Path   
   
def get_file_size_3 (file_path_4):

   # open file
   Path(file_path_4).stat()
 
   # getting file size
   file=Path(file_path_4).stat().st_size
 
   # display the size of the file
   print("Size of file is :", file, "bytes")
   
   
#get_file_size_3 (file_path_4='test_panda.csv')   


#################################################################################################
#### grouping files with matching string
#################################################################################################

def group_file_name_ends_with (folder_path, ends_with_str):

   LIST_file = oslistdir(folder_path)

   LIST_file_ends_with = []

   for file in LIST_file:
   
      if file.endswith(ends_with_str):
      
         LIST_file_ends_with.append(file)
         print (file + ' added to list') 
         
      else:
      
         print (file + ' NOT added to list')
         
         
   return LIST_file_ends_with
      
         
   
   
   
