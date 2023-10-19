from bs4 import BeautifulSoup
import requests

respones=requests.get("https://www.nature.com/cddiscovery/articles?searchType=journalSearch&sort=PubDate&year=2023")
soup=BeautifulSoup(respones.text,"lxml")
base_url="https://www.nature.com/cddiscovery/articles?searchType=journalSearch&sort=PubDate&year=2023&page="
host="https://www.nature.com"
tag_value=[]
a=[]
for tag in soup.find_all('a',attrs={"class":"c-pagination__link"}):
   href=tag['href'].split("=")
   list_value=href[-1]
   a.append(int(list_value))
page_no=max(a)
for i in range(1,page_no+1):
   page=base_url+str(i)
   respones=requests.get(page)
   soup=BeautifulSoup(respones.text,"lxml")
   for tag in soup.find_all('a',attrs={"class":"c-card__link u-link-inherit"}):
      href=tag['href']
      articles=host+href
      file = open('articles.txt','a')
      file.write(articles+"\n")