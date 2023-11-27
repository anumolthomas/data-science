import requests
from bs4 import BeautifulSoup
def getdata(url):
    r=requests.get(url)
    return r.content
print("Name:Anumol Thomas\nRoll No:22MCA011\nCourse Name:DATA SCIENCE LAB\nCourse Code:20MCA241\n")
htmldata=getdata("https://www.geeksforgeeks.org/beautifulsoup-installation-python/")
soup=BeautifulSoup(htmldata,'html.parser')
links=soup.find_all("a")
print("links:",len(links))
for link in links:
    if link.get("href")!="":
        print("Link:",link.get("href"),"Text:",link.string)