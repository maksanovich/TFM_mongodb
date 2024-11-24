
import requests


def get_request ():


   #x = requests.get('http://173.208.166.82/TEST_CODE/test_PHP.php?first=2&second=2&third=9')
   #x = requests.get('http://173.208.166.82/TEST_CODE/get_IP.php')
   x = requests.get('http://173.208.166.82/TEST_CODE/py_245.py')

   print("get request => ", x.text)
   

#get_request ()   
   

### Python request automatically encodes the url sent to the browser (no need to encode it before posting it using request)

url = 'http://localhost/TEST_CODE/a2_test_API.php/run?LOG_tfm_task_request=one_unique&TFM_task_action=func_1#1conn_str=hello1#2db_name=hello2#3name:name,age:age,address:address}'

def post_request ():

   x = requests.post(url)

   print("post request => ", x.text) 


post_request ()