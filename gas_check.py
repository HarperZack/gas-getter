import requests
from bs4 import BeautifulSoup


def get_urls(zip):
    urls = [
    f'https://www.autoblog.com/{int(zip)}-gas-prices/',
    f'https://www.autoblog.com/{int(zip)}-gas-prices/pg-2/',
    f'https://www.autoblog.com/{int(zip)}-gas-prices/pg-3/'
    ]
    return urls


def get_results(zip):
    urls = get_urls(zip)
    results = list()
    low = float(10)
    for url in urls:
        data = requests.get(url).text
        soup = BeautifulSoup(data, 'html.parser')
        responses = soup.find_all("li", class_="shop")
        for entry in responses:
            try:
                rows = entry.text.split('\n')
                shop_raw = rows[2]
                price = float(rows[4][1:5])
                price_report = rows[4][5:]
                days = price_report[0]
                if int(days) < 5:
                    if price < low:
                        low = price
                        results = {shop_raw: price}
            except IndexError:
                break
    return results
