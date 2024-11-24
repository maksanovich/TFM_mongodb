import sys
sys.path.append("../plg_CUSTOM/")
sys.path.append("../plg_UBUNTU/")
sys.path.append("../plg_TFM/")
from plg_CUSTOM import *
from plg_UBUNTU import *
from plg_TFM import *

class Create_delete:
    def __init__(self, LIST_file_path,LIST_databases):
        self.LIST_file_path = LIST_file_path
        self.LIST_databases = LIST_databases
    def create(self):
        log2('info', 'Create Database')
        try:
            for server in LIST_read_csv_server(self.LIST_file_path):
                server_ip, ssh_username, ssh_password = server_details(server)
                if server_ip:
                    ssh_client = Ssh_into_server(server_ip, ssh_username, ssh_password)
                    for database in self.LIST_databases:
                        command = cmd_create_database.format(db_name=database)
                        ssh_exec(ssh_client, command)
                    ssh_client.close()
        except Exception as e:
            log2('error', f"An error occurred in create_Database: {e}")

    def delete(self):
        log2('info', 'Delete Database')
        try:
            for server in LIST_read_csv_server(self.LIST_file_path):
                server_ip, ssh_username, ssh_password = server_details(server)
                if server_ip:
                    ssh_client = Ssh_into_server(server_ip, ssh_username, ssh_password)
                    for database in self.LIST_databases:
                        command = cmd_delete_database.format(db_name=database)
                        ssh_exec(ssh_client, command)
                    ssh_client.close()
        except Exception as e:
            log2('error', f"An error occurred in delete_Database: {e}")