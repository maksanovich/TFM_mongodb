

from a0_items import *
from plg_Regex import * 

 
def get_ALL_urls (url):
 
   reqs = requests.get(url)
   soup = BeautifulSoup(reqs.text, 'html.parser')
 
   LIST_url = []

   for link in soup.find_all('a'):

      #print(link.get('href'))
      LIST_url.append (link.get('href'))
      
   return LIST_url
    

# print (get_ALL_urls (url= 'https://www.geeksforgeeks.org/'))



def get_domain_from_url (url):

   t = urlparse(url).netloc
   
   domain = ('.'.join(t.split('.')[-2:]))
   
   return domain
   

'''
LIST_domain = []
for x in get_ALL_urls (url='https://journalists.feedspot.com/usa_news_websites/'):
  
    LIST_domain.append (get_domain_from_url (url=x))
    #print (get_domain_from_url (url=x))
    
   
LIST_domain = list(set(LIST_domain))


for y in LIST_domain:

   print (y)

'''


def get_HTML_elements (url):

   page = requests.get(url)
   soup = BeautifulSoup(page.text, 'html.parser')
 
   for ID in soup.find_all('div', id=True):  
      print(ID.get('id'))


#get_HTML_elements (url = 'https://www.google.com')


   # target url
url = 'https://www.google.com'
 
''' 
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

classes = []
for element in soup.find_all(title=True):
    classes.extend(element["title"])
    
print (classes)   
'''

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser').prettify()
'''
for tag in soup.findAll():
    try:
        print(tag['title'])
    except KeyError:
        pass
'''        
 
#print (soup)


def test_code (): 
   for line in soup.splitlines():

      class_only = remove_all_before_and_after_symbols (symbol_1 = 'class=' , symbol_2='>', string=line)
  
      #print (class_only)
      print (line)
      
      
'''      
How to get Domain search query url:
1. Get all elements from Webpage (Home page)
2. Get text field input and search input elements only (we need search textbox only) - Use id, title, class, name to check if its a text field input
3. Use id, title, class..etc to check if the input text field exists --> https://pythonexamples.org/python-selenium-check-if-input-text-field-exists/
4. Enter 3 values into the text field input and click enter. you should be redirected to a search result page 
5. The search result page should have values that you input into
6. Get the full url of the search result page
7. Remove anything AFTER the search query, including the search query to get the Domain search query url 
8. Use more search query with the DSQU to ensure the DSQU is correct (correct means that it directs to the correct search result page, with correct search results in html )
'''
