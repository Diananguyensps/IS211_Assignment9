import requests
from bs4 import BeautifulSoup

def main():
    url = "https://www.cbssports.com/nfl/stats/playersort/nfl/year-2024-season-regular-category-touchdowns"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    table = soup.find("table")
    if not table:
        print("Could not find the stats table. The website structure might have changed.")
        return
    rows = table.find_all("tr")[1:21]
    print("🏈 Top 20 NFL Players - Touchdowns (Regular Season)\n")
    for row in rows:
        cols = [col.text.strip() for col in row.find_all("td")]
        if len(cols) >= 5:
            player = cols[0]
            team = cols[1]
            position = cols[2]
            touchdowns = cols[-1]
            print(f"{player} | {team} | {position} | Touchdowns: {touchdowns}")

if __name__ == "__main__":
    main()

