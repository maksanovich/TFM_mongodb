

import numpy as np

# https://www.geeksforgeeks.org/break-list-chunks-size-n-python/


def list_SPLIT_1 (LIST_to_split, start_index, items_per_list ):

   LIST_of_list = []
        
   end_index = len(LIST_to_split)
     
   for i in range(start_index, end_index, items_per_list):
   
      x = i
      
      LIST_of_list.append(LIST_to_split[x:x+items_per_list])
      
      #print(LIST_to_split[x:x+items_per_list])
      
   return LIST_of_list



LIST = [1, 2, 3, 4, 5,
           6, 7, 8, 9, 934]

print (list_SPLIT_1 (LIST_to_split=LIST, start_index=0, items_per_list=4 ))


###############################################################################################################################
##### 
#################################################################################################################################


