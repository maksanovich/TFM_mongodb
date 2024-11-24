

from a0_items import * 

import subprocess

###################################################################################################
### plugins - Install Python modules by code
####################################################################################################

def install_module_OS (module_name):

   os.system("pip install " + module_name)


#install_module_OS (module_name="psutil")




def install_module_SUBPROCESS (module_name):

   subprocess.check_call([sys.executable, "-m", "pip", "install", module_name])
   
   
#install_module_SUBPROCESS (module_name="psutil")   