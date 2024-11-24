
###################################################
###### System hardware info 
###################################################

##Speces - CPU
cmd_CPU_0 = 'lscpu'  #General CPU specs 
cmd_CPU_1 ='cat /proc/cpuinfo' #Each individual cpu core specs

##Specs - RAM
cmd_RAM_0 = 'sudo lshw -short -C memory' #RAM list summary
cmd_RAM_1 = 'dmidecode --type memory'   #Full RAM specs 
cmd_RAM_2 = 'grep MemTotal /proc/meminfo' #Total memory
cmd_RAM_3 = 'awk "'"/MemTotal/ {print $2}"'" /proc/meminfo'  #Total memory 

##Specs - DISK
cmd_DISK_0 = 'fdisk -l | grep Disk' #Total hard disk space 
cmd_DISK_1 ='lshw -short -C disk' #Disk specs summary
cmd_DISK_2 = 'lsblk'

##Specs - OS
cmd_OS_0 = 'cat /etc/os-release' #Operating system specs

##Specs - HOST
cmd_HOST_0 = 'hostnamectl' #host machine info

##Specs - SOFTWARE
cmd_SOFT_0 = 'sudo yum list installed | wc -l'  #count the software installed
cmd_SOFT_1 = 'sudo yum list installed'  #list all software installed --> https://www.cyberciti.biz/faq/check-list-installed-packages-in-centos-linux/

##Usage - CPU
cmd_CPU_use_0 = 'top -b -n1'    #using 'top' wont work --> https://stackoverflow.com/questions/25101619/reading-output-of-top-command-using-paramiko
cmd_CPU_use_1 = 'ps -eo %cpu,comm --sort=-%mem | head -n 10'

##Usage - RAM
cmd_RAM_use_0 = 'free -h'   #Total free and used memory 
cmd_RAM_use_1 = 'ps -eo %mem,comm --sort=-%mem | head -n 10'  #TOP 10 MEMORY-CONSUMING PROCESSES

cmd_CPU_RAM_use_0 = 'ps -eo %cpu,%mem,comm --sort=-%mem | head -n 10' 

##Usage - DISK --> https://www.tecmint.com/find-top-large-directories-and-files-sizes-in-linux/
cmd_DISK_use_0 = 'df -H --output=source,size,used,avail'

cmd_DISK_use_1 = 'du -a /etc/ | sort -n -r | head -n 10' #TOP 10 DISK-CONSUMING PROCESSES

cmd_DISK_use_2 = 'df -h /' #total disk of the root directory 

#cmd_DISK_use_3 = 'df -h --output='size','pcent' /' #https://linuxiac.com/check-disk-space-linux/

cmd_DISK_use_4 = 'df -h -t ext4'  #https://www.howtogeek.com/409611/how-to-view-free-disk-space-and-disk-usage-from-the-linux-terminal/

###### SYSTEM & URL #####

##System - PING
cmd_Sys_0 = 'ping -c 10 ' #must have a space after ping. server_ip is a variable containing ip

##System - Uptime 
cmd_Sys_1 = 'uptime' #How long the machine has been up & running 


###################################################
###### Linux packages 
###################################################

# list last installed packages
cmd_installed_pkg = 'rpm -qa --last'

update_packages="yum -y update"


###################################################
###### 7 zip  
###################################################

### 7zip for file zip -- https://elearning.wsldp.com/pcmagazine/extract-7zip-centos-7/
cmd_install_p7zip = 'yes | sudo yum install p7zip'

#https://unix.stackexchange.com/questions/470266/how-to-locate-a-package-installed-by-yum/470458
cmd_p7zip_install_path = 'rpm -q --filesbypkg p7zip'
cmd_search_7zip_version = 'yum search 7zip'
cmd_info_7zip_version = 'yum info 7zip'

cmd_remove_p7zip = 'yes | yum remove p7zip'
cmd_update_after_remove_7zip = 'yum update'

