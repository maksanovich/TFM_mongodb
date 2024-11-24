import sys
import time
sys.path.append("../plg_CUSTOM/")
sys.path.append("../plg_UBUNTU/")
sys.path.append("../plg_TFM/")
from plg_CUSTOM import *
from plg_UBUNTU import *
from plg_TFM import *

class Sharding:
    def __init__(self,LIST_config_server,config_replica_set_name,LIST_shard_server,
                                      shard_replica_set_name, mongos_server, mongos_port,mongos_log_folder,mongos_conf_file):
        self.LIST_config_server = LIST_config_server
        self.config_replica_set_name = config_replica_set_name
        self.LIST_shard_server = LIST_shard_server
        self.shard_replica_set_name = shard_replica_set_name
        self.mongos_server = mongos_server
        self.mongos_port = mongos_port
        self.mongos_log_folder = mongos_log_folder
        self.mongos_conf_file = mongos_conf_file



    def start(self):
        log2('info', 'Sharding')
        try:
            LIST_all_server = [self.mongos_server]
            LIST_all_server.extend(self.LIST_config_server)
            LIST_all_server.extend(self.LIST_shard_server)
            # setup configsvr
            setup_config_server(self.LIST_config_server, self.config_replica_set_name, LIST_all_server)
            # setup shardsvr
            setup_shared_server(self.LIST_shard_server, self.shard_replica_set_name, LIST_all_server)
            # mongos
            setup_mongos(LIST_all_server, self.mongos_server, self.mongos_port, self.LIST_config_server, self.config_replica_set_name,
                         self.LIST_shard_server, self.shard_replica_set_name, self.mongos_log_folder, self.mongos_conf_file)


        except Exception as e:
            log2('error', f"An error occurred in sharding: {e}")