
from faker import Faker
from mimesis import Person
#from mimesis.locales import Locale
#from mimesis.enums import Gender


###########################################################
#### Fake profile - Memesis
############################################################

def create_fake_profile_1 (profile_count):

   #de = Person(locale=Locale.DE)
   #en = Person(locale=Locale.EN)
   person = Person()
   
   LIST_profile = []

   for x in range (profile_count):
   
      full_name = person.full_name()
      age = person.age()
      gender= person.gender()
      height= person.height()
      language = person.language()
      nationality = person.nationality()
      academic_degree = person.academic_degree()
      email = person.email()
      occupation = person.occupation()
      
      LIST_profile.append ('#_full_name ' + str(full_name) + ' #_age ' + str(age) 
      + ' #_gender ' + str(gender) + ' #_height ' + str(height) + ' #_language ' + str(language)
      + ' #_nationality ' + nationality + ' #_academic ' + str(academic_degree) + ' #_email ' 
      + str(email) + ' #_occupation ' + str(occupation))
         
   return LIST_profile
   
''' 
LIST_test = create_fake_profile_1 (profile_count=10)    

for x in LIST_test:
   print (x.encode('ascii'))
'''  


###########################################################
#### Fake profile - Faker
############################################################

# https://www.datacamp.com/tutorial/creating-synthetic-data-with-python-faker-tutorial
def create_fake_profile_2 (profile_count):

   fake = Faker()
   
   LIST_profile = []
   
   for x in range (profile_count):
       
      profile = fake.profile()      
      print (str(x) + ' --> ' + str(profile))
      
      LIST_profile.append (profile)
      
   return LIST_profile 
 
create_fake_profile_2 ( profile_count=10)  

#LIST_test = create_fake_profile_2 ( profile_count=100)     

'''
for x in LIST_test:
   print (x.encode('ascii'), flush=True)
'''     
      
   
###########################################################
#### Fake profile - Custom
############################################################   