cmd_create_p7zip_TFM = ''


###################################################
###### Epel release  
###################################################

cmd_install_epel_release_for_7zip = 'yes | sudo yum install epel-release' # yes | will ansewr YES to the prompt. yes no | ansewr NO to the prompt.
cmd_import_epel_gpg_key = 'rpm --import http://download.fedoraproject.org/pub/epel/RPM-GPG-KEY-EPEL-6'

cmd_search_epel_version = 'yum search epel-release'
cmd_epel_install_path = 'rpm -q --filesbypkg epel-release'

#Check installed package versions -- https://www.tecmint.com/install-epel-repository-on-centos/
cmd_info_epel_version = 'yum info epel-release'
cmd_remove_epel_release = 'yes | yum remove epel-release' # yes | will ansewr YES to the prompt. yes no | ansewr NO to the prompt.
cmd_update_after_remove_epel_release = 'yes | yum update' # yes | will ansewr YES to the prompt. yes no | ansewr NO to the prompt.



###################################################
###### Iptables 
###################################################

iptables_install="$SUDO $INSTALLER -y install iptables iptables-persistent"
ufw_install_for_centos_1="$SUDO $INSTALLER -y install epel-release"
ufw_install="$SUDO $INSTALLER -y install ufw"
iptables_version="iptables -V"
iptables_ufw_iptables_enable="$SUDO ufw --force enable"
iptables_ufw_iptables_disable="$SUDO ufw disable"
iptables_ufw_iptables_status="$SUDO ufw status"


###################################################
###### Lsyncd
###################################################

cmd_install_rsync="yum install -y rsync"
cmd_lsyncd_install="yum -y install lsyncd"
cmd_install_sshclients="yum -y install openssh-clients"
cmd_rm_id_rsa='rm -f /root/.ssh/id_rsa'
cmd_ssh_keygen_create_keys='ssh-keygen -b 2048 -t rsa -f /root/.ssh/id_rsa -q -N ""'
cmd_start_lsyncd="systemctl start lsyncd"
cmd_stop_lsyncd="systemctl stop lsyncd"
cmd_enable_lsyncd="systemctl enable lsyncd"


###################################################
###### Rysnc 
###################################################

rsync_install="$SUDO $INSTALLER -y install rsync"
rsync_version="rsync --version"
rsync_start="$SUDO service rsync start"
rsync_stop="$SUDO service rsync stop"
rsync_status="$SUDO service rsync status"
rsync_restart="$SUDO service rsync restart"
rsync_mkdir_www="$SUDO mkdir -p /tmp/var/www"
rsync_local_backup="$SUDO rsync -avn /var/www /tmp/var/www"
rsync_remote_backup= ''
#rsync_grep_www="$SUDO grep -nri "/tmp/var/www" /etc/crontab"
rsync_mode_change="$SUDO chmod 0666 /etc/crontab"
rsync_mode_revert="$SUDO chmod 0644 /etc/crontab"
rsync_copy_rsyncd_conf="$SUDO cp /usr/share/doc/rsync/examples/rsyncd.conf /etc"


###################################################
###### Docker
###################################################

cmd_check_install_or_update_docker = ''' if [ -x "$(command -v docker)" ]; then
    echo "Update docker"
    # command
else
    echo "Install docker"
    # command
fi '''

docker_help ='docker --help'
docker_install = ''
docker_container_list = 'docker ps'
docker_version = 'docker version'
docker_status = 'service docker status'
docker_start =''
docker_stop = ''
docker_restart =''

cmd_Docker_install_path = 'rpm -q --filesbypkg docker' #this may not work in some situtations 

#remove docker to install a clean copy of docker 
cmd_remove_docker = '''yum remove docker \
                  docker-client \
                  docker-client-latest \
                  docker-common \
                  docker-latest \
                  docker-latest-logrotate \
                  docker-logrotate \
                  docker-engine'''



