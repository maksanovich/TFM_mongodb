
from a0_items import * 

# pip install requests-html
from requests_html import HTMLSession



def get_proxy_list ():
   
   LIST_proxy_ip_port = []
      
   #get GOOD proxy from DB_proxies
   

   return LIST_proxy_ip_port
   


#with random proxy
def get_url_status_code (url):

   LIST_proxy_ip_port = get_proxy_list()
   random_proxy = random.choice(LIST_proxy_ip_port + [''])

   x = requests.get(url, proxies=random_proxy)
   
   status_code = x.status_code
   #print(x.status_code)
      
   return status_code


#print(get_url_status_code (url='https://w3schools.com'))



#https://www.scrapingbee.com/blog/python-requests-proxy/
def request_url_with_session (url):

   session = requests.Session()

   LIST_proxy_ip_port = get_proxy_list()
   random_proxy = random.choice(LIST_proxy_ip_port + [''])

   session.proxies = random_proxy

   response = session.get(url)
   print (response)


request_url_with_session (url='https://w3schools.com')




# https://stackoverflow.com/questions/26393231/using-python-requests-with-javascript-pages
def get_page_with_JS ():

   session = HTMLSession()

   r = session.get('https://duckduckgo.com/?va=k&t=ht&q=top+RSS+feeds+china&ia=web')

   page = r.html.render()  # this call executes the js in the page

   print (page)

#get_page_with_JS ()



def get_ALL_urls (url):

   try:
   
      reqs = requests.get(url)
     
      soup = BeautifulSoup(reqs.text, 'html.parser')
 
      LIST_url = []
   
      for link in soup.findAll('a'):
   
         #print(link.get('href'))      
         LIST_url.append(link.get('href'))
         
      return LIST_url   
      
   except requests.exceptions.RequestException as errex: 
      print("Exception request") 



      
'''
LIST_url = get_ALL_urls (url= 'https://rss.feedspot.com/algeria_rss_feeds/')

for x in LIST_url:

   if 'rss' in x or 'feed' in x and 'http' in x and 'feedspot' not in x:
   
      print (x)
      
   else:
   
      print ('rss NOT in')
'''


def get_Image_urls (url):

   LIST_image_url = []

   response = requests.get(url)
   soup = BeautifulSoup(response.content, "html.parser")

   for img in soup.findAll('img'):
      
      src = img.get("src")
      
      if src:
      
         # resolve any relative urls to absolute urls using base URL
         src = requests.compat.urljoin(url, src)
         #print(src) 
         
         LIST_image_url.append (src)

   return LIST_image_url         


#print (get_Image_urls ('https://en.wikipedia.org/wiki/Main_Page'))




def create_url_with_params (url, params):
 
   r = requests.get(url, params)
   url_with_params = r.url 
   print(url_with_params)
   
   return url_with_params
   
   
# should only have TFM_Task, TFM_task_action parameters, 
# Other values should use TFMdata1, 2..3 as value keys, so that PHP only needs to GET TFM_task & TFM_task variables 
parameters = {'TFM_task': 'MSQM_Country_language', 
              'TFM_task_action': 'Folders_CREATE_TFMdata1_/data/raw/_TFMdata2_xyzfile.db_TFMdata2_helloFILE.txt', 
              }

#print (create_url_with_params (url='https://httpbin.org/get', params=parameters))