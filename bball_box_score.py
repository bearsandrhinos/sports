import csv
from basketball_reference_web_scraper import client
from basketball_reference_web_scraper.data import OutputType

# Get all player box scores for January 1st, 2017 
day112017 = client.player_box_scores(day=1, month=1, year=2017)

first = {}
i = 0
box_score = []
d = 0

with open('box_score_test.csv', mode='w') as csv_file:
    fieldnames = ['slug', 'name', 'team', 
    'location', 'opponent', 'outcome', 'seconds_played', 
    'made_field_goals', 'attempted_field_goals', 'made_three_point_field_goals',
    'attempted_three_point_field_goals', 'made_free_throws', 'attempted_free_throws',
    'offensive_rebounds', 'defensive_rebounds', 'assists', 'steals', 'blocks',
    'turnovers', 'personal_fouls', 'game_score', 'game_date']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

    for months in range(1, 13):
        for days in range(1, 32):
            date = str(months)+"-"+str(days)+"-2019"
            i = 0
            game = client.player_box_scores(day=int(days), month=int(months), year=2019)
            for rows in game:
                x = game[i]
                x["game_date"] = date
                #box_score.append(x)
                writer.writerow({'slug': x['slug'], 'name': x['name'], 'team': x['team'],
                'location': x['location'], 'opponent': x['opponent'], 'outcome': x['outcome'], 'seconds_played': x['seconds_played'], 
                'made_field_goals': x['made_field_goals'], 'attempted_field_goals': x['attempted_field_goals'], 'made_three_point_field_goals': x['made_three_point_field_goals'],
                'attempted_three_point_field_goals': x['attempted_three_point_field_goals'], 'made_free_throws': x['made_free_throws'], 'attempted_free_throws': x['attempted_free_throws'],
                'offensive_rebounds': x['offensive_rebounds'], 'defensive_rebounds': x['defensive_rebounds'], 'assists': x['assists'], 'steals': x['steals'], 'blocks': x['blocks'],
                'turnovers': x['turnovers'], 'personal_fouls': x['personal_fouls'], 'game_score': x['game_score'], 'game_date': x['game_date']})
                i+=1

    

print("All Done.")