cmd_install_docker = ''

# Multi-line bash script 
cmd_Docker_running_or_not = '''if curl -s --unix-socket /var/run/docker.sock http/_ping 2>&1 >/dev/null
then
  echo "Running"
else
  echo "NOT running"
fi '''

cmd_Docker_status = 'systemctl status docker' #To check if Docker engine is running 
cmd_start_docker_engine = 'systemctl start docker'
cmd_docker_version = 'docker version'

#Check if docker is installed, if so update it 
cmd_check_install_or_update_docker = ''' if [ -x "$(command -v docker)" ]; then
    echo "Update docker"
    # command
else
    echo "Install docker"
    # command
fi '''

cmd_install_docker_engine = ''


# ####################### Docker compose ####################################
cmd_docker_compose_version = 'docker-compose version'

cmd_install_docker_compose = ''

cmd_stop_docker_compose ='docker-compose stop'
cmd_start_docker_compose = 'docker-compose up -d'



###################################################
###### Php
###################################################









###################################################
###### Joomla 
###################################################

#https://www.digitalocean.com/community/tutorials/how-to-install-joomla-on-a-virtual-server-running-centos-6

cmd_install_wget_unzip="yum install -y wget unzip"
cmd_download_joomla="wget -P /tmp/ https://downloads.joomla.org/cms/joomla3/3-9-25/Joomla_3-9-25-Stable-Full_Package.zip"
cmd_unzip_joomla="unzip -o /tmp/Joomla_3-9-25-Stable-Full_Package.zip -d /var/www/html/"
cmd_chown_html_dir="chown -R apache:apache /var/www/html/*"
cmd_chmod_html_dir="chmod -R 775 /var/www/html/*"
cmd_unzip_backup="unzip -o /tmp/joomla.zip -d /var/www/html/"
joomla_owner_permission_joomla="$SUDO chown -R www-data:www-data /var/www/html/joomla"
joomla_mode_changes_joomla="$SUDO chmod -R 755 /var/www/html/joomla"
#joomla_copy_file="$SUDO cp /tmp/$OS_TYPE/joomla.conf /etc/apache2/sites-available"
#joomla_enable_virtualhost_1="$SUDO a2ensite joomla.conf"
#joomla_enable_virtualhost_2="$SUDO a2enmod rewrite"


cmd_joomla_file_list = 'find / -name '"'joomla'"' '
cmd_admintools_file_list = 'find / -name '"'admintools'"' '
cmd_rsfirewall_file_list = 'find / -name '"'rsfirewall'"' '


###################################################
###### Apache - Httpd 
###################################################

cmd_httpd_install="yum install -y httpd"
cmd_httpd_stop="systemctl stop httpd"
cmd_httpd_enable="systemctl enable --now httpd"
cmd_http_firewall="firewall-cmd --permanent --zone=public --add-service=http"
cmd_https_firewall="firewall-cmd --permanent --zone=public --add-service=https"
cmd_php_chown="chown -R root:apache /var/lib/php/*"
cmd_restart_php="systemctl restart php-fpm.service"
cmd_install_epel="yum install -y epel-release yum-utils"
cmd_install_remi="yum -y install https://rpms.remirepo.net/enterprise/remi-release-7.rpm"
cmd_remi_disable="yum-config-manager --disable remi-php54"
cmd_remi_enable="yum-config-manager --enable remi-php74"
cmd_install_php_tools="yum -y update && yum -y install php-fpm php-cli php-gd php-opcache php-mysqlnd php-json php-mcrypt php-xml php-curl mod_php"


###################################################
###### Maria DB - Galera cluster 
###################################################

