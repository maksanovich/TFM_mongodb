

from a0_items import * 
import pymongo 
from pymongo import MongoClient
from pprint import pprint
import bson
import json


##### Must download & install MongoDB software from --> https://www.mongodb.com/try/download/community #######
# https://www.w3schools.com/python/python_mongodb_getstarted.asp

#################################################
########### Database ##############################


def create_DB (conn_str, db_name, coll_name):
   
   myclient = pymongo.MongoClient(conn_str)

   mydb = myclient[db_name]
   print (mydb, flush=True)

   #To create a db, we must create a collection 
   mydb.create_collection(coll_name)
   
   LIST_db = myclient.list_database_names()
   
   if db_name in LIST_db:
   
      print(db_name + " => database exists", flush=True)
          
   else:
      print (db_name + " => database NOT exists", flush=True)

    
#create_DB(conn_str ="mongodb://localhost:27017/", db_name = "TEST_1",  coll_name="test_sample")
  
  
def get_ALL_db_names (conn_str):

   myclient = pymongo.MongoClient(conn_str)
 
   LIST_db = myclient.list_database_names()
   print (LIST_db)
   
   return LIST_db


#get_ALL_db_names (conn_str="mongodb://localhost:27017/") 




####################################################################################
######## Collections ################################################################


def get_ALL_collection_in_db (conn_str, db_name):

   myclient = pymongo.MongoClient(conn_str)
   mydb = myclient[db_name]
 
   LIST_collection = mydb.list_collection_names()   
   
   print (LIST_collection, flush=True)   
   return LIST_collection 
 

#get_ALL_collection_in_db (conn_str="mongodb://localhost:27017/", db_name="Country_language")




#drop the only collection in db will also remove the db 
def drop_collection (conn_str, db_name, coll_name):

   myclient = pymongo.MongoClient(conn_str)

   mydb = myclient[db_name]
   mydb.drop_collection(coll_name)

 
#drop_collection(conn_str ="mongodb://localhost:27017/", db_name = "TEST_1",  coll_name="test_sample") 



def create_collection (conn_str, db_name, coll_name):

   myclient = pymongo.MongoClient(conn_str)
   mydb = myclient[db_name]
 
   LIST_collection = mydb.list_collection_names()   
   #print (LIST_collection)
   
   if coll_name in LIST_collection:
   
      print(coll_name + " => colleciton exists", flush=True)
      
   else:
      
      mydb.create_collection(coll_name)
      print (coll_name + " => collection NOT exists, is created", flush=True)
      
        
#create_collection (conn_str ="mongodb://localhost:27017/", db_name = "mydatabase",  coll_name="hello shane")         
         


# Rename collection - 
def rename_collection (conn_str, db_name, coll_name_OLD, coll_name_NEW):

   myclient = pymongo.MongoClient(conn_str)
   mydb = myclient[db_name]

   LIST_collection = mydb.list_collection_names()
   
   if coll_name_OLD in LIST_collection:
        
      mydb[coll_name_OLD].rename(coll_name_NEW, dropTarget = True)  # renaming the collection  
      print(coll_name_NEW + " => colleciton exists and renamed to => " + coll_name_NEW, flush=True)
      
   else:
      print(coll_name_OLD + " => NOT exists", flush=True)


#rename_collection (conn_str ="mongodb://localhost:27017/", db_name = "mydatabase",  coll_name_OLD="vvvv", coll_name_NEW="vv3543")   



#############################################################################################
##### Documents ##############################################################################


def create_ONE_document (conn_str, db_name, coll_name, doc_data):

   myclient = pymongo.MongoClient(conn_str)
   mydb = myclient[db_name]
   mycol = mydb[coll_name]

   x = mycol.insert_one(doc_data)
   doc_id = x.inserted_id
   
   print(doc_id)   
   return doc_id

'''
name = "john"
age="23"
address="1213 road"
country="China"
state="Beijing"
LIST_hobby = ["hobby_1", "hobby_23", "hobby_32"]

doc_data = {"name":name,
            "age":age,
            "address":address,
            "country":country,
            "state": state,
            "LIST_hobby":LIST_hobby}
        
create_ONE_document (conn_str ="mongodb://localhost:27017/", db_name = "mydatabase",  coll_name="mycoll", doc_data = doc_data)
'''


def create_MANY_document (conn_str, db_name, coll_name, LIST_doc_data):

   myclient = pymongo.MongoClient(conn_str)
   mydb = myclient[db_name]
   mycol = mydb[coll_name]

   x = mycol.insert_many(LIST_doc_data)
   LIST_doc_id = x.inserted_ids
   
   print(LIST_doc_id)   
   return LIST_doc_id

'''
mylist = [
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
]

create_MANY_document (conn_str ="mongodb://localhost:27017/", db_name = "mydatabase",  coll_name="hello shane", LIST_doc_data = mylist)
'''





#####################################################################################
###### Find documents ################################################################


def get_ALL_docs_in_collection (conn_str, db_name, coll_name):

   LIST_doc = []

   myclient = pymongo.MongoClient(conn_str)
   mydb = myclient[db_name]   

   collection = mydb[coll_name]

   LIST_document = collection.find()
   
   #print (LIST_document) #this won't work, must loop through list 
   
   for doc in LIST_document:
      
      #print (doc)
      LIST_doc.append(doc)
   
   #print (LIST_doc)   
   return LIST_doc


LIST_all_doc = get_ALL_docs_in_collection (conn_str ="mongodb://localhost:27017/", db_name = "mydatabase",  coll_name="vv3543")


doc_key_1 = 'name'
doc_key_2 = 'address'

'''
for doc in LIST_all_doc:

   print(doc[doc_key_1] + ' => ' + doc[doc_key_2]) # get values by key
'''

'''
LIST_to_be_item = []

for doc in LIST_all_doc:

   if 'John' in doc[doc_key_1]:
      pass
      
   else:
   
      LIST_to_be_item.append (doc)
      print (doc)
      
'''



def get_FIRST_doc (conn_str, db_name, coll_name):

   myclient = pymongo.MongoClient(conn_str)
   mydb = myclient[db_name]   

   collection = mydb[coll_name]

   FIRST_document = collection.find_one()
   
   print (FIRST_document)
   return FIRST_document

#get_FIRST_doc (conn_str ="mongodb://localhost:27017/", db_name = "mydatabase",  coll_name="vv3543")



# https://stackoverflow.com/questions/38476377/bson-object-size-of-document-retrieved-from-db
def get_doc_size (conn_str, db_name, coll_name):

   myclient = pymongo.MongoClient(conn_str)
   mydb = myclient[db_name]   

   collection = mydb[coll_name]

   FIRST_document = collection.find_one()
   
   #Doc_size = object.bsonsize(FIRST_document)
   
   Doc_size = len(bson.BSON.encode(FIRST_document))
   
   print (str(Doc_size) + ' bytes')
   return Doc_size

#get_doc_size (conn_str ="mongodb://localhost:27017/", db_name = "mydatabase",  coll_name="vv3543")   





#####################################################################################
###### Delete documents ################################################################

def delete_ONE_document (conn_str, db_name, coll_name, doc_values):

   myclient = pymongo.MongoClient(conn_str)
   mydb = myclient[db_name]
   mycol = mydb[coll_name]

   mycol.delete_one(doc_values)


#delete_document (conn_str, db_name, coll_name, doc_values)



def delete_ALL_docs_in_collection (conn_str, db_name, coll_name):

   myclient = pymongo.MongoClient(conn_str)
   mydb = myclient[db_name]
   mycol = mydb[coll_name]

   x = mycol.delete_many({})

   print(x.deleted_count, " documents deleted.")
   

#delete_ALL_docs_in_collection (conn_str, db_name, coll_name)



#####################################################################################
###### Update documents ################################################################


def update_ONE_document (conn_str, db_name, coll_name, values_OLD, values_NEW):

   myclient = pymongo.MongoClient(conn_str)
   mydb = myclient[db_name]
   mycol = mydb[coll_name]
   
   mycol.update_one(values_OLD, values_NEW)


#update_ONE_document (conn_str ="mongodb://localhost:27017/", db_name = "mydatabase",  coll_name="mycoll", values_OLD={ "name": "shane" }, values_NEW={ "$set": { "name": "PETER123" } })



def update_MANY_document ():

   myclient = pymongo.MongoClient(conn_str)
   mydb = myclient[db_name]
   mycol = mydb[coll_name]
   
   #To be completed soon 
 


