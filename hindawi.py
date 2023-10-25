from bs4 import BeautifulSoup
import requests

url = ("https://www.hindawi.com/journals/cggr/contents/")
base_url=("https://www.hindawi.com/journals/cggr/contents/page/{}/")
host=("https://www.hindawi.com")
class hindawi_art:
    def page_num(self):
        respones = requests.get(url=url)
        soup = BeautifulSoup(respones.text,'lxml')
        a_tag = soup.find('a',attrs = {'class':"sc-htpNat bUhGXt link sc-iELTvK cqojQs pagination__last"})
        herf_tag = a_tag['href'].split("/")
        #print(type(int(herf_tag[-2])))
        self.page_no=int(herf_tag[-2])
        #print(page_no)
        #print(a_tag)
        #print(soup)
    def art_url(self):
        for i in range(1,self.page_no+1):
           # print((base_url.format(i)))
            page=base_url.format(i)
            respones=requests.get(page)
            soup=BeautifulSoup(respones.text,'lxml')
           # print(soup)
            for tag in soup.find_all('a',attrs={'class':"sc-htpNat bUhGXt link sc-cEvuZC bTvMeW"}):
                href=tag['href']
                articles = host+href
                f=open("hindaart.txt","a")
                f.write(articles+"\n")
                f.close()

obj=hindawi_art()
obj.page_num()
obj.art_url()
