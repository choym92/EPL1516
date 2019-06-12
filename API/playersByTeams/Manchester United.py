from urllib.request import urlopen
from bs4 import BeautifulSoup
import http.client
import json

connection = http.client.HTTPConnection('api.football-data.org')
headers = { 'X-Auth-Token': 'eb3e492624d444f49e859ba3afa146bf', 'X-Response-Control': 'full' }
connection.request('GET', '/v1/teams/66', None, headers )
response = json.loads(connection.getresponse().read().decode())
for item in response["_links"]:
      for item2 in item:
            print(item2)
