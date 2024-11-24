

from a0_items import * 
import random



#select random but allow null value in list # https://stackoverflow.com/questions/45639573/how-do-i-make-random-choice-include-not-choosing
def random_select_from_list (LIST_item):

   random_item = random.choice(LIST_item+[None])
   
   return random_item 


   
   


