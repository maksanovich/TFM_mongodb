
from a0_items import * 



# https://stackoverflow.com/questions/71705688/how-to-remove-numbers-from-text_mains
def remove_numbers_from_text_main (text_main):

   text_main_no_num = re.sub('[0-9]', '', text_main)
   
   return text_main_no_num


#print(remove_numbers_from_text_main (text_main = 'hello3535'))




def remove_all_before_text (before_text, text_main):

   new_text_main = re.sub(r'^.*?' + before_text, '', text_main).strip()
   
   return new_text_main 

#print (remove_all_before_text (before_text='/0', text_main ='/0_hello_world_/2_john its me'))




def remove_all_after_text (after_text, text_main):

   new_text_main = text_main.partition(after_text)[0].strip()
   
   return new_text_main
   
#print (remove_all_after_text (after_text='a_1', text_main ='a_0 hello world a_1 john its me'))




def remove_all_before_and_after_texts (before_text, after_text, text_main):

   new_text = re.sub(r'^.*?'+before_text, '', text_main.partition(after_text)[0]).strip()

   return new_text
   

#print (remove_all_before_and_after_texts (before_text='/1_', after_text='/2_', text_main='Folders/1_TFM_param_1/2_TFM_param_2/3_TFM_param_3/4_TFM_param_4'))




#https://stackoverflow.com/questions/32732506/how-can-i-remove-words-in-a-sentence-starting-with-a-particular-set-of-character
#https://stackoverflow.com/questions/51343919/remove-word-from-string-start-with-specific-characters

def remove_all_text_starts_with_characters_1 (start_char, text_main):

   new_text = re.sub(r'\b' + str(start_char) + '\w+', '', str(text_main))
   
   return new_text
 
#text = 'hello, john in hell but hellen is not'   
#print(remove_all_text_starts_with_characters_1 (start_char='hell', text_main=text) )  
   
   
   
def remove_all_text_starts_with_characters_2 (start_char, text_main):

   new_text = re.sub('(?:\s)'+ str(start_char)  +'[^, ]*', '', str(text_main))
   
   return new_text
   
   
#text = 'hello, john in hell but hellen is not'   
#print(remove_all_text_starts_with_characters_2 (start_char='hell', text_main=text) )    





def get_first_letter_of_string (string):

   letter = re.findall(r'\b\w', string)
   return letter
   
'''   
First_letter = get_first_letter_of_string (string='hey whats')   
print (First_letter)
'''