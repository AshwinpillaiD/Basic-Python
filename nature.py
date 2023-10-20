from bs4 import BeautifulSoup
import requests

respones = requests.get("https://www.nature.com/cddiscovery/articles?searchType=journalSearch&sort=PubDate&year=2023")
soup = BeautifulSoup(respones.text,"lxml")

base_url = "https://www.nature.com/cddiscovery/articles?searchType=journalSearch&sort=PubDate&year=2023&page="
host = "https://www.nature.com"
tag_value = []
a = []
class articleslink():
   def page_num(self):
         for tag in soup.find_all('a',attrs={"class":"c-pagination__link"}):
           # print(tag)
            href = tag['href'].split("=")
          #  print(href)
            list_value = href[-1]
           # print(list_value)
            a.append(int(list_value))
         self.page_no=max(a)
         print(self.page_no)
                     
   def Url_pn(self):
         for i in range(1,self.page_no+1):
            page = base_url+str(i)
            print(page,"\n")                     
            respones = requests.get(page)
            soup = BeautifulSoup(respones.text,"lxml")
            for tag in soup.find_all('a',attrs={"class":"c-card__link u-link-inherit"}):
               href = tag['href']
               articles = host+href
               print(articles)
               file = open('articles.txt','a')
               file.write(articles+"\n")
               file.close()
obj=articleslink()   
obj.page_num()
obj.Url_pn()
