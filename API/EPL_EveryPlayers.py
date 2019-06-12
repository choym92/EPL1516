from urllib.request import urlopen
from bs4 import BeautifulSoup
import http.client
import json

connection = http.client.HTTPConnection('api.football-data.org')
headers = { 'X-Auth-Token': 'eb3e492624d444f49e859ba3afa146bf', 'X-Response-Control': 'minified' }
connection.request('GET', '/v1/soccerseasons/398/teams', None, headers )
response = json.loads(connection.getresponse().read().decode())

for item in response['teams']:
      teamName = item['name']
      print('Team:')
      print('\nPlayer:')
      api_key = '/v1/teams/' + str(item['id'] ) + '/players'
      connection.request('GET', api_key, None, headers)
      response2 = json.loads(connection.getresponse().read().decode())
      for item2 in response2['players']:
            print (item2['name'])
            print(teamName)
            print(item2['position'])
            print(item2['jerseyNumber'])
            print(item2['dateOfBirth'])
            print (item2['nationality'])
            print(item2['contractUntil'])
            print(item2['marketValue'])
            print('\n')