cmd_mariadb_install="yum install -y MariaDB-server MariaDB-client galera"
cmd_mariadb_start="systemctl start mariadb"
cmd_mariadb_stop="systemctl stop mariadb"
cmd_mariadb_restart="systemctl restart mariadb"
cmd_mariadb_enable="systemctl enable mariadb"
cmd_galera_start="galera_new_cluster"
cmd_firewalld_add_3306__tcp_port="firewall-cmd --permanent --zone=public --add-port=3306/tcp"
cmd_firewalld_add_4567__tcp_port="firewall-cmd --permanent --zone=public --add-port=4567/tcp"
cmd_firewalld_add_4568__tcp_port="firewall-cmd --permanent --zone=public --add-port=4568/tcp"
cmd_firewalld_add_4444__tcp_port="firewall-cmd --permanent --zone=public --add-port=4444/tcp"
cmd_firewalld_add_4567__udp_port="firewall-cmd --permanent --zone=public --add-port=4567/udp"
cmd_update_galera_node_status="sed -i 's/safe_to_bootstrap: 0/safe_to_bootstrap: 1/' /var/lib/mysql/grastate.dat"


cmd_firewalld_add_3306__tcp_port = (
    "firewall-cmd --permanent --zone=public --add-port=3306/tcp"
)
cmd_firewalld_add_4567__tcp_port = (
    "firewall-cmd --permanent --zone=public --add-port=4567/tcp"
)
cmd_firewalld_add_4568__tcp_port = (
    "firewall-cmd --permanent --zone=public --add-port=4568/tcp"
)
cmd_firewalld_add_4444__tcp_port = (
    "firewall-cmd --permanent --zone=public --add-port=4444/tcp"
)
cmd_firewalld_add_4567__udp_port = (
    "firewall-cmd --permanent --zone=public --add-port=4567/udp"
)
cmd_update_galera_node_status = (
    "sed -i 's/safe_to_bootstrap: 0/safe_to_bootstrap: 1/' /var/lib/mysql/grastate.dat"
)


###################################################
###### TiDB
###################################################

cmd_install_tidb_server = "yum install tidb tidb-client tidb-ctl -y"
cmd_install_pd = "yum install pd -y"
cmd_install_tikv = "yum install tikv -y"

cmd_make_cluster_yaml="""
echo "
# For more information about the format of the tiup cluster topology file, consult
# https://docs.pingcap.com/tidb/stable/production-deployment-using-tiup#step-3-initialize-cluster-topology-file

# # Global variables are applied to all deployments and used as the default value of
# # the deployments if a specific deployment value is missing.
global:
  # # The OS user who runs the tidb cluster.
  user: \"tidb\"
  # # SSH port of servers in the managed cluster.
  ssh_port: 22
  # # Storage directory for cluster deployment files, startup scripts, and configuration files.
  deploy_dir: \"/tidb-deploy\"
  # # TiDB Cluster data storage directory
  data_dir: \"/tidb-data\"
  # # Supported values: \"amd64\", \"arm64\" (default: \"amd64\")
  arch: \"amd64\"

pd_servers:
  - host: 172.20.0.2

tidb_servers:
  - host: 172.20.0.3

tikv_servers:
  - host: 172.20.0.4

monitoring_servers:
  - host: 172.20.0.5

grafana_servers:
  - host: 172.20.0.6
" > cluster.yaml
"""


cmd_start_tidb_server = "tidb-server --config=tidb-server.toml"
cmd_start_pd_server = "pd-server --config=pd.toml"
cmd_start_tikv_server= "tikv-server --config=tikv.toml"

cmd_enable_tidb_server = "systemctl enable tidb; systemctl start tidb"
cmd_enable_pd_server = "tiup cluster start pd --config=pd.toml"
cmd_enable_tikv_server = "tiup cluster start tikv --config=tikv.toml"

# node status
cmd_update_tidb_node_status = (
    "sed -i 's/status: 0/status: 1/' /var/lib/tidb/tidbstate.dat"
)

## Firewall##

