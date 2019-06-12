#I can't seem to scrape the table for some reason
#Import
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pymysql

#Connect to database
#conn = pymysql.connect(host='127.0.0.1', user='root', passwd='idk', db='idk')
#cur=conn.cursor()
#cur.execute("idk")

def storeTeamvlaue(team_name,rank,point,win,draw,lose,GF,GA,points,strength,weakness,
                   style):
    cur.execute("INSERT INTO team_table (team_name,rank,point,win,draw,lose,GF,GA,points,strength,weakness,style) VALUES (%s,%f,%f,%f,%f,%f,%s,%s,%f,%s,%s,%s)",
                (team_name,rank,point,win,draw,lose,GF,GA,points,strength,weakness,style))
    cur.connection.commit()

def storePlayervalue(name,age,team,height,weight,position,shirt_number,nationality,strengh,weakness,style):
    cur.execute("INSERT INTO player_table (name,age,team,height,weight,position,shirt_number,nationality,strengh,weakness,style) VALUES (%s,%f,$s,%f,%f,%s,%f,%s,%s,%s,%s,%s)",
                (name,age,team,height,weight,position,shirt_number,nationality,strengh,weakness,style))
    cur.connection.commit()
    
                
def main():
    teamList=list()
    
    html = urlopen("https://www.whoscored.com/Regions/252/Tournaments/2/England-Premier-League/")
    bsObj = BeautifulSoup(html, "html.parser")

    tm=bsObj.findAll("div",{"id" : "tournament-tables-12496"})
    print(tm)

    for item in tm:
        a=itme.get_text().strip()
        teamList.append(a)
main()
