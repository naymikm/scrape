from bs4 import BeautifulSoup
from urllib2 import urlopen


html = urlopen("http://www.yelp.com/search?find_desc=Contractors&find_loc=Phoenix&start=3000")
bsobj = BeautifulSoup(html,'html5lib')

test = bsobj.find('div',{'class':'column column-alpha '}).find('div',{'class':'content'}).\
find('h3').text

print(test)
