
print ("i am from plg_SSH.py")


from a0_items import * 
import locale


##########################################################################################################################

def SSH_into_server (server_ip, SSH_username, SSH_password):

   try:
   
      client = paramiko.client.SSHClient()
      client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
      client.connect(server_ip.strip(), username=SSH_username.strip(), password=SSH_password.strip())     
   
      print (server_ip + ' is connected \n')      
      return client
           
   except:
   
      print (server_ip + ' NOT connected \n')
   





#https://stackoverflow.com/questions/62656579/why-im-getting-unicodeencodeerror-charmap-codec-cant-encode-character-u2 
def test ():  
 
   client1 = SSH_into_server (server_ip='173.208.150.146', SSH_username='root', SSH_password='Vgd9x0ay6i7p!')  
   _stdin_1, _stdout_1,_stderr_1 = client1.exec_command("df")
   _stdin_2, _stdout_2,_stderr_2 = client1.exec_command("lsblk")

   #encoding = locale.getpreferredencoding()

   print(_stdout_1.read().decode())
   print ('\n')
   #print(_stdout_2.read().decode(encoding))
   print(_stdout_2.read().decode('ascii', 'ignore'))

   client1.close()
   
#test()





###################################################################################################################################
#### SFTP
###################################################################################################################################

# https://rajansahu713.medium.com/sftp-files-transfer-using-python-59b4cead090a

def get_items_via_SSH (server_ip, SSH_username, SSH_password):

   #get files of remote server 
   client1 = SSH_into_server (server_ip, SSH_username, SSH_password) 

   sftp = client1.open_sftp()
   
   LIST_item = sftp.listdir()
   print (sftp.listdir())
   
   return LIST_item
   
#get_items_via_SSH (server_ip='107.150.45.226', SSH_username='root', SSH_password='Y4wxyopsvgu2!') 



#SFTP create folder 
def create_item_via_SSH (remote_file_path_name):

   #connection to SSH
   client1 = SSH_into_server (server_ip, SSH_username, SSH_password) 

   sftp = client1.open_sftp()
   
   sftp.mkdir (remote_file_path_name)
   



#SFTP get
def download_item_via_SSH (local_file_path, remote_file_path):

   #connection to SSH
   client1 = SSH_into_server (server_ip, SSH_username, SSH_password) 

   sftp = client1.open_sftp()
   
   sftp.get (remote_file_path, local_file_path)



#SFTP put 
def upload_item_via_SSH (local_file_path, remote_file_path):

   #connection to SSH
   client1 = SSH_into_server (server_ip, SSH_username, SSH_password) 

   sftp = client1.open_sftp()
   
   sftp.put (local_file_path, remote_file_path)




#SFTP remove
def remove_item_via_SSH (remote_file_path):

   #connection to SSH
   client1 = SSH_into_server (server_ip, SSH_username, SSH_password) 

   sftp = client1.open_sftp()
   
   sftp.remove (remote_file_path)
   
