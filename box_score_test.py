from basketball_reference_web_scraper import client
from basketball_reference_web_scraper.data import OutputType

# Get all player box scores for January 1st, 2017 
day112017 = client.player_box_scores(day=1, month=1, year=2017)

#testing

player = []
team = []
game_date = []
location = []
opponent = []
outcome = []
seconds_played = []
made_field_goals =[]
attempted_field_goals = []
made_three_point_field_goals = []
attempted_three_point_field_goals = []
made_free_throws = []
attempted_free_throws = []
box_score = {}
i = 0

# first = day112017[0]

# player.append(first["name"])

# first = day112017[1]
# player.append(first["name"])
# player.append(first["team"])
# player.append(first["assists"])
# print(player)

for date in day112017:
    x = day112017[i]
    game_date.append("1-1-2017")
    i+=1

i = 0

for players in day112017:
    first = day112017[i]

    player.append(first["name"])
    i+=1

i = 0

for teams in day112017:
    x = day112017[i]

    team.append(x["team"])
    i+=1

for locations in day112017:
    x = day112017[i]

    team.append(x["location"])
    i+=1

box_score = {"game_date": game_date, "name": player, "team": team}


print(box_score)
