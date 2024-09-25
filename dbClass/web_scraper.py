import requests
from bs4 import BeautifulSoup

def extract_player_info(row):
    player_info = {}
    # Extract data with error handling for missing fields
    player_info['jersey_number'] = row.find('td', class_='roster_jerseynum').text.strip() if row.find('td', class_='roster_jerseynum') else None
    player_info['name'] = row.find('td', class_='sidearm-table-player-name').text.strip() if row.find('td', class_='sidearm-table-player-name') else None
    player_info['position'] = row.find('td', class_='rp_position_short').text.strip() if row.find('td', class_='rp_position_short') else None
    player_info['class_year'] = row.find('td', class_='roster_class').text.strip() if row.find('td', class_='roster_class') else None
    player_info['hometown'] = row.find('td', class_='hometownhighschool').text.strip() if row.find('td', class_='hometownhighschool') else None
    player_info['major'] = row.find('td', class_='player_major').text.strip() if row.find('td', class_='player_major') else None
    return player_info

def scrape_player_info(url):
    # Send a GET request to the page
    response = requests.get(url)
    
    # Check if request was successful
    if response.status_code != 200:
        print(f"Failed to retrieve page. Status code: {response.status_code}")
        return None
    
    # Parse the page content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    players_data = []
    
    # Find all table rows (tr) that contain player information
    rows = soup.find_all('tr')
    for row in rows:
        player_info = extract_player_info(row)
        if player_info['jersey_number'] and player_info['name']:
            players_data.append(player_info)
    
    return players_data  # Return the list of all players

# Example usage
url = 'https://auwolves.com/sports/baseball/roster'  # Replace with the actual URL
player_data = scrape_player_info(url)

if player_data:
    for player in player_data:
        print(player)  # Print each player's info
