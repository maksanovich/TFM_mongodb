

import sys
import feedparser


# https://stackoverflow.com/questions/75249065/reading-rss-feed-in-python

# https://medium.com/@jonathanmondaut/fetching-data-from-rss-feeds-in-python-a-comprehensive-guide-a3dc86a5b7bc
def get_RSS_feeds_content (rss_url):

   LIST_rss_content = []
   
   try:

      feed = feedparser.parse(rss_url)
   
      print (feed.keys())

      if feed.status == 200:
   
         for entry in feed.entries:
              
            print(entry.title)
            print (entry.published)        
            #print (entry.summary)
            print(entry.link)
            print ('\n')
         
            LIST_rss_content.append (' #_title ' + entry.title + ' #_pulished ' + entry.published + ' #_link ' + entry.link) 
                
      else:
      
         print("Failed to get RSS feed. Status code:", feed.status) 
         
   except:
    
      print ('ERROR')


   return LIST_rss_content         


#get_RSS_feeds_content (rss_url= 'https://www.dailytelegraph.com.au/feed')  

get_RSS_feeds_content (rss_url= 'https://rss.feedspot.com/algeria_rss_feeds/')  




#Input search query into search engine to get RSS urls by category 
def create_search_query_for_RSS_websites (LIST_country, LIST_rss_category):


   LIST_search_query = []
      
      
   for x in dict_reader_CSV (path_CSV): 

      LIST_country.append(x['Name'].strip())
            
                                      
   for country in LIST_country:
      
      for rss_category in LIST_rss_category:
      
         LIST_search_query.append ("Top rss feeds " + rss_category +  country)
   
   
   return LIST_search_query   
   
'''   
LIST_country = []
LIST_rss_category = [' ', 'news', 'business', 'games', 'videos', 'sports', 'politics']
'''