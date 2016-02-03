from bs4 import BeautifulSoup
import requests


# how to get the content of a specific element
# use firefox with the firebug extension
# select the considered element
# right click on the path in the inspector window ->  "copy css path"

b = requests.get("https://www.hip.reutlingen-university.de/qisserver/rds?state=user&type=0&topitem=&breadCrumbSource=portal&topitem=functions")

soup = BeautifulSoup(b.text, 'html.parser')
c = soup.select("html body div#wrapper div.divcontent div#makronavigation")


print(str(c).replace('[','').replace(']',''))

print(c[0].text)


soup = BeautifulSoup(str(c).replace('[','').replace(']',''), 'html.parser')
c = soup.find_all("li")

print(c)