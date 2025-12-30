import requests
from bs4 import BeautifulSoup
import pandas as pd


header = {
    'user-agent': 'Mozilla/5.0 \
        (Windows NT 10.0; Win64; x64) \
        AppleWebKit/537.36 (KHTML, like Gecko) \
        Chrome/143.0.0.0 Safari/537.36',
    "Accept-language": "en-US,en;q=0.9"
    }

links = [
    "https://groww.in/stocks/rail-vikas-nigam-ltd",
    "https://groww.in/stocks/hindustan-copper-ltd",
    "https://groww.in/stocks/indian-railway-finance-corporation-ltd",
    "https://groww.in/stocks/billionbrains-garage-ventures-ltd",
    "https://groww.in/stocks/reliance-power-ltd"
]
stock_details = []
for link in links:
    web_page = requests.get(link, headers= header)
    # print(web_page.status_code)
    try:
        soup = BeautifulSoup(web_page.text, 'html.parser')
        price_div = soup.find("div", class_="lpu38Pri").text
        company = soup.find("h1", class_="lpu38Head").text
        change_div = soup.select("div.bodyBaseHeavy")
        for div in soup.select("div.bodyBaseHeavy"):
            if "%" in div.text:
                change = div.text.split("1D")[0].strip()
                break
        div_volume = soup.find("div", class_="stockPerformance_keyText__f0fuN", string="Volume")
        volume = div_volume.find_next("span", class_="stockPerformance_value__g7yez").text
        list = [company, price_div, change, volume]
        stock_details.append(list)
    except AttributeError:
        print("Data not found")

column = ["Company", "Price", "Change", "Volume"]
df = pd.DataFrame(stock_details, columns = column)
df.to_excel("stocks.xlsx", index=False)