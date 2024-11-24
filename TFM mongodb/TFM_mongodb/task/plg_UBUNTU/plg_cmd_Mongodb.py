cmd_install_mongodb = [
    "sudo apt-get install gnupg curl",
    "curl -fsSL https://www.mongodb.org/static/pgp/server-7.0.asc | sudo gpg -o /usr/share/keyrings/mongodb-server-7.0.gpg --dearmor",
    "echo \"deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-7.0.gpg ] https://repo.mongodb.org/apt/ubuntu $(lsb_release -sc)/mongodb-org/7.0 multiverse\" | sudo tee /etc/apt/sources.list.d/mongodb-org-7.0.list",
    "sudo apt-get update",
    "sudo apt-get install -y mongodb-org",
    "sudo systemctl start mongod",
    "sudo systemctl enable mongod"
]
cmd_remove_mongodb = [
    "sudo service mongod stop",
    "sudo apt-get purge mongodb-org* -y",
    "sudo rm -r /var/log/mongodb /var/lib/mongodb"
]
cmd_bind_ip = "sudo sed -i 's/^  bindIp: .*/  bindIp: 127.0.0.1 ,{host}/' /etc/mongod.conf"
# cmd_set_host_name = "mongosh --host {host}"
cmd_delete_mongo_sock = "sudo rm -rf /tmp/mongodb-27017.sock"
cmd_restart_mongod = "sudo systemctl restart mongod"
cmd_create_database = 'mongosh --eval "db = connect(\'mongodb://localhost:27017/{db_name}\'); db.createCollection(\'init_collection\');"'
cmd_delete_database = 'mongosh --eval "db = connect(\'mongodb://localhost:27017/{db_name}\'); db.dropDatabase();"'
cmd_dump_database = 'mongodump --db {db_name} --out {backup_path}'
cmd_restore_database = 'mongorestore --nsInclude={db_name}.* {backup_path}'
cmd_delete_backup = 'sudo rm -r {backup_path}'

#replication
cmd_allow_ip_to_mongo = "sudo ufw allow from {remote_host} to any port 27017"
cmd_bind_ip_for_replication = 'mongod --bind_ip {hosts}'
cmd_set_replication = 'mongod --replSet "{replication_name}" --bind_ip {hosts}'
replica_set_config = '''
replication:
  replSetName: "{replica_set_name}"
                            '''
set_replica_command = "echo '{replica_set_config}' | sudo tee -a /etc/mongod.conf"
cmd_repl_set_init = 'mongosh --eval "{repl_set_init}"'
cmd_allow_ssh = "sudo ufw allow 22"
cmd_deny_mongo_port = "sudo ufw deny 27017"
cmd_delete_deny_mongo_port = "sudo ufw delete deny 27017"
cmd_ufw_enable = "sudo ufw --force enable"

#sharding
configserver_sharding_config = '''
sharding:
  clusterRole: configsvr
replication:
  replSetName: "{replica_set_name}"
                            '''

shardserver_sharding_config = '''
sharding:
  clusterRole: shardsvr
replication:
  replSetName: "{replica_set_name}"
                            '''

set_sharding_command = "echo '{shard_config}' | sudo tee -a /etc/mongod.conf"

mongos_config = '''sharding:
  configDB: {config_servers}
net:
  port: {port}
  bindIp: localhost,{host}
systemLog:
  destination: file
  logAppend: true
  path: {log_folder}mongos.log
processManagement:
  fork: true'''

cmd_create_mongos_config = 'echo "{config_content}" | sudo tee {file_path}'
cmd_mongos_config = "mongos --config {file_path}"
cmd_create_folder = "sudo mkdir {folder_path}"
cmd_change_owner_to_mongodb = "sudo chown -R mongodb:mongodb {folder_path}"
cmd_write_to_mongodb = "sudo chmod -R 775 {folder_path}"
add_shard_config = '"sh.addShard(\\"{shard_servers}\\")"'
cmd_add_shard = 'mongosh --port {port} --eval {add_shard_config}'
cmd_allow_ip_to_mongos = "sudo ufw allow from {remote_host} to any port {port}"
cmd_deny_mongos_port = "sudo ufw deny {port}"
cmd_delete_deny_mongos_port = "sudo ufw delete deny {port}"