import sys

sys.path.append("../plg_CUSTOM/")
sys.path.append("../plg_UBUNTU/")
sys.path.append("../plg_TFM/")
from plg_CUSTOM import *
from plg_UBUNTU import *
from plg_TFM import *

class Setup:
    def __init__(self, LIST_file_path):
        self.LIST_file_path = LIST_file_path

    def install(self):
        log2('info', 'Install MongoDB')
        try:
            for server in LIST_read_csv_server(self.LIST_file_path):
                server_ip, ssh_username, ssh_password = server_details(server)
                if server_ip:
                    ssh_client = Ssh_into_server(server_ip, ssh_username, ssh_password)
                    for command in cmd_install_mongodb:
                        ssh_exec(ssh_client, command)
                    ssh_client.close()

        except Exception as e:
            log2('error', f"An error occurred in install_mongodb: {e}")
    def remove(self):
        log2('info', 'Remove MongoDB')
        try:
            for server in LIST_read_csv_server(self.LIST_file_path):
                server_ip, ssh_username, ssh_password = server_details(server)
                if server_ip:
                    ssh_client = Ssh_into_server(server_ip, ssh_username, ssh_password)
                    for command in cmd_remove_mongodb:
                        ssh_exec(ssh_client, command)
                    ssh_client.close()

        except Exception as e:
            log2('error', f"An error occurred in remove_mongodb: {e}")