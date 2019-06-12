import pymysql
def main(): 
 #connect to database
 conn = pymysql.connect(host='127.0.0.1', user='root', passwd='Yusarang10101993!', db='soccer')
 cur = conn.cursor()
 cur2 = conn.cursor()
 cur.execute("USE soccer")
 cur2.execute("USE soccer")
 
 #welcome statements
 print ("Welcome to the English Premeire League Database.")
 print ("Please Select one of the following options.")
 
 response = int(input("1. Exit"+"\n"+"2. Matches"+"\n"+"3. Teams"+"\n"+"4. Players"+"\n"))
 
 #user inputs
 if response == 1:
  print("Good Bye!")
 
 #match search 
 if response == 2:
  print("\n"+"----------------------------------")
  print("Would you like to search matches by the match date or home team?")
  match_response = int(input("1. Match Date"+"\n" + "2. Home Team"+"\n"))
  
  if match_response == 1:
   print("\n"+"----------------------------------")
   match_date = input("Please enter the date of the match (DD/MM/YYYY): ")
   print("\n"+"----------------------------------")
   cur.execute("SELECT game_date, home_team, away_team, home_goals, away_goals FROM game WHERE game_date = %s", match_date)
   for line in cur:
    print("Date:",line[0])
    print("Home Team:",line[1])
    print("Away Team:",line[2])
    print("Final Score (Home:Away)",line[3],":",line[4],"\n")
	
   
  if match_response == 2:
   print("\n"+"----------------------------------")
   match_team = input("Please enter the name of the home team: ")
   cur.execute("SELECT game_date, home_team, away_team, home_goals, away_goals FROM game WHERE home_team = %s", match_team)
   for line in cur:
    print("Date:",line[0])
    print("Home Team:",line[1])
    print("Away Team:",line[2])
    print("Final Score (Home:Away)",line[3],":",line[4],"\n")

   
 #team search
 if response == 3:
  print("\n"+"----------------------------------")
  team_question = int(input("What information would you like to view?"+"\n"+"1. League Standings"+"\n"+"2. Team Specific Data " +"\n"))
  if team_question == 1:
   print("\n"+"----------------------------------")
   cur.execute("SELECT t.rank, t.team_name, o.team_points FROM team t, team_totals o WHERE t.team_id = o.team_id")
   print("\n"+"----------------------------------")
   for line in cur:
    print("Rank:",line[0])
    print("Team:",line[1])
    print("Points:",line[2],"\n")
   
  # team specific data
  if team_question == 2:
   cur.execute('SELECT team_id, team_name FROM team')
   for line in cur:
    print('Team ID:',line[0],"Team Name:",line[1])
   print("\n"+"----------------------------------")
   team_input = int(input("Enter the Team ID of the team you would like to search: "))
   print("\n"+"----------------------------------")
   cur.execute('SELECT t.team_name,o.team_games, o.team_wins, o.team_draws, o.team_losses, o.team_goals, o.team_goals_conceded FROM team t, team_totals o WHERE t.team_id = o.team_id AND t.team_id = %s',team_input)
   for line in cur:
    print('Team Name:',line[0])
    print('Total Games Played:',line[1])
    print('Record (W-D-L):',line[2],'-',line[3],'-',line[4])
    print('Total Goals Made:',line[5])
    print('Total Goals Conceded:',line[6])
  
 #player search
 if response == 4:
  print("\n"+"----------------------------------")
  player_selection = int(input("Would you like to search for player by name or team?"+"\n"+"1. Name" + "\n" + "2. Team"+"\n"))
  
  # search by name
  if player_selection == 1:
   print("\n"+"----------------------------------")
   name_input = input("\n"+"Enter the name of the player: ")
   print("\n"+"----------------------------------")
   cur.execute("SELECT name, team_name, position, shirt_number, dateofbirth, nationality, salary FROM player WHERE name = %s",(name_input))
   for line in cur:
    print("Player Name:",line[0])
    print("Team:",line[1])
    print("Position:",line[2])
    print("Shirt Number:",line[3])
    print("Date of Birth:",line[4])
    print("Nationality:",line[5])
    print("Salary (Euros):", line[6])
	 
  if player_selection == 2:
   print("\n"+"----------------------------------")
   cur.execute('SELECT team_id, team_name FROM team')
   for line in cur:
    print('Team ID:',line[0],'Team Name:',line[1])
   print("\n"+"----------------------------------")
   team_name = input("\n"+"Enter Team Name: ")
   cur.execute("SELECT player_id, name FROM player WHERE team_name = %s",team_name)
   print("\n"+"----------------------------------")
   for line in cur:
    print(line[0],line[1])
   #select player id
   print("\n"+"----------------------------------")
   selection = int(input("Select Player ID: "))
   print("\n"+"----------------------------------")
   cur.execute("SELECT name, team_name, position, shirt_number, dateofbirth, nationality, salary FROM player WHERE player_id = %s",selection)
   for line in cur:
    print("Player Name:",line[0])
    print("Team:",line[1])
    print("Position:",line[2])
    print("Shirt Number:",line[3])
    print("Date of Birth:",line[4])
    print("Nationality:",line[5])
    print("Salary (Euros):", line[6])
   


main()