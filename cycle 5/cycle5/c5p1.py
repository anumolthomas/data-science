import requests
from bs4 import BeautifulSoup
def getdata(url):
    r=requests.get(url)
    return r.content
print("Name:Anumol Thomas\nRoll No:22MCA011\nCourse Name:DATA SCIENCE LAB\nCourse Code:20MCA241\n")
htmldata=getdata('https://www.geeksforgeeks.org/beautifulsoup-installation-python/')
Soup=BeautifulSoup(htmldata,'html.parser')
data=''
pr=len(Soup.find_all('p'))
print("P tag:",pr)
for data in Soup.find_all('p'):
    print(data.get_text())