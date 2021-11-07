import requests
from bs4 import BeautifulSoup

url = 'https://www.cbssports.com/nfl/stats/player/passing/nfl/regular/all/?sortcol=td&sortdir=descending'

webpage = requests.get(url).text
soup = BeautifulSoup(webpage, features = 'html5lib')
player_stats = soup.find_all('tr')[1:21]

for player in player_stats:
    name = player.find(attrs={'class': "CellPlayerName--long"}).text
    position = player.find(attrs={'class': "CellPlayerName-position"}).text
    team = player.find(attrs={'class': "CellPlayerName-team"}).text
    touchdowns = stats[7].text
    
    print(f'Name - {name}, Position - {position}, Team - {team}, Touchdowns - {touchdowns}')


if __name__ == "__main__":
    pass
