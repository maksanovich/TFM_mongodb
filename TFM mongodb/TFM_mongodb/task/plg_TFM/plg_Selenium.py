

from a0_items import *
from plg_Regex import * 
from selenium import webdriver
from fake_useragent import UserAgent
import time 
from plg_Random import * 


'''
1. Use chrome driver to find all elements of Home page - create a list for the elements ( LIST_element)

- get by id, by class, by name, create 3 separate lists and compare the lists and remove all duplicate values 

- create one list from all 3 lists combined (id, class and name)

logic 1
1. Input search query into each element of the LIST_element by id, class, name...etc, then hit submit or return button 
2. check if the returned page source is the correct search result page, containing the searched results - urls, content, keywords..etc 
3. check if the url returned is the correct url containing correct search query 

5. if none of the elements exists, or if none returned correct search results, go to next set of logic

logic 2
1. find a button to click on 
2. after clicking on the button, see if a textbox appears, and if the textbox element exists in LIST_element 
3. input search query into the textbox and submit 

4. check if the returned page source is the correct search result page, containing the searched results - urls, content, keywords..etc 
5. check if the url returned is the correct url containing correct search query 

6. If the searchbox is still not found after clicking on the search button, add this page url to list --> LIST_no_searchbox



'''

################################################################################################################################################ 


def use_Chromedriver (path_Chromedriver, url, headless_enabled, js_enabled, user_agent_enabled, proxy_ip_port):

   ### Use options to make chrome browser headless
   #options = Options()
   chrome_options = webdriver.ChromeOptions()
   
   chrome_options.add_argument("--start-maximized") #need to maximize the browser window to see all the form controls
   chrome_options.add_argument("--disable-extensions")
   chrome_options.add_argument(f'--proxy-server={proxy_ip_port}')
   
   
   if 'yes' in headless_enabled:
   
      print ('Headless enabled')
   
      chrome_options.add_argument("--headless")
      #chrome_options.add_argument("--disable-javascript") //Not working
      
   else:
   
      print ('Headless NOT enabled')
   
   
   if 'yes' in js_enabled:
   
      print ('Javascript enabled')
       
   else:
      print ('Javascript NOT enabled')
      
      prefs = {}
      prefs["webkit.webprefs.javascript_enabled"] = False
      prefs["profile.content_settings.exceptions.javascript.*.setting"] = 2
      prefs["profile.default_content_setting_values.javascript"] = 2
      prefs["profile.managed_default_content_settings.javascript"] = 2

      chrome_options.add_experimental_option("prefs", prefs)
      chrome_options.add_experimental_option( "prefs",{'profile.managed_default_content_settings.javascript': 2})
      #options.headless = True      
   
   if 'yes' in user_agent_enabled:
      
      ###Use fake user agents  
      ua = UserAgent()
      userAgent = ua.random
      chrome_options.add_argument(f'user-agent={userAgent}')
      
      print ('user agent enabled --> ' + str(userAgent))
          
   else:
      
      print ('user agent NOT enabled')

   
   Chromedriver = webdriver.Chrome(path_Chromedriver, options = chrome_options)
   Chromedriver.get(url)
   time.sleep(10)
   
   return Chromedriver
   
 

################################################################################################################################################ 
   
   
def get_proxy_list ():
   
   LIST_proxy_ip_port = []
      
   #get GOOD proxy from DB_proxies

   return LIST_proxy_ip_port
   
   
   
   
def get_page_source (path_Chromedriver, url):

   LIST_proxy_ip_port = get_proxy_list()
   random_proxy = random_select_from_list (LIST_item=LIST_proxy_ip_port)

   d_Chrome = use_Chromedriver (path_Chromedriver, url, headless_enabled='no', js_enabled='yes',user_agent_enabled ='yes', proxy_ip_port=random_proxy)   
   
   page_source = d_Chrome.page_source
   
   #print (page_source.encode('utf-8'), flush=True)
   return page_source 
   
   
#get_page_source (path_Chromedriver="../../data/raw/Chromedrivers/chromedriver-win64/chromedriver.exe", url='https://duckduckgo.com/?t=h_&q=python&ia=web')  

 

def get_ALL_links (path_Chromedriver, url):


   html_page = get_page_source (path_Chromedriver=path_Chromedriver, url=url)
   LIST_link = []
   
   soup = BeautifulSoup(html_page)

   for link in soup.findAll(attrs={'href': re.compile("http")}):
      
      http_link = link.get('href')
      print (http_link, flush=True)
      
      LIST_link.append(http_link) 

   return LIST_link      
   
   
