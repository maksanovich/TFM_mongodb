

from a0_items import *

from fuzzywuzzy import fuzz


#https://www.datacamp.com/tutorial/fuzzy-string-python
# https://www.geeksforgeeks.org/fuzzywuzzy-python-library/

# string order matter    
def FZ_ratio (str_1, str_2, to_lower_case):
 
   if 'yes' in to_lower_case:
   
      score_1 = fuzz.ratio(str_1.lower(),str_2.lower())
      
      return score_1
      
   else:
   
      score_2 = fuzz.ratio(str_1,str_2)
      
      return score_2
   
   
#print (FZ_ratio (str_1="my book", str_2="My BOOK", to_lower_case='yes'))
   
   
   
   
# Order matters for partial ratio
def FZ_partial_ratio (str_1, str_2, to_lower_case):

   if 'yes' in to_lower_case:
   
      score_1 = fuzz.partial_ratio(str_1.lower(),str_2.lower())
      
      return score_1
      
   else:
   
      score_2 = fuzz.ratio(str_1,str_2)
      
      return score_2
   
   
#print (FZ_partial_ratio (str_1="book", str_2="back", to_lower_case='yes')  ) 
  

  
# similar strings but out of order. string similarity matter, order not matter.     
def FZ_token_sort_ratio (str_1, str_2, to_lower_case):

   if 'yes' in to_lower_case:
   
      score_1 = fuzz.token_sort_ratio(str_1.lower(),str_2.lower())
      
      return score_1
      
   else:
   
      score_2 = fuzz.ratio(str_1,str_2)
      
      return score_2
   
   
#print (FZ_token_sort_ratio (str_1="book shane", str_2="shane book", to_lower_case)  ) 
   
   
   
   
def FZ_token_set_ratio (str_1, str_2, to_lower_case):

   if 'yes' in to_lower_case:
   
      score_1 = fuzz.token_set_ratio(str_1.lower(),str_2.lower())
      
      return score_1
      
   else:
   
      score_2 = fuzz.ratio(str_1,str_2)
      
      return score_2
   
   
#print (FZ_token_set_ratio (str_1="book", str_2="back", to_lower_case ='no')  )



#handles lower and upper cases
def FZ_WRatio (str_1,str_2, to_lower_case):

   if 'yes' in to_lower_case:
   
      score_1 = fuzz.WRatio(str_1.lower(),str_2.lower())
      
      return score_1
      
   else:
   
      score_2 = fuzz.ratio(str_1,str_2)
      
      return score_2
   
   
#print (FZ_WRatio (str_1="my book", str_2="My BOOK", to_lower_case)  )