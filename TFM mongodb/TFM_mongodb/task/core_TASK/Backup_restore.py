import sys
sys.path.append("../plg_CUSTOM/")
sys.path.append("../plg_UBUNTU/")
sys.path.append("../plg_TFM/")
from plg_CUSTOM import *
from plg_UBUNTU import *
from plg_TFM import *

class Backup_restore:
    def __init__(self, LIST_file_path):
        self.LIST_file_path = LIST_file_path

    def dump(self, LIST_dump_databases):
        log2('info', 'Dump Database')
        try:
            for server in LIST_read_csv_server(self.LIST_file_path):
                server_ip, ssh_username, ssh_password = server_details(server)
                if server_ip:
                    ssh_client = Ssh_into_server(server_ip, ssh_username, ssh_password)
                    for database in LIST_dump_databases:
                        command = cmd_dump_database.format(db_name=database["name"],
                                                           backup_path=database["backup_path"])
                        ssh_exec(ssh_client, command)
                    ssh_client.close()
        except Exception as e:
            log2('error', f"An error occurred in dump_Database: {e}")

    def restore(self,LIST_restore_databases):
        log2('info', 'Restore Database')
        try:
            for server in LIST_read_csv_server(self.LIST_file_path):
                server_ip, ssh_username, ssh_password = server_details(server)
                if server_ip:
                    ssh_client = Ssh_into_server(server_ip, ssh_username, ssh_password)
                    for database in LIST_restore_databases:
                        # restore
                        command = cmd_restore_database.format(db_name=database["name"],
                                                              backup_path=database["backup_path"])
                        ssh_exec(ssh_client, command)
                        # delete backup
                        if database["delete_backup"]:
                            delete_command = cmd_delete_backup.format(
                                backup_path=f'{database["backup_path"]}/{database["name"]}/')
                            ssh_exec(ssh_client, delete_command)
                    ssh_client.close()
        except Exception as e:
            log2('error', f"An error occurred in restore_Database: {e}")