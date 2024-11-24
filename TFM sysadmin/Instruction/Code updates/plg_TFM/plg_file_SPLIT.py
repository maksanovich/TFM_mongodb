

from a0_items import *
from plg_Folders import * 



# https://stackoverflow.com/questions/8096614/split-large-files-using-python 
def split_file_by_lines (filename, lines_per_file, output_folder_path):

   ouput_folder = create_folder (output_folder_path) #create ouput folder if not exists
   
   with open(filename, 'rb') as fin:
   
      fout = open(folder_path + "F_0.txt","wb")    
      for i,line in enumerate(fin):         
         fout.write(line)
            
         if (i+1)%lines_per_file == 0:
            fout.close()
            fout = open(folder_path + "F_%d.txt"%(i/lines_per_file+1),"wb")

      fout.close()   
           
           
split_file_by_lines (filename='sample.txt', lines_per_file=200, output_folder_path ='../../data/raw/output_folder/')      




