
from a0_items import * 

import sys
sys.path.append('../plg_TFM/') 



def str_to_lowercase (string):

   lower_str = string.lower()

   return lower_str
   
#print (str_to_lowercase (string='ABC_HELLO'))

 
 
def LIST_2_letter_str ():

   LIST_letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

   LIST_first_2_letters = []
   
   for x in LIST_letter:

      for y in LIST_letter:
   
         z = x+y
         #print (z)
         
         LIST_first_2_letters.append(z)
   
   return LIST_first_2_letters
   
print (len(LIST_2_letter_str ()))
         
      
      
     
def check_str_index (string, start_index, end_index):

   first_N_chars = string [start_index:end_index]
   
   return first_N_chars      
      

#print(check_str_index (string='shane fang', start_index=0, end_index=2))