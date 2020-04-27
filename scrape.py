from requests import get
from bs4 import BeautifulSoup
import csv

symbols = ['vle']
final_result = []

filename='output.csv'

for symbol in symbols:

    url = 'https://web.tmxmoney.com/quote.php?qm_symbol='+symbol
    responce = get(url)
    soup = BeautifulSoup(responce.text, 'html.parser')
    # print(type(html_soup))

    url1 = url.split('=')

    result = []
    result.append(url1[1])

    stock_price = soup.find("span", attrs={"class": "price"}).getText().replace(
    "\n", "").replace("\t", '').replace('\r', '')

    result.append(stock_price)

    market_cap = soup.find("div", attrs={
                        "class": "dq-card"}).getText().replace("\n", "").replace("\t", '').replace('\r', '')
    result.append(market_cap)

    market_cap1 = soup.select_one(
    '#contentWrapper > div > div > div > div.tmx-panel.detailed-quote > div.tmx-panel-body > div > div:nth-child(9) > div > strong').getText()
    result.append(market_cap1)
    market_cap2=soup.select_one(
        '#pane-charting > div > div > div.col-md-9.col-lg-10 > div > div > div.qmod-tool-wrap > div > div.qmod-block-wrapper.qmod-financials-block > div.qmod-financials-cont > table > tbody > tr:nth-child(1) > td:nth-child(3)'
    )
    
    market_cap3=soup.select_one('#contentWrapper > div > div > div > div.tmx-panel.detailed-quote > div.tmx-panel-body > div > div:nth-child(13) > div > strong').getText()
    print(market_cap3)
    result.append(market_cap2)
    final_result.append(result)
    

print(final_result)

with open(filename, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(final_result)