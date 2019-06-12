from urllib.request import urlopen
from bs4 import BeautifulSoup
import http.client
import json

connection = http.client.HTTPConnection('api.football-data.org')
headers = { 'X-Auth-Token': 'eb3e492624d444f49e859ba3afa146bf', 'X-Response-Control': 'full' }
connection.request('GET', '/v1/teams/1044/players', None, headers )
response = json.loads(connection.getresponse().read().decode())
# AFC Bournemouth
for item in response['players']:
      print (item['name'])
      print(item['position'])
      print(item['jerseyNumber'])
      print(item['dateOfBirth'])
      print (item['nationality'])
      print(item['contractUntil'])
      print(item['marketValue'])
      print("\n")
