from urllib.request import urlopen
from bs4 import BeautifulSoup
import http.client
import json

connection = http.client.HTTPConnection('api.football-data.org')
headers = { 'X-Auth-Token': 'eb3e492624d444f49e859ba3afa146bf', 'X-Response-Control': 'full' }
connection.request('GET', '/v1/soccerseasons/398/leagueTable', None, headers )
response = json.loads(connection.getresponse().read().decode())
print(response["leagueCaption"])
print("# Team GP W D L  GF GA GD PTS")
for item in response["standing"]:
      print(item["position"], item["teamName"], item["playedGames"], item["wins"], item["draws"], item["losses"], item["goals"], item["goalsAgainst"], item["goalDifference"] , item["points"])