# fire_wall_add_pd_port = f"firewall-cmd --zone=public --add-port={server.pd_port}/tcp --permanent"
# fire_wall_add_tikv_port = f"firewall-cmd --zone=public --add-port={server.tikv_port}/tcp --permanent"
# fire_wall_add_tidb_port = f"firewall-cmd --zone=public --add-port={server.tidb_port}/tcp --permanent"
# fire_wall_add_tispark_port = f"firewall-cmd --zone=public --add-port={server.tispark_port}/tcp --permanent"
# fire_wall_reload = "firewall-cmd --reload"


# Set up TiDB cluster
cmd_setup_tidb_cluster = "tidb-ctl create-cluster"

# Stop TiDB
cmd_stop_tidb = "systemctl stop tidb"

# Configure TiDB firewall
cmd_configure_tidb_firewall_4000 = "firewall-cmd --permanent --add-port=4000/tcp"
cmd_configure_tidb_firewall_10080 = "firewall-cmd --permanent --add-port=10080/tcp"
cmd_reload_firewall = "firewall-cmd --reload"

cmd_install_firewall = "yum install firewalld -y"
#cmd_tidb_configure_firewall = "ufw allow from 0.0.0.0 to any port 4000"



###################################################
###### Keepalived
###################################################

cmd_keepalive_install="yum -y install keepalived"
cmd_keepalive_stop="systemctl stop keepalived"
cmd_keepalive_enable="systemctl enable --now keepalived"
cmd_keepalive_conf_backup="mv /etc/keepalived/keepalived.conf /etc/keepalived/keepalived.conf.bak"


###################################################
###### Fail2ban 
###################################################

cmd_install_Fail2ban = '''yum -y install fail2ban fail2ban-systemd
yum update -y selinux-policy*
'''
cmd_configure_fail2ban = '''cp -pf /etc/fail2ban/jail.conf /etc/fail2ban/jail.local
sed -i "/#ignoreip =/s/^#//g" /etc/fail2ban/jail.local
sed -i "285i enabled = true" /etc/fail2ban/jail.local
sed -i "286i #action = firewallcmd-ipset" /etc/fail2ban/jail.local
sed -i "287i maxretry = 5" /etc/fail2ban/jail.local
sed -i "288i bantime = 86400" /etc/fail2ban/jail.local
'''
cmd_enable_fail2ban = 'systemctl enable fail2ban && systemctl start fail2ban'
cmd_remove_fail2ban = '''systemctl stop fail2ban && systemctl disable fail2ban
rpm -e --nodeps `rpm -aq | grep -i fail2ban`
'''
fail2ban_restart_cmd = 'systemctl restart fail2ban'



###################################################
###### ClamAV
###################################################

cmd_install_ClamAV = 'yum -y install clamav-server clamav-data clamav-update clamav-filesystem clamav clamav-scanner-systemd clamav-devel clamav-lib clamav-server-systemd'
cmd_uninstall_ClamAV = '''systemctl stop clamd@scan && systemctl disable clamd@scan
rpm -e --nodeps `rpm -aq | grep -i clamav`
'''
clamav_selinux_config="setsebool -P antivirus_can_scan_system 1 && setsebool -P clamd_use_jit 1"
clamav_config='''sed -i -e 's/^Example/#Example/' /etc/clamd.d/scan.conf
sed -i "/clamd.sock/s/^#//g" /etc/clamd.d/scan.conf
sed -i -e "s/^Example/#Example/" /etc/freshclam.conf
freshclam
'''
clamav_enable_cmd="systemctl start clamd@scan && systemctl enable clamd@scan"
clamav_scan="freshclam && clamscan -r /"
clamav_restart_cmd="systemctl restart clamd@scan"


###################################################
###### Lynis audit
###################################################

cmd_install_Lynis = 'yum -y install lynis'
cmd_start_Lynis = 'lynis audit system'
cmd_stop_Lynis = 'killall -9 lynis'
cmd_remove_Lynis = 'rpm -e --nodeps `rpm -aq | grep -i lynis'


