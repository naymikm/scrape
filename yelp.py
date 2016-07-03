from bs4 import BeautifulSoup
from urllib2 import urlopen
from random import randint
from time import sleep

with open('/home/naymikm/scrape/csv/phx_test50.csv','w') as out:
    #phoneBook = {}
    for i in range(5):
        sleep(randint(3,10))
        html = urlopen("http://www.yelp.com/search?find_desc=Contractors&find_loc=Phoenix&start="+str(i*10))
        bsobj = BeautifulSoup(html)
    
        
        bizHits = bsobj.findAll('li', {'class':'regular-search-result'})
        for hit in bizHits:
           
            bizName = (hit.find('span',{'class':'indexed-biz-name'}).find('span').text).encode('ascii','ignore').replace(',','')
            bizNum = (hit.find('div', {'class': 'secondary-attributes'}).find('span', {'class': 'biz-phone'}).text.strip()).encode('ascii', 'ignore')
            #phoneBook[bizName] = bizNum
            
            out.write(bizName+','+bizNum+'\n')
            print(bizName+':\t'+bizNum)
    
        print('\nFinished scraping page:\t' + str(i + 1))
        print('Sleeping...\n')
        
        
        
        #for listing in phoneBook:
        #    print(listing+':\t'+phoneBook[listing])
  
#    for listing in phoneBook:
#        out.write(listing+'\t'+phoneBook[listing]+'\n')
#    out.close()
