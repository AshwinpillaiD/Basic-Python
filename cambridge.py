from bs4 import BeautifulSoup
import requests


url = ("https://www.cambridge.org/core/publications/journals")
host = ("https://www.cambridge.org")
response = requests.get(url)
#print(response.status_code)
soup=BeautifulSoup(response.text,"lxml")
#print(soup)
#class journals:
  #def journals_link(self):
for a_tag in soup.find_all('a',attrs = {"class":"title"}):
     href_tag=a_tag["href"]
     #print(href_tag)
     jour_link=(host+href_tag+"/all-issues")
     #print(jour_link)
     with open("journal_link.txt","a") as file:
         file.write(jour_link+"\n")
        
  # def issue_link(self):
   #  with open("journal_link.txt","r") as file:
         #for line in jour_link:
             #print(line)
         response1=requests.get(jour_link)
         soup1=BeautifulSoup(response1.text,"lxml")
        #   print(soup1)
         for vol in soup1.find_all('a',attrs={"class":"row"}):
             href_tag1=vol["href"]
             if href_tag1.startswith('/core/journals/'):
              #  print(host+href_tag1)
                issue_link=host+href_tag1
                with open("issue_link.txt","a") as file:
                    file.write(issue_link+"\n")
                      
  # def article_link(self):
                      # for art_link in issue_link:
                    response2=requests.get(issue_link)
                    soup1=BeautifulSoup(response2.text,"lxml")
                    for art in soup1.find_all('a',attrs={"class":"part-link"}):
                       # print(art)
                        art_link1=art['href']
                        print(host+art_link1)
                        hart_link=host+art_link1
                        with open("article_link.txt","a") as file:
                             file.write(hart_link+"\n")



                         #break    
                      # break 
          #  break
         #break
#obj=journals()
#obj.journa