#get_ALL_links (path_Chromedriver="../../data/raw/Chromedrivers/chromedriver-win64/chromedriver.exe", url='https://duckduckgo.com/?t=h_&q=python&ia=web', proxy_ip_port='')   
   
   
   
   
# Xpath_value = "//*[@id]"      Xpath_value = "//*[@id='query']"  
# Xpath_value = "//*[@class]"
def get_ALL_attributes_by_xpath (path_Chromedriver, url, Xpath_value):

   LIST_html_attribute = []
   
   LIST_proxy_ip_port = get_proxy_list()
   random_proxy = random_select_from_list (LIST_item=LIST_proxy_ip_port)
   
   d_Chrome = use_Chromedriver (path_Chromedriver, url, headless_enabled='no', js_enabled='no',user_agent_enabled ='yes', proxy_ip_port=random_proxy)


   try:

      #https://stackoverflow.com/questions/20244691/python-selenium-how-do-i-find-all-element-ids-on-a-page
      LIST_element = d_Chrome.find_elements(By.XPATH, Xpath_value)
      # to get names use "//*[@name]"

      for element in LIST_element:
    
         LIST_html_attribute.append('Tag: ' + str(element.tag_name).encode('ascii', 'ignore').decode('ascii') 
         + ' ID: ' + str(element.get_attribute('id')).encode('ascii', 'ignore').decode('ascii') 
         + ' Name: ' + str(element.get_attribute('name')).encode('ascii', 'ignore').decode('ascii') 
         + ' Type: ' + str(element.get_attribute('type')).encode('ascii', 'ignore').decode('ascii')
         + ' Title: ' + str(element.get_attribute('title')).encode('ascii', 'ignore').decode('ascii') 
         + ' Class: ' + str(element.get_attribute('class')).encode('ascii', 'ignore').decode('ascii') 
         + ' Placeholder: ' + str(element.get_attribute('placeholder')).encode('ascii', 'ignore').decode('ascii'))
      
      
      print ('LIST html attribute => ' + str(LIST_html_attribute))      
      return LIST_html_attribute
   
   except:
   
      print ('Elements NOT found')
  


#LIST_output = None

#LIST_output = get_ALL_attributes_by_xpath (path_Chromedriver="../../data/raw/Chromedrivers/chromedriver-win64/chromedriver.exe", url="https://timesofindia.indiatimes.com/", Xpath_value= "//*[@id]")
LIST_output = get_ALL_attributes_by_xpath (path_Chromedriver="../../data/raw/Chromedrivers/chromedriver-win64/chromedriver.exe", url="https://timesofindia.indiatimes.com/", Xpath_value= "//*[@class]") 
#LIST_output = get_ALL_attributes_by_xpath (path_Chromedriver="../../data/raw/Chromedrivers/chromedriver-win64/chromedriver.exe", url="https://timesofindia.indiatimes.com/", Xpath_value= "//*[@name]") 
#LIST_output = get_ALL_attributes_by_xpath (path_Chromedriver="../../data/raw/Chromedrivers/chromedriver-win64/chromedriver.exe", url="https://timesofindia.indiatimes.com/", Xpath_value= "//*[@type]")
#LIST_output = get_ALL_attributes_by_xpath (path_Chromedriver="../../data/raw/Chromedrivers/chromedriver-win64/chromedriver.exe", url="https://timesofindia.indiatimes.com/", Xpath_value= "//*[@aria-label]") 
 
''' 
# https://rollbar.com/blog/python-typeerror-nonetype-object-is-not-iterable/#:~:text=The%20Python%20TypeError%3A%20NoneType%20Object%20Is%20Not%20Iterable%20error%20can,over%2C%20which%20avoids%20the%20error.
if LIST_output is not None: 
 
   for x in LIST_output:

      if 'OG1TB' in x:

         print (x, flush=True)
      
      else: 
         
         pass
         
else:

   print ('LIST has NO elements')
'''

################################################################################################################################################

def input_search_bar(path_Chromedriver, url, Xpath_value, search_query, remove_after_text):
 
 
   LIST_proxy_ip_port = get_proxy_list()
   random_proxy = random_select_from_list (LIST_item=LIST_proy_ip_port)
 
   d_Chrome = use_Chromedriver (path_Chromedriver, url, headless_enabled='no', js_enabled='yes', user_agent_enabled ='yes', proxy_ip_port=random_proxy)
   print(d_Chrome.title)
   
   try:
      search_bar = d_Chrome.find_element(By.XPATH, Xpath_value)
      search_bar.clear()
   
      search_bar.send_keys(search_query)
      search_bar.send_keys(Keys.RETURN)
      
      time.sleep(5)
      
      full_url = d_Chrome.current_url
      Domain_section_query_url = remove_all_after_text (after_text=remove_after_text, text_main= full_url)
      
      print(full_url)
      print (Domain_search_query_url)
          
      return full_url, Domain_section_query_url  
   
   
   except:
   
      print('Not inputable')   
   

