import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
url = "http://www.soccerstats.com/table.asp?league=england&tid=a"

r = requests.get(url)

soup = BeautifulSoup(r.content)

g_data = soup.find_all('table',{"id":"btable"})
playerdatasaved=""
for item in g_data:
      for record in item.findAll('tr'):
            playerdata=""
            for data in record.findAll('td'):
                  playerdata=playerdata+","+data.text
            playerdatasaved=playerdatasaved+"\n"+playerdata[1:]
print(playerdatasaved)
