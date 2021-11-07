import requests
from bs4 import BeautifulSoup

url = 'http://www.footballlocks.com/nfl_point_spreads.shtml'
response = requests.get(url)
soup = BeautifulSoup(response.text)

tables = soup.find_all('table', cols='4', width='500')
rows = tables[0].findall('tr')

header = True
for row in rows:
    cells = row.find_all('td')
    if header:
        header = False
        continue
        
    favorite = cells[1].text
    spread = float(cells[2].text)
    underdog = cells[3].text
    
    print(f'favorite - {favorite}, Underdog - {underdog}, Spread - {spread:.0f}')






if __name__ == "__main__":
    pass
