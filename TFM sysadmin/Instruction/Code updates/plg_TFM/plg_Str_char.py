
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
   
#print (len(LIST_2_letter_str ()))
#print (LIST_2_letter_str ())
  
'''  
for num in range (100):

   for letter_group in LIST_2_letter_str ():

      print ('sq_' + letter_group + '_' + str(num))
'''      
     
     
def check_str_index (string, start_index, end_index):

   first_N_chars = string [start_index:end_index]
   
   return first_N_chars      
      

#print(check_str_index (string='shane fang', start_index=0, end_index=2))



#https://stackoverflow.com/questions/20988835/how-to-get-the-first-2-letters-of-a-string-in-python#:~:text=It%20is%20as%20simple%20as,do%20it%2C%20if%20you%20need.&text=In%20general%2C%20you%20can%20get,string%5B0%3A2%5D%20.
def get_first_N_char (string, char_num):

   result = string[:char_num]
   print (result)
   
   return result


#get_first_N_char (string='apple orange', char_num=2)
