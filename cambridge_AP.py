from bs4 import BeautifulSoup
import requests


url = ("https://www.cambridge.org/core/publications/journals")
host = ("https://www.cambridge.org")
response = requests.get(url)
#print(response.status_code)
soup = BeautifulSoup(response.text,"lxml")
#print(soup)
class cambridge:
    def journals_link(self):
        for a_tag in soup.find_all('a',attrs = {"class":"title"}):
            href_tag = a_tag["href"]
            #print(href_tag)
            jour_link = (host+href_tag+"/all-issues")
            #print(jour_link)
            with open("journal_link.txt","a") as file:
                file.write(jour_link+"\n")
       
    def issues1_link(self):
       # def issues1_link(self):
        with open("journal_link.txt.bkp", "r") as file:
            for journal_links in file:  
               # print(journal_links)              
                response1 = requests.get(journal_links.strip()) 
               # print(response1)
                soup1 = BeautifulSoup(response1.text, "lxml")
                for vol in soup1.find_all('a', attrs={"class": "row"}):
                    href_tag1 = vol["href"]
                    #print(href_tag1)
                    if href_tag1.startswith('/core/journals/'):
                        issue_linka = host + href_tag1
                        #print(issue_linka)
                        with open("issues_link.txt", "a") as file1:
                           file1.write(issue_linka+"\n")


    def article_link(self):
       #with open("article_link.txt","a") as file:
         
        with open("issues_link1.txt.bkp", "r") as file2:                
            for art_link in file2:
                #print(art_link)
               # art_link = "https://www.cambridge.org/core/journals/cambridge-law-journal/issue/34913514C2EEA7D0010DF7A42CBEC61D"       
                # art_link = "https://www.cambridge.org/core/journals/acta-neuropsychiatrica/issue/952F85CDF18CAF8D52E89D72F69C6316"
                
                response3 = requests.get(art_link.strip())
                soup3 = BeautifulSoup(response3.text,"lxml")
                #print(soup3)
                ul_tag = soup3.find('ul',attrs={'class':'pagination'})
                if ul_tag:
                    #print("True")
                    for a_tag in ul_tag.find_all('a',attrs={'class':''}):
                       # print(a_tag)
                        href_tag = a_tag['href'].split("=")
                       # print(href_tag)    
                        
                    print(href_tag)    
                    page_no = (int(href_tag[-1]))
                    #print(page_no)
                    # get the last page
                    id_no = art_link.split('/')[-1]
                    #print(id_no)
                    for i in range(1,page_no+1):
                        page_link = art_link.strip()+'?sort=canonical.position%3Aasc&pageNum={}&searchWithinIds={}&productType=JOURNAL_ARTICLE&template=cambridge-core%2Fjournal%2Farticle-listings%2Flistings-wrapper&hideArticleJournalMetaData=true&displayNasaAds=false'.format(i,id_no)
                        #print(page_link)
                        response2 = requests.get(page_link.strip())
                        soup2 = BeautifulSoup(response2.text,"lxml")
                        for art in soup2.find_all('a',attrs = {"class":"part-link"}):
                           # print(art)
                            art_link1 = art['href']
                           # print(host+art_link1)
                            hart_link = host+art_link1
                            with open("article_link.txt","a") as file:
                                file.write(hart_link+"\n")


                else:
                    print("Flase")
                    response2 = requests.get(art_link.strip())
                    soup2 = BeautifulSoup(response2.text,"lxml")
                    for art in soup2.find_all('a',attrs = {"class":"part-link"}):
                       # print(art)
                        art_link1 = art['href']
                       # print(host+art_link1)
                        hart_link = host+art_link1
                        with open("article_link.txt","a") as file:
                            file.write(hart_link+"\n")



       
       
obj=cambridge()
#obj.journals_link()
#obj.issues1_link()
obj.article_link()