#input_search_bar (path_Chromedriver = "../../data/raw/Chromedrivers/chromedriver-win64/chromedriver.exe", url='https://google.com', Xpath_value = '//*[@name="q"]', search_query='python coding', remove_after_text='python', proxy_ip_port='')


####################################################################################################################################

def click_on_button (path_Chromedriver, url, Xpath_value):

   LIST_proxy_ip_port = get_proxy_list()
   random_proxy = random_select_from_list (LIST_item=LIST_proy_ip_port)

   d_Chrome = use_Chromedriver (path_Chromedriver, url, headless_enabled='no', js_enabled='yes',user_agent_enabled ='yes', proxy_ip_port =random_proxy)
    
   try:
      button = d_Chrome.find_element(By.XPATH, Xpath_value)

      button.click()
      time.sleep(5)
      
      print('Clickable')
      
      return button 
      
   except:
   
      print('Not clickable')   
   
#click_on_button (path_Chromedriver = "../../data/raw/Chromedrivers/chromedriver-win64/chromedriver.exe", url='https://timesofindia.indiatimes.com/', Xpath_value = "//*[@class='OG1TB']", proxy_ip_port='')



####################################################################################################################################
## test proxy 
######


def test_proxy (LIST_proxy, url, proxy_ip_port):

  
   random_proxy = random.choice(PROXIES)
   
   seleniumwire_options = {
      'proxy': {
         'http': f'{random_proxy}',
         'https':f' {random_proxy}',
         'verify_ssl': False, 
   },
   }


   Chromedriver = webdriver.Chrome (
      service=ChromeService(ChromeDriverManager().install()),
      seleniumwire_options=seleniumwire_options
   )

   Chromedriver.visit()   
   

proxies = ['http://103.21.244.160:80', 'http://132.226.118.106:8080' ]
#test_proxy (LIST_proxy, url='https://timesofindia.indiatimes.com/')



def test_proxy_1 (path_Chromedriver, proxy):

   chrome_options = webdriver.ChromeOptions()
   #chrome_options.add_argument('--proxy-server=%s' % PROXY)
   chrome_options.add_argument(f'--proxy-server={PROXY}')
   
   chrome_options.add_argument("ignore-certificate-errors")
    
   chrome = webdriver.Chrome(path_Chromedriver, options=chrome_options)
   #chrome.get("https://www.ipchicken.com/")
   chrome.get("https://api.ipify.org/?format=json")

   time.sleep(20)


#test_proxy_1 (path_Chromedriver="../../data/raw/Chromedrivers/chromedriver-win64/chromedriver.exe", proxy = "11.456.448.110:8080" #  HOST:PORT)



############################################################################
## Test list of elements 


#https://stackoverflow.com/questions/52706901/how-to-assert-the-text-box-is-enabled-or-disabled
#https://pythonexamples.org/python-selenium-check-if-input-text-field-exists/

#https://www.browserstack.com/guide/python-selenium-to-run-web-automation-test

def input_search_bar_LIST (path_Chromedriver, url, Xpath_value, search_query):

   d_Chrome = get_HTML_attributes_by_xpath (path_Chromedriver, url, Xpath_value)[1]
   LIST_attribute = get_HTML_attributes_by_xpath (path_Chromedriver, url, Xpath_value)[0]
   
   for attribute in LIST_attribute:
   
      #get the ID only 
      ID = remove_all_before_and_after_texts (text_1 = 'ID:', text_2='Name:', text = attribute)
   
      # Check if value in input text is empty
      try:
         
         id_element =  d_Chrome.find_elements(By.XPATH, Xpath_v = "//*[@id=" + ID + "]" )
         #print("Input text field exists.")
      
         id_element.clear()
      
         id_element.send_keys(search_query)

         id_element.submit()
         time.sleep(5)
      
         full_url = Chromedriver.current_url
         print(full_url)
      
         Domain_search_query_url = remove_all_after_text (after_text=search_query, text_main= full_url)
      
         print ('dsqu = ' + Domain_search_query_url)
      
            
      except (NoSuchElementException, WebDriverException):
   
         print("Input textbox NOT exists.")

   # Close the driver
   #Chromedriver.quit()
   
   
#input_search_textbox (path_Chromedriver = "../../data/raw/Chromedrivers/chromedriver-win64/chromedriver.exe", url="https://timesofindia.indiatimes.com/", Xpath_value= "//*[@id]", search_query = 'orange')   
#input_search_textbox (path_Chromedriver = "../../data/raw/Chromedrivers/chromedriver-win64/chromedriver.exe", url="https://google.com/", Xpath_value="//*[@name='q']")



   
def click_on_button_LIST ():

   d_Chrome = get_HTML_attributes_by_xpath (path_Chromedriver, url, Xpath_value)[1]
   LIST_attribute = get_HTML_attributes_by_xpath (path_Chromedriver, url, Xpath_value)[0]
   
   pass




def get_page_source_URLS ():

   pass