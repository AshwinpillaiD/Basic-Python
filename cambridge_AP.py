from bs4 import BeautifulSoup
import requests


url = ("https://www.cambridge.org/core/publications/journals")
host = ("https://www.cambridge.org")
response = requests.get(url)
#print(response.status_code)
soup = BeautifulSoup(response.text,"lxml")
class cambridge:
    def journals_link(self):
        for a_tag in soup.find_all('a',attrs = {"class":"title"}):
            href_tag = a_tag["href"]
            jour_link = (host+href_tag+"/all-issues")  #all-issues used toget the all-issues
            with open("journal_link.txt","a") as file:
                file.write(jour_link+"\n")
       
    def issues1_link(self):
        with open("journal_link.txt", "r") as file:
            for journal_links in file:  
                response1 = requests.get(journal_links.strip()) 
                soup1 = BeautifulSoup(response1.text, "lxml")
                for vol in soup1.find_all('a', attrs={"class": "row"}):
                    href_tag1 = vol["href"]
                    if href_tag1.startswith('/core/journals/'): #startswith function used get the string start with condetion 
                        issue_linka = host + href_tag1
                        with open("issues_link.txt", "a") as file1:
                           file1.write(issue_linka+"\n")

    def art_fun(self,art_link=None,page_link=None):
            response2 = requests.get(art_link.strip())
            soup2 = BeautifulSoup(response2.text,"lxml")
            for art in soup2.find_all('a',attrs = {"class":"part-link"}):
                art_link1 = art['href']
                hart_link = host+art_link1
                with open("article_link.txt","a") as file:
                    file.write(hart_link+"\n")

    def article_link(self):
        with open("issues_link.txt", "r") as file2:                
            for art_link in file2:
                response3 = requests.get(art_link.strip())
                soup3 = BeautifulSoup(response3.text,"lxml")
                ul_tag = soup3.find('ul',attrs={'class':'pagination'})
                if ul_tag:
                    for a_tag in ul_tag.find_all('a',attrs={'class':''}):
                        href_tag = a_tag['href'].split("=")
                    page_no = (int(href_tag[-1]))
                    id_no = art_link.split('/')[-1]
                    for i in range(1,page_no+1):
                        page_link = art_link.strip()+'?sort=canonical.position%3Aasc&pageNum={}&searchWithinIds={}&productType=JOURNAL_ARTICLE&template=cambridge-core%2Fjournal%2Farticle-listings%2Flistings-wrapper&hideArticleJournalMetaData=true&displayNasaAds=false'.format(i,id_no)
                        self.art_fun(page_link)
                else:
                    self.art_fun(art_link)
                          
obj=cambridge()
obj.journals_link()
obj.issues1_link()
obj.article_link()


