

from a0_items import *


   
# get free proxies --> https://thepythoncode.com/article/using-proxies-using-requests-in-python
#Code NOT working 



#https://stackoverflow.com/questions/55872164/how-to-rotate-proxies-on-a-python-requests
import requests
from requests_ip_rotator import ApiGateway, EXTRA_REGIONS

def AWS_proxy ():

   gateway = ApiGateway("https://www.transfermarkt.es")
   gateway.start()

   session = requests.Session()
   session.mount("https://www.transfermarkt.es", gateway)

   response = session.get("https://www.transfermarkt.es/jadon-sancho/profil/spieler/your_id")
   print(response.status_code)

   # Only run this line if you are no longer going to run the script, as it takes longer to boot up again next time.
   gateway.shutdown() 
   
   
   


