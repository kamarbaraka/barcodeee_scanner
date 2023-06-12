import pandas as pd

players = [{"112222222":{'dailyWinners': 3, 'dailyFreePlayed': 2, 'user': 'Player1', 'bank': 0.06},
"5522222222":{'dailyWinners': 3, 'dailyFreePlayed': 2, 'user': 'Player2', 'bank': 4.0},
"56556262":{'dailyWinners': 1, 'dailyFreePlayed': 2, 'user': 'Player3', 'bank': 3.1},
"36565656":{'dailyWinners': 3, 'dailyFreePlayed': 2, 'user': 'Player4', 'bank': 0.32}}]

df = pd.DataFrame.from_dict(players)

print (df)

df.to_excel('players222.xlsx')