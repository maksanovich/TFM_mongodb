import sys
import time
sys.path.append("../plg_CUSTOM/")
sys.path.append("../plg_UBUNTU/")
sys.path.append("../plg_TFM/")
from plg_CUSTOM import *
from plg_UBUNTU import *
from plg_TFM import *

class Replication:
    def __init__(self, PRIMARY_server, LIST_secondary_server, replica_set_name):
        self.PRIMARY_server = PRIMARY_server
        self.LIST_secondary_server = LIST_secondary_server
        self.replica_set_name = replica_set_name

    def start(self):
        log2('info', 'Replication')
        try:
            primary_ip = self.PRIMARY_server["ip"]
            primary_username = self.PRIMARY_server["username"]
            primary_password = self.PRIMARY_server["password"]
            LIST_all_server = [elem for elem in self.LIST_secondary_server]
            LIST_all_server.append(self.PRIMARY_server)
            LIST_all_server.reverse()
            for server in LIST_all_server:
                server_ip = server['ip']
                server_username = server['username']
                server_password = server['password']
                ssh_client = Ssh_into_server(server_ip, server_username, server_password)
                ssh_exec(ssh_client, cmd_bind_ip.format(host=server_ip))
                time.sleep(2)
                ssh_exec(ssh_client, set_replica_command.format(
                    replica_set_config=replica_set_config.format(replica_set_name=self.replica_set_name)))
                restart_mongo(ssh_client)
                allow_mongo_to_other_server(ssh_client, server_ip, LIST_all_server)
                ssh_client.close()
                print(f"Replication setup complete on {server_ip}.")

            time.sleep(10)
            members = ", ".join([f"{{ _id: {i}, host: '{node['ip']}:27017' }}" for i, node in enumerate(LIST_all_server)])
            repl_set_init = f'''
                    rs.initiate({{
                        _id: \\"{self.replica_set_name}\\",
                        members: [{members}]
                    }})
                    '''
            ssh_client = Ssh_into_server(primary_ip, primary_username, primary_password)
            ssh_exec(ssh_client, cmd_repl_set_init.format(repl_set_init=repl_set_init))
            ssh_client.close()
            time.sleep(10)
        except Exception as e:
            log2('error', f"An error occurred in replication: {e}")