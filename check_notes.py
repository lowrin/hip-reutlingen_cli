from bs4 import BeautifulSoup
import requests

pruefungsverwaltung = "https://www.hip.reutlingen-university.de/qisserver/rds?state=change&type=1&moduleParameter=studyPOSMenu&nextdir=change&next=menu.vm&subdir=applications&xml=menu&purge=y&navigationPosition=functions%2CstudyPOSMenu&breadcrumb=studyPOSMenu&topitem=functions&subitem=studyPOSMenu"
loginpage = "https://www.hip.reutlingen-university.de/qisserver/rds?state=user&type=1&category=auth.login&startpage=portal.vm&breadCrumbSource=portal"

name = "<name>"
password =  "<password>"


session = requests.session
# asdf: name, fdsa: password
payload = {'asdf': name, 'fdsa': password}
session = requests.Session()
r = session.post(loginpage, data=payload)

#debugging
#print(r.text)
#print(r.headers)
#print(r.request.headers)


# uebersichts seite
pruefungsverwaltung_page = session.get(pruefungsverwaltung)
#print(r2.text)
soup = BeautifulSoup(pruefungsverwaltung_page.text, 'html.parser')
#print(soup.prettify())

# get the notenspiegel link with the session id (asi)
pruefungsverwaltung_site =  soup.findAll("div", { "class" : "mikronavi_list" })
s1 = BeautifulSoup(str(pruefungsverwaltung_site), 'html.parser')
notenspiegel =  s1.find_all(href=True)
notenübersicht_link = str(notenspiegel).split('"')[3]

asi = notenübersicht_link.split("=")[8]
#print(asi)


# hier muesst ihr den anderen, studiengangspezifischen, link setzen.
wim = "https://www.hip.reutlingen-university.de/qisserver/rds?state=notenspiegelStudent&next=list.vm&nextdir=qispos/notenspiegel/student&createInfos=Y&struct=auswahlBaum&nodeID=auswahlBaum%7Cabschluss%3Aabschl%3D90%2Cstgnr%3D1%7Cstudiengang%3Astg%3DWIN&expand=0&asi="+asi+"#auswahlBaum%7Cabschluss%3Aabschl%3D90%2Cstgnr%3D1%7Cstudiengang%3Astg%3DWIN"

#load the page with cookie
notenspiegel_page = session.get(wim)
#print(r2.text)



########################
# read notenspiegel overview
soup = BeautifulSoup(notenspiegel_page.text, 'html.parser')
#print(soup.prettify())
notenspiegel_content =  soup.findAll("div", { "class" : "content" })
#print(notenspiegel_content)
soup = BeautifulSoup(str(notenspiegel_content), 'html.parser')
tabellen =  soup.findAll("table")
print(tabellen)
soup = BeautifulSoup(str(tabellen[1]), 'html.parser')
for tr in soup.find_all("tr"):
    print(tr)
    print("--")
    cells = tr.findAll("td")
    print(cells)
    print(cells[1].find(Text=True))


