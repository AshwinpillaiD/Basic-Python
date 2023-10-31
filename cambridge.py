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
        #print(jour_link)
        with open("journal_link.txt","a") as file:
            file.write(jour_link+"\n")

  def volume_link(self):
        with open("journal_link.txt","r") as file:
            for line in file:
                print(line)
                response1=requests.get(line)
                soup1=BeautifulSoup(response1.text,"lxml")
            #   print(soup1)
                for vol in soup1.find_all('li',attrs={"class":"accordion-navigation"}):
                    for a_tag in vol.find_all('a'):
                        print(a_tag)
                        href_tag=a_tag['href']
                        #print(href_tag)
                #    break

                #     a_tag=vol['li']
                break

obj=journals()
obj.journals_link()
obj.volume_link()
