
from a0_items import *



#print (os.listdir(folder_MASTER_data_LOG))
folder_LOG_DB = '../data/cooked/LOG_173_208_166_82/'
LOG_DB = 'TASK_a1_get_trans_joomla_P.db'
TFM_task_action = 'FROM 01-Jan-2023 1:00 TO 01-Jan_2023 1:29'



# https://www.sqlitetutorial.net/sqlite-python/creating-tables/
def create_connection(LOG_DB):

    conn = None
    try:
        conn = sqlite3.connect(folder_MASTER_data_LOG + folder_LOG_DB + LOG_DB)
        
        #print ("successuflly connected")
        return conn
        
    except Error as e:
        print(e)

    return conn

#create_connection(LOG_DB)


############################################################################
## LOG - first update - started
############################################################################

def DB_LOG_get_progress_items_0 (LOG_DB):
 
   now = datetime.now()
   item_new = ' #_0 ' + str(now)

   con_sqlite = create_connection(LOG_DB)
   cursor=con_sqlite.cursor()
   cursor.execute("SELECT * FROM LOG_request WHERE TFM_task_action=?", (TFM_task_action,))

   rows = cursor.fetchone()
   
   progress_items = rows[4].strip()
   #print (progress_items)
   
   LIST_new = progress_items.partition("#_0")[0].strip() #remove all strings after #_0
   #print (LIST_new)

   LIST_updated = LIST_new + item_new
   #print (LIST_updated)
   
   return LIST_updated

#DB_LOG_get_progress_items_0(LOG_DB)



# Start - 1st update
def DB_LOG_update_0 (LOG_DB, TFM_task_action):
 
   Total_progress_items = '1'
   Completed = '25%'

   con_sqlite = create_connection(LOG_DB)
   cursor=con_sqlite.cursor()
   cursor.execute('''UPDATE LOG_request SET Started_date_time = ?, Progress_items = ?, Total_progress_items =?, Completed =? WHERE TFM_task_action = ?''', (LOG_date_time, str(DB_LOG_get_progress_items_0(LOG_DB)), Total_progress_items, Completed, TFM_task_action)) 
   con_sqlite.commit ()


#DB_LOG_update_0 ()



############################################################################
## LOG - second update
############################################################################

def DB_LOG_get_progress_items_1 (LOG_DB, TFM_task_action):
 
   now = datetime.now()
   item_new = ' #_1 ' + str(now)

   con_sqlite = create_connection(LOG_DB)
   cursor=con_sqlite.cursor()
   cursor.execute("SELECT * FROM LOG_request WHERE TFM_task_action=?", (TFM_task_action,))

   rows = cursor.fetchone()
   
   progress_items = rows[4]
   #print (progress_items)
   
   LIST_new = progress_items.partition("#_1")[0]#remove all strings after #_1
   #print (LIST_new)

   LIST_updated = LIST_new + item_new
   #print (LIST_updated)
   
   return LIST_updated

#DB_LOG_get_progress_items_1(LOG_DB)



# 2nd update
def DB_LOG_update_1 (LOG_DB, TFM_task_action):
   
   LIST_progress_item = str(DB_LOG_get_progress_items_1(LOG_DB))
   Total_progress_items = '2'
   Completed = '50%'
   
   con_sqlite = create_connection(LOG_DB)
   cursor=con_sqlite.cursor()
   cursor.execute('''UPDATE LOG_request SET Started_date_time = ?, Progress_items = ?, Total_progress_items=?, Completed =? WHERE TFM_task_action = ?''', (LOG_item, LIST_progress_item, Total_progress_items, Completed, TFM_task_action)) 
   con_sqlite.commit ()
   


############################################################################
## LOG - third update
############################################################################

def DB_LOG_get_progress_items_2 (LOG_DB, TFM_task_action):
 
   now = datetime.now()
   item_new = ' #_2 ' + str(now)

   con_sqlite = create_connection(LOG_DB)
   cursor=con_sqlite.cursor()
   cursor.execute("SELECT * FROM LOG_request WHERE TFM_task_action=?", (TFM_task_action,))

   rows = cursor.fetchone()
   
   progress_items = rows[4]
   #print (progress_items)
   
   LIST_new = progress_items.partition("#_2")[0]#remove all strings after #_1
   #print (LIST_new)

   LIST_updated = LIST_new + item_new
   #print (LIST_updated)
   
   return LIST_updated

#DB_LOG_get_progress_items_2(LOG_DB)


# 3rd update
def DB_LOG_update_2 (LOG_DB, TFM_task_action):

   LIST_progress_item = str(DB_LOG_get_progress_items_1(LOG_DB))
   Total_progress_items = '3'
   Completed = '75%'
   
   con_sqlite = create_connection(LOG_DB)
   cursor=con_sqlite.cursor()
   cursor.execute('''UPDATE LOG_request SET Started_date_time = ?, Progress_items = ?, Total_progress_items=?, Completed =? WHERE TFM_task_action = ?''', (LOG_item, LIST_progress_item, Total_progress_items, Completed, TFM_task_action)) 
   con_sqlite.commit ()
   
   
   
############################################################################
## LOG - last update - finished
############################################################################   
   
def DB_LOG_get_progress_items_3 (LOG_DB, TFM_task_action):
 
   now = datetime.now()
   item_new = ' #_3 ' + str(now)

   con_sqlite = create_connection(LOG_DB)
   cursor=con_sqlite.cursor()
   cursor.execute("SELECT * FROM LOG_request WHERE TFM_task_action=?", (TFM_task_action,))

   rows = cursor.fetchone()
   
   progress_items = rows[4]
   #print (progress_items)
   
   LIST_new = progress_items.partition("#_3")[0]#remove all strings after #_1
   #print (LIST_new)

   LIST_updated = LIST_new + item_new
   #print (LIST_updated)
   
   return LIST_updated

#DB_LOG_get_progress_items_3(LOG_DB)   
   
    
    
# Finish - last update
def DB_LOG_update_3 (LOG_DB, TFM_task_action):

   LIST_progress_item = str(DB_LOG_get_progress_items_1(LOG_DB))
   Total_progress_items = '4'
   Completed = '100%'
   
   con_sqlite = create_connection(LOG_DB)
   cursor=con_sqlite.cursor()
   cursor.execute('''UPDATE LOG_request SET Started_date_time = ?, Progress_items = ?, Total_progress_items= ?, Completed =? WHERE TFM_task_action = ?''', (LOG_item, LIST_progress_item, Total_progress_items, Completed, TFM_task_action)) 
   con_sqlite.commit ()
   
   
   
if __name__ == "__main__":

    DB_LOG_update_0 (LOG_DB, TFM_task_action):
    DB_LOG_update_1 (LOG_DB, TFM_task_action):
    #DB_LOG_update_2 (LOG_DB, TFM_task_action):
    #DB_LOG_update_3 (LOG_DB, TFM_task_action):