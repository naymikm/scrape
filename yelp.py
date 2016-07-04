from bs4 import BeautifulSoup
from urllib2 import urlopen
from random import randint
from time import sleep
import subprocess

subprocess.call( "echo '#Each scrape = 10\nInitializing...\n' > log.txt",shell=True )
print('Initializing scraper...')
with open('/home/naymikm/scrape/csv/VB_contractors.csv','w') as out:
    #phoneBook = {}
    page = 0
    total = 0
    while page <= 99:
        sleep(randint(5,30))
        html = urlopen("http://www.yelp.com/search?find_desc=Contractors&find_loc=Virginia+Beach&start="+str(page*10))
        bsobj = BeautifulSoup(html,'html5lib')
    
        bizHits = bsobj.findAll('li', {'class':'regular-search-result'})
       
        if bizHits == []:
            subprocess.call("echo '\nAll pages exhausted xD' >> log.txt",shell=True)
            exit(0)
        else:
            for hit in bizHits:
                bizName = hit.find('span',{'class':'indexed-biz-name'}).find('span')
                bizNameText = bizName.text.encode('ascii','ignore').replace(',','')
                
                bizNum = hit.find('div', {'class': 'secondary-attributes'}).find('span', {'class': 'biz-phone'})
                bizNumText = bizNum.text.strip().encode('ascii', 'ignore')
                
                #phoneBook[bizName] = bizNum
                #print(type(bizName))
                #print(type(bizNum)) 
                if len(bizNumText) > 1:
                    out.write(bizNameText+','+bizNumText+'\n')
                    total += 1
                else:
                    continue
            
            subprocess.call( "echo 'scraped' >> log.txt",shell=True )
            page += 1
    
print('Done!')
        
        
        #for listing in phoneBook:
        #    print(listing+':\t'+phoneBook[listing])
  
#    for listing in phoneBook:
#        out.write(listing+'\t'+phoneBook[listing]+'\n')
#    out.close()
