import requests
from bs4 import BeautifulSoup
url = "http://www.soccerstats.com/team.asp?league=england&teamid=3"
r=requests.get(url)
soup = BeautifulSoup(r.content)


g_data=soup.findAll("div",{"class":"six columns"})
for item in g_data:
      print (item.contents[6].findAll("table",{"cellpadding":"2"})[1].text)