###################################################
###### Hosts allow deny 
###################################################

ssh_touch_files = 'touch /etc/hosts.{allow,deny}'
ssh_add_to_allow_list = 'echo "sshd: {}" >> /etc/hosts.allow'

#ssh_deny_hosts = 'echo "sshd: ALL" >> /etc/hosts.deny' #Deny ALL hosts 
ssh_deny_hosts = 'echo "sshd: " >> /etc/hosts.deny'


###################################################
###### Inotify
###################################################

cmd_install_Inotify = '''
yum makecache
yum -y install inotify-tools
'''
cmd_remove_Inotify = 'yum -y remove inotify-tools'


###################################################
###### Rootkit hunter
###################################################

cmd_download_RKhunter = '''wget http://downloads.sourceforge.net/project/rkhunter/rkhunter/1.4.6/rkhunter-1.4.6.tar.gz
tar zxvf rkhunter-1.4.6.tar.gz
'''
cmd_install_RKhunter = 'cd rkhunter-1.4.6 && bash installer.sh --layout default --install'
cmd_update_RKhunter = '/usr/local/bin/rkhunter --update && /usr/local/bin/rkhunter --propupd'
cmd_run_RKhunter = 'rkhunter --check --skip-keypress'
cmd_remove_RKhunter = 'rm -rf /usr/local/bin/rkhunter && rm -rf /root/rkhunter-1.4.6*'

# ModEvasive
cmd_install_ModEvasive = 'yum install mod_evasive -y'
cmd_remove_ModEvasive = '''yum -y remove mod_evasive
systemctl restart httpd
'''


###################################################
###### Modsecurity
###################################################

cmd_install_ModSecurity = 'yum install mod_security -y'
cmd_install_rule_set = 'yum -y install mod_security_crs'
cmd_remove_ModSecurity = '''yum -y remove mod_security
systemctl restart httpd
'''
apache_reload_cmd = 'systemctl reload httpd'


###################################################
###### Haproxy
###################################################

cmd_install_haproxy="yum -y install haproxy"
cmd_chmod="cd /etc/firewalld/services && restorecon haproxy.xml && chmod 640 haproxy.xml"
cmd_haproxy_add_service="firewall-cmd --permanent --add-service=haproxy"
cmd_firewalld_reload="firewall-cmd --reload"
cmd_setsebool_1="setsebool -P haproxy_connect_any 1"
cmd_systemctl_status="systemctl status haproxy.service -l --no-pager"
cmd_haproxy_stop="systemctl stop haproxy"
cmd_haproxy_enable="systemctl enable --now haproxy"


###################################################
###### SYSTAT
###################################################

cmd_SYSSTAT_install_path = 'rpm -q --filesbypkg sysstat'
cmd_SYSSTAT_file_list = 'find / -name '"'sysstat'"' '

cmd_install_SYSSTAT = 'yum -y install sysstat'
cmd_enable_SYSSTAT = ''
cmd_start_SYSSTAT =''


###################################################
###### ModEvasive
###################################################

cmd_install_ModEvasive = 'yum install mod_evasive -y'
cmd_remove_ModEvasive = '''yum -y remove mod_evasive
systemctl restart httpd
'''


###################################################
###### Mailu
###################################################

cmd_show_Mailu_file_list = 'find / -type d -name mailu'

cmd_show_Docker_Mailu_files = 'docker container ls' #loop to see if if 'mailu' in the text 
cmd_install_Docker_Mailu = ''

cmd_start_docker_compose_Mailu = 'docker-compose -p mailu up -d'

cmd_mailu_create_admin_user = ' docker-compose -p mailu exec -T admin flask mailu admin $MAIL_SERVER_AMDIN_USR $MAIL_SERVER_DOMAIN "$MAIL_SERVER_AMDIN_PASS" '

