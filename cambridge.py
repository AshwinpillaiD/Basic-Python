from bs4 import BeautifulSoup
import requests

url = ("https://www.cambridge.org/core/publications/journals")
host = ("https://www.cambridge.org")
response = requests.get(url)
#print(response.status_code)
soup=BeautifulSoup(response.text,"lxml")
#print(soup)
class journals:
  def journals_link(self):
    for a_tag in soup.find_all('a',attrs = {"class":"title"}):
        href_tag=a_tag["href"]
        #print(href_tag)
        jour_link=(host+href_tag+"/all-issues")
        print(jour_link)
        file=open("journal_link.txt","a")
        file.write(jour_link+"\n")
        file.close()

        response1=requests.get(jour_link)
        soup1=BeautifulSoup(response1.text,"lxml")
        for vol in soup1.find_all('li',attrs={"class":"accordion-navigation"}):
            a_tag=vol['li']
            print(a_tag)

        break

obj=journals()
obj.journals_link()
