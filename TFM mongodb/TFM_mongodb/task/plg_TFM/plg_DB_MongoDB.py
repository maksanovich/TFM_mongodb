import sys
import time

sys.path.append("../plg_CUSTOM/")
sys.path.append("../plg_UBUNTU/")
from plg_CUSTOM import *
from plg_UBUNTU import *

def allow_mongo_to_other_server(ssh_client,server_ip,LIST_all_server):
    ssh_exec(ssh_client, cmd_delete_deny_mongo_port)
    for other_server in LIST_all_server:
        if server_ip != other_server["ip"]:
            ssh_exec(ssh_client, cmd_allow_ip_to_mongo.format(remote_host=other_server["ip"]))
    ssh_exec(ssh_client, cmd_deny_mongo_port)
    ssh_exec(ssh_client, cmd_allow_ssh)
    ssh_exec(ssh_client, cmd_ufw_enable)

def restart_mongo(ssh_client):
    ssh_exec(ssh_client, cmd_delete_mongo_sock)
    ssh_exec(ssh_client, cmd_restart_mongod)


def allow_mongos_to_other_server(ssh_client,server_ip,LIST_all_server,mongos_port):
    ssh_exec(ssh_client, cmd_delete_deny_mongos_port.format(port=mongos_port))
    for other_server in LIST_all_server:
        if server_ip != other_server["ip"]:
            ssh_exec(ssh_client, cmd_allow_ip_to_mongos.format(remote_host=other_server["ip"],port=mongos_port))
    ssh_exec(ssh_client, cmd_deny_mongos_port.format(port=mongos_port))
    ssh_exec(ssh_client, cmd_allow_ssh)
    ssh_exec(ssh_client, cmd_ufw_enable)


def setup_config_server(LIST_config_server,config_replica_set_name,LIST_all_server):
    for server in LIST_config_server:
        server_ip = server['ip']
        server_username = server['username']
        server_password = server['password']
        ssh_client = Ssh_into_server(server_ip, server_username, server_password)
        ssh_exec(ssh_client, cmd_bind_ip.format(host=server_ip))
        ssh_exec(ssh_client, set_sharding_command.format(
            shard_config=configserver_sharding_config.format(replica_set_name=config_replica_set_name)))
        time.sleep(2)
        restart_mongo(ssh_client)
        allow_mongo_to_other_server(ssh_client, server_ip, LIST_all_server)
        ssh_client.close()
        print(f"Sharding Configsvr setup complete on {server_ip}.")
    for server in LIST_config_server:
        if server["primary"]:
            server_ip = server['ip']
            server_username = server['username']
            server_password = server['password']
            ssh_client = Ssh_into_server(server_ip, server_username, server_password)
            members = ", ".join(
                [f"{{ _id: {i}, host: '{node['ip']}:27017' }}" for i, node in enumerate(LIST_config_server)])
            repl_set_init = f'''
                                        rs.initiate({{
                                            _id: \\"{config_replica_set_name}\\",
                                            configsvr: true,
                                            members: [{members}]
                                        }})
                                        '''
            ssh_exec(ssh_client, cmd_repl_set_init.format(repl_set_init=repl_set_init))
            restart_mongo(ssh_client)
            ssh_client.close()


def setup_shared_server(LIST_shard_server,shard_replica_set_name,LIST_all_server):
    for server in LIST_shard_server:
        server_ip = server['ip']
        server_username = server['username']
        server_password = server['password']
        ssh_client = Ssh_into_server(server_ip, server_username, server_password)
        ssh_exec(ssh_client, cmd_bind_ip.format(host=server_ip))
        ssh_exec(ssh_client, set_sharding_command.format(
            shard_config=shardserver_sharding_config.format(replica_set_name=shard_replica_set_name)))
        time.sleep(2)
        restart_mongo(ssh_client)
        allow_mongo_to_other_server(ssh_client, server_ip, LIST_all_server)
        ssh_client.close()
        print(f"Sharding Shardsvr setup complete on {server_ip}.")

    for server in LIST_shard_server:
        if server["primary"]:
            server_ip = server['ip']
            server_username = server['username']
            server_password = server['password']
            ssh_client = Ssh_into_server(server_ip, server_username, server_password)
            members = ", ".join(
                [f"{{ _id: {i}, host: '{node['ip']}:27017' }}" for i, node in enumerate(LIST_shard_server)])
            repl_set_init = f'''
                                        rs.initiate({{
                                            _id: \\"{shard_replica_set_name}\\",
                                            members: [{members}]
                                        }})
                                        '''
            ssh_exec(ssh_client, cmd_repl_set_init.format(repl_set_init=repl_set_init))
            restart_mongo(ssh_client)
            ssh_client.close()

def setup_mongos(LIST_all_server,mongos_server,mongos_port,LIST_config_server,config_replica_set_name,
                 LIST_shard_server,shard_replica_set_name,mongos_log_folder,mongos_conf_file):
    server_ip = mongos_server['ip']
    server_username = mongos_server['username']
    server_password = mongos_server['password']
    ssh_client = Ssh_into_server(server_ip, server_username, server_password)
    allow_mongos_to_other_server(ssh_client, server_ip, LIST_all_server, mongos_port)
    config_members = ", ".join(f"{node['ip']}:27017" for i, node in enumerate(LIST_config_server))
    config_servers = f"{config_replica_set_name}/{config_members}"
    ssh_exec(ssh_client, cmd_create_mongos_config.format(config_content=mongos_config.format(config_servers=
                                                                                             config_servers,
                                                                                             port=mongos_port,
                                                                                             host=server_ip,
                                                                                             log_folder=mongos_log_folder),
                                                         file_path=mongos_conf_file, ))
    ssh_exec(ssh_client, cmd_create_folder.format(folder_path=mongos_log_folder))
    ssh_exec(ssh_client, cmd_change_owner_to_mongodb.format(folder_path=mongos_log_folder))
    ssh_exec(ssh_client, cmd_write_to_mongodb.format(folder_path=mongos_log_folder))
    ssh_exec(ssh_client, cmd_mongos_config.format(file_path=mongos_conf_file))
    restart_mongo(ssh_client)
    shard_members = ", ".join(f"{node['ip']}:27017" for i, node in enumerate(LIST_shard_server))
    shard_servers = f"{shard_replica_set_name}/{shard_members}"
    ssh_exec(ssh_client, cmd_add_shard.format(host=server_ip, port=mongos_port,
                                              add_shard_config=add_shard_config.format(
                                                  shard_servers=shard_servers, )))
    ssh_client.close()