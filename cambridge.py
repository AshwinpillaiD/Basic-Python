from bs4 import BeautifulSoup
import requests


url = ("https://www.cambridge.org/core/publications/journals")
host = ("https://www.cambridge.org")

#get journal_link

response = requests.get(url)
#print(response.status_code)
soup=BeautifulSoup(response.text,"lxml")
for a_tag in soup.find_all('a',attrs = {"class":"title"}):
    href_tag = a_tag["href"]
    jour_link = (host+href_tag+"/all-issues")  # change the next from using concatenation (all-issues)
    with open("journal_link.txt","a") as file:
       file.write(jour_link+"\n")

#get issues_link
        
    response1 = requests.get(jour_link)
    soup1 = BeautifulSoup(response1.text,"lxml")
    for vol in soup1.find_all('a',attrs = {"class":"row"}):
        href_tag1 = vol["href"]
        if href_tag1.startswith('/core/journals/'):  #Required. The value to check if the string starts with
            issue_link = host+href_tag1
            with open("issue_link.txt","a") as file:
                file.write(issue_link+"\n")
                      
# get article_link
            response2 = requests.get(issue_link)
            soup1 = BeautifulSoup(response2.text,"lxml")
            for art in soup1.find_all('a',attrs = {"class":"part-link"}):
                art_link1 = art['href']
                hart_link = host+art_link1
                with open("article_link.txt","a") as file:
                    file.write(hart_link+"\n")



               

