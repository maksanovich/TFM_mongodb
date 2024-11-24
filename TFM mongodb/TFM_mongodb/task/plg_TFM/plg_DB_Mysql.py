

import mysql.connector



def Mysql_connect (Mysql_host, Mysql_user, Mysql_pass):

   try:
   
      mydb = mysql.connector.connect( host = Mysql_host, user = Mysql_user, password = Mysql_pass )
  
      print(str(mydb) + " --> Connected")
      
      return mydb
    
   except mysql.connector.Error as err:
   
      print("Error: {}".format(err))


#Mysql_connect (Mysql_host='localhost', Mysql_user='shane', Mysql_pass='')




def Mysql_get_ALL_DB (My_host, My_user, My_pass):

   LIST_db = []

   conn = Mysql_connect (Mysql_host=My_host, Mysql_user=My_user, Mysql_pass=My_pass)
   
   mycursor = conn.cursor()   
   mycursor.execute("SHOW DATABASES")
 
   myresult = mycursor.fetchall()
 
   for x in myresult:
   
      #print(x)
      LIST_db.append(x)
      
   return LIST_db
   

#print (Mysql_get_ALL_DB (My_host='localhost', My_user='root', My_pass=''))

'''
LIST_db = Mysql_get_ALL_DB (My_host='localhost', My_user='root', My_pass='')
for x in LIST_db:

   print (x)
'''



def Mysql_get_ALL_tables (My_host, My_user, My_pass, My_db_name):

   LIST_table = []

   conn = Mysql_connect (Mysql_host=My_host, Mysql_user=My_user, Mysql_pass=My_pass)
  
   mycursor = conn.cursor()
   mycursor.execute("Use " + str(My_db_name)) #use the database 
   mycursor.execute("SHOW TABLES")
 
   myresult = mycursor.fetchall()
 
   for x in myresult:
   
      #print(x)
      LIST_table.append(x)
      
   return LIST_table 


#Mysql_get_ALL_tables (My_host='localhost', My_user='root', My_pass='', My_db_name = 'joomla112')[1]



def Mysql_search_db_name (My_host, My_user, My_pass, My_db_name):

   LIST_all_db = Mysql_get_ALL_DB (My_host, My_user, My_pass)
   
   conn = Mysql_connect (Mysql_host=My_host, Mysql_user=My_user, Mysql_pass=My_pass)
   cursor = conn.cursor()
     
   for db in LIST_all_db:
   
      db_name = str(db).replace("'", "").replace("(", "").replace(")", "").replace(",", "")
      #print (db_name)
 
      if str(My_db_name).lower() in str(db_name).lower():
      
         DB_exists = 'yes'
         #print (My_db_name + ' in ' + db_name)
         
         return DB_exists
                        
      else:
         
         pass
         
         
#print (Mysql_search_db_name(My_host='localhost', My_user='root', My_pass='', My_db_name='Rajesh_db') )
   
 


def Mysql_create_DB (My_host, My_user, My_pass, My_db_name):

   conn = Mysql_connect (Mysql_host=My_host, Mysql_user=My_user, Mysql_pass=My_pass)
   cursor = conn.cursor()

   DB_name_exists = Mysql_search_db_name (My_host=My_host, My_user=My_user, My_pass=My_pass, My_db_name=My_db_name)
   
   #print (DB_name_exists)

   
   if DB_name_exists is not None and 'yes' in DB_name_exists:
   
      print (My_db_name + ' exists, database NOT created')

   else:
   
      cursor.execute("CREATE DATABASE IF NOT EXISTS " + str(My_db_name))
         
      print (My_db_name + ' NOT exists, database created')


#Mysql_create_DB (My_host='localhost', My_user='root', My_pass='', My_db_name='Rajesh_db') 
 



def Mysql_create_table (My_host, My_user, My_pass, My_db_name, table_name, table_columns):

   conn = Mysql_connect (Mysql_host=My_host, Mysql_user=My_user, Mysql_pass=My_pass)
   
   cursor = conn.cursor()
   cursor.execute("Use " + str(My_db_name)) #use the database 
   cursor.execute("CREATE TABLE IF NOT EXISTS " + table_name + " " + table_columns)

'''
tb_name = "customers"
tb_columns = "(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))"
Mysql_create_table (My_host='localhost', My_user='root', My_pass='', My_db_name='rajesh_db', table_name = "customers", table_columns="(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
'''



def Mysql_select_ALL_tb_data (My_host, My_user, My_pass , My_db_name, My_table_name):

   conn = Mysql_connect (Mysql_host=My_host, Mysql_user=My_user, Mysql_pass=My_pass)
   
   cursor = conn.cursor()
   cursor.execute("Use " + str(My_db_name)) #use the database 
   cursor.execute("SELECT * FROM " + My_table_name)

   myresult = cursor.fetchall()
   
   return myresult 
   

print (Mysql_select_ALL_tb_data (My_host='localhost', My_user='root', My_pass='' , My_db_name = 'rajesh_db', My_table_name='customers'))



def Mysql_delete_ALL_tb_data():

   pass
   



def Mysql_insert_tb_data (My_host, My_user, My_pass, My_db_name, My_sql , My_value):

   conn = Mysql_connect (Mysql_host=My_host, Mysql_user=My_user, Mysql_pass=My_pass)
   
   cursor = conn.cursor()
   cursor.execute("Use " + str(My_db_name)) #use the database 
   cursor.execute(My_sql, My_value)

   conn.commit()
   
   print(cursor.rowcount, "record inserted.")

'''
db = "rajesh_db"
sql ="INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
Mysql_insert_tb_data (My_host='localhost', My_user='root', My_pass='', My_db_name = db, My_sql =sql , My_value=val)
'''
   
   
   
def Mysql_update_tb_data (My_host, My_user, My_pass, My_db_name, My_sql , My_value):

   conn = Mysql_connect (Mysql_host=My_host, Mysql_user=My_user, Mysql_pass=My_pass)
   
   cursor = conn.cursor()
   cursor.execute("Use " + str(My_db_name)) #use the database 
   cursor.execute(My_sql, My_value)

   conn.commit()
   
   print(cursor.rowcount, "record(s) affected")
   
'''   
db = "rajesh_db"
sql = "UPDATE customers SET name =%s , address = %s WHERE address = %s"
val = ("peter", "kenmore 123", "moggill 123")
Mysql_update_tb_data (My_host='localhost', My_user='root', My_pass='', My_db_name = db, My_sql =sql , My_value=val)  

'''