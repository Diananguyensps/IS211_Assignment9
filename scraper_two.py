import requests
from bs4 import BeautifulSoup

def main():
    url = "https://finance.yahoo.com/quote/AAPL/history?p=AAPL"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    rows = soup.find_all("tr")
    print("🍏 Apple Stock Historical Prices (Date & Close)\n")
    for row in rows[1:]:
        cols = [c.text.strip() for c in row.find_all("td")]
        if len(cols) >= 6:
            date = cols[0]
            close = cols[4]
            print(f"{date}: Close Price = {close}")

if __name__ == "__main__":
    main()

