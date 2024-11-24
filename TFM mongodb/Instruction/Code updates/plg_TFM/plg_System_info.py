

from a0_items import * 


import psutil 
import datetime

###################################################################################################
### plugins - Check hardware specs
####################################################################################################

# https://www.juniper.net/documentation/us/en/software/junos/automation-scripting/topics/task/junos-python-modules-psutil-module.html
### *** CPU FUNCTIONS ***

def CPU_count ():
   
   count_CPU = psutil.cpu_count()
   # Number of logical CPUs in the system
   print ("psutil.cpu_count() = {0}".format(count_CPU))
   
   return count_CPU

#CPU_count ()



### *** DISK FUNCTIONS ***

def DISK_partitions ():

   # List of named tuples containing all mounted disk partitions
   dparts = psutil.disk_partitions()
   print("psutil.disk_partitions() = {0}".format(dparts))
   
   return dparts


def DISK_usage ():

   # Disk usage statistics   
   du = psutil.disk_usage('/')
   print("psutil.disk_usage('/') = {0}".format(du))
   
   return du


### *** MEMORY FUNCTIONS ***

def get_sys_memory ():

# System memory usage statistics
   mem = psutil.virtual_memory()
   print("psutil.virtual_memory() = {0}".format(mem))

   THRESHOLD = 100 * 1024 * 1024  # 100MB
   if mem.available <= THRESHOLD:
      print("warning, available memory below threshold")
      
   return mem


#get_sys_memory ()




### *** PROCESS FUNCTIONS ***

def get_process_id ():

   # List of current running process IDs.
   pids = psutil.pids()
   print("psutil.pids() = {0}".format(pids))
   
   return pids

#get_process_id ()




def get_process_id_name ():

   # Check whether the given PID exists in the current process list.
   for proc in psutil.process_iter():
   
      try:
      
         pinfo = proc.as_dict(attrs=['pid', 'name'])
         
      except psutil.NoSuchProcess:
      
         pass
         
      else:
      
        print(pinfo)


### *** SYSTEM INFORMATION FUNCTIONS ***

def get_sys_boot_time ():

   # System boot time expressed in seconds since the epoch
   boot_time = psutil.boot_time()
   print("psutil.boot_time() = {0}".format(boot_time))

   # System boot time converted to human readable format
   print(datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S"))
   
   return boot_time



def get_sys_users ():

   # Users currently connected on the system
   users = psutil.users()
   print("psutil.users() = {0}".format(users))
   
   return users

#get_sys_users ()