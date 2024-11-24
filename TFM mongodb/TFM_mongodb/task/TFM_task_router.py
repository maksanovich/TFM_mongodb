import sys

sys.path.append('core_TASK/')
sys.path.append('plg_CUSTOM/')
sys.path.append('plg_UBUNTU/')
sys.path.append('plg_TFM/')

from plg_CUSTOM import *
from core_TASK import *
from plg_TFM import *

def select_task(TFM_task, TFM_task_action, LIST_file_path=None, LIST_databases=None,
                LIST_dump_databases=None, LIST_restore_databases=None
                , PRIMARY_server=None, LIST_secondary_server=None,replica_set_name="", LIST_config_server=None,
                config_replica_set_name=None,LIST_shard_server=None,shard_replica_set_name=None,mongos_server=None, mongos_port=None, mongos_log_folder=None,mongos_conf_file=""):
    match TFM_task:
        case "Mongodb":
            log2("info", "Implement Mongodb")
            match TFM_task_action:
                case "Install_MongoDB":
                    Mongodb_setup = Setup(LIST_file_path)
                    Mongodb_setup.install()
                case "Remove_MongoDB":
                    Mongodb_setup = Setup(LIST_file_path)
                    Mongodb_setup.remove()
                case "Create_Database":
                    Mongodb_create_delete = Create_delete(LIST_file_path,LIST_databases)
                    Mongodb_create_delete.create()
                case "Delete_Database":
                    Mongodb_create_delete = Create_delete(LIST_file_path,LIST_databases)
                    Mongodb_create_delete.delete()
                case "Dump_Database":
                    Mongodb_backup_restore = Backup_restore(LIST_file_path)
                    Mongodb_backup_restore.dump(LIST_dump_databases)
                case "Restore_Database":
                    Mongodb_backup_restore = Backup_restore(LIST_file_path)
                    Mongodb_backup_restore.restore(LIST_restore_databases)
                case "Replication":
                    Mongodb_replication = Replication(PRIMARY_server,LIST_secondary_server,replica_set_name)
                    Mongodb_replication.start()
                case "Sharding":
                    Mongodb_sharding = Sharding(LIST_config_server,config_replica_set_name,LIST_shard_server,
                                      shard_replica_set_name, mongos_server, mongos_port,mongos_log_folder,mongos_conf_file)
                    Mongodb_sharding.start()


csv_TFM_email_hosts = "../data/raw/TFM_email_cluster.csv"

select_task(TFM_task="RAW_folders_create", TFM_task_action='')
#install
# select_task(TFM_task="Mongodb", TFM_task_action='Install_MongoDB'
#            , LIST_file_path=[csv_TFM_email_hosts])
#Remove
# select_task(TFM_task="Mongodb", TFM_task_action='Remove_MongoDB'
#            , LIST_file_path=[csv_TFM_email_hosts])
#create multiple databases
# select_task(TFM_task="Mongodb", TFM_task_action='Create_Database'
#             , LIST_file_path=[csv_TFM_email_hosts], LIST_databases=["demo"])
#delete databases
# select_task(TFM_task="Mongodb", TFM_task_action='Delete_Database'
#             , LIST_file_path=[csv_TFM_email_hosts], LIST_databases=["demo"])
#dump database
# select_task(TFM_task="Mongodb", TFM_task_action='Dump_Database'
#             , LIST_file_path=[csv_TFM_email_hosts], LIST_dump_databases=[{"name": "demo", "backup_path": "/root/backup/"}])

#Restore database
# select_task(TFM_task="Mongodb", TFM_task_action='Restore_Database'
#             , LIST_file_path=[csv_TFM_email_hosts], LIST_restore_databases=[{"name": "demo", "backup_path": "/root/backup/",
#                                                                              "delete_backup":True}])

PRIMARY_server = {"ip": "146.190.93.109", "username": "root", "password": "169Mabdb"}
LIST_secondary_server = [
    {"ip": "178.128.16.216", "username": "root", "password": "169Mabdb"},
    # {"ip": "146.190.93.53", "username": "root", "password": "169Mabdb"}
    # Add more nodes as needed
]

replica_set_name = "rs1"
#Replication
# select_task(TFM_task="Mongodb", TFM_task_action='Replication'
#             , PRIMARY_server=PRIMARY_server, LIST_secondary_server=LIST_secondary_server, replica_set_name=replica_set_name)

#Sharding
# before sharding make sure delete replication from mongod.conf file from each server if they have
LIST_config_server = [{"ip": "146.190.93.109", "username": "root", "password": "169Mabdb","primary":True}] # there will just one primary and insert in first
config_replica_set_name = "rs1"
LIST_shard_server = [
    {"ip": "178.128.16.216", "username": "root", "password": "169Mabdb", "primary":True},
    # {"ip": "146.190.93.53", "username": "root", "password": "169Mabdb"}
    # Add more nodes as needed
    # There will be just one primary and insert in first
]
shard_replica_set_name = "rs2"
# Delete mongos.conf file from mongos server if it has
mongos_server = {"ip": "146.190.93.53", "username": "root", "password": "169Mabdb"}
mongos_port = 27018

select_task(TFM_task="Mongodb",TFM_task_action='Sharding',LIST_config_server=LIST_config_server,config_replica_set_name=config_replica_set_name,
            LIST_shard_server=LIST_shard_server,shard_replica_set_name=shard_replica_set_name,mongos_server=mongos_server,
            mongos_port=mongos_port, mongos_log_folder="/etc/mongodb-configs/", mongos_conf_file="/etc/mongos.conf")