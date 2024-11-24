
from a0_items import *



#create db file  (./ = same folder, ../ = outside current folder)
# https://stackoverflow.com/questions/5801170/python-sqlite-create-table-if-not-exists-problem
def sqlite_create_file (sqlite_path, sql):

   if os.path.isfile(sqlite_path):
   
      print (sqlite_path + ' alraedy exists')
      
   else:
  
      conn = sqlite3.connect (sqlite_path)
      
      c = conn.cursor()
      c.execute(sql)

      conn.commit()
     
      print (sqlite_path + ' NOT exists, is created!')


'''
db_file = 'DB_shane.db'
sql_create = 'create table if not exists HELLO_table (ID integer primary key autoincrement, name text)'

sqlite_create_file (sqlite_path = 'DB_shane.db', sql = sql_create)
'''


# Use loop to insert multiple values of ONE column only 
def sqlite_insert_data (sqlite_path, sql_insert, data):

   conn = sqlite3.connect(sqlite_path)
   c = conn.cursor()

   c.execute(sql_insert,(data,)) #must have , at the end of data variable, 1 element tuple -- https://stackoverflow.com/questions/16856647/sqlite3-programmingerror-incorrect-number-of-bindings-supplied-the-current-sta
   
   conn.commit()

'''
sql = 'INSERT INTO Country_language (country_code)VALUES(?)'
sqlite_insert_data (sqlite_path='../../data/cooked/DB_country_language/China.db', sql_insert=sql, data='just_country_code')
'''



# Use loop to insert multiple values of ONE column only 
def sqlite_insert_data_multi_columns (sqlite_path, sql, data):

   conn = sqlite3.connect(sqlite_path)
   c = conn.cursor()

   c.execute(sql, data) # https://pynative.com/python-sqlite-insert-into-table/
   conn.commit()
   
   

def test_code ():   
   
   sqlite_insert_with_param = """INSERT INTO SqliteDb_developers
                          (id, name, email, joining_date, salary) 
                          VALUES (?, ?, ?, ?, ?);"""

   data_tuple = ('2', 'TFM', 'hello@email.com')   
   
   sqlite_insert_data_multi_columns (sqlite_path ='sqlite.db', sql = sqlite_insert_with_param, data = data_tuple)   
   
   

#######################################################################################################
#######################################################################################################

# https://pynative.com/python-sqlite-update-table/
# Use loop to update multiple values. But update 1 column at a time (ref_column = reference column)

def sqlite_update_data (sqlite_path, sql_update, update_data):

   try:
    
      sqliteConnection = sqlite3.connect(sqlite_path)
      cursor = sqliteConnection.cursor()
      print("Connected to SQLite")
 
      cursor.execute(sql_update, update_data)
      sqliteConnection.commit()
      print("Record Updated successfully")
      cursor.close()

   except sqlite3.Error as error:
    
      print("Failed to update sqlite table", error)
        

'''
sql = "Update Country_language set country_code = ? where id = ?"
data_tuple = ('TEST123', '1')
sqlite_update_data (sqlite_path='../../data/cooked/DB_country_language/China.db', sql_update=sql, update_data = data_tuple)
'''



def sqlite_delete_table (sqlite_path, table_name):

   conn = sqlite3.connect(Sqlite_file)
   c = conn.cursor()

   sql = 'drop table ' + table_name
   c.execute(sql)

   conn.commit()



def sqlite_select_ALL_data (sqlite_path, sql):

   LIST_sqlite_data = []

   conn = sqlite3.connect(sqlite_path)
   c = conn.cursor()
   
   c.execute(sql)

   LIST_sqlite_data = c.fetchall()   
   
   return LIST_sqlite_data
  
'''
sql_select = "SELECT * FROM Country_language "
LIST_test = sqlite_select_ALL_data (sqlite_path= '../../data/cooked/DB_country_language/China.db', sql=sql_select)

print (len(LIST_test))

for x in LIST_test:

   if len(str(x))==0 or x is None or x == None :
   
      print (" None ")
      
   else:
   
      print (" NOT none")
'''

 

def sqlite_delete_ALL_data (sqlite_path, table_name):

   conn = sqlite3.connect(sqlite_path)
   c = conn.cursor()

   sql = 'DELETE FROM ' + table_name 
   cur = conn.cursor()
   cur.execute(sql)
   conn.commit()
   
   
#sqlite_delete_ALL_data (sqlite_path= '../../data/cooked/DB_country_language/China.db', table_name='Country_language')   