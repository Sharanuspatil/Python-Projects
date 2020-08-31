import urllib
from bs4 import BeautifulSoup

url = ('Enter - ')

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
tag = soup("span")
count=0
sum=0
for i in tag:
	x=int(i.text)
	count+=1
	sum = sum + x
print (count)
print (sum)
