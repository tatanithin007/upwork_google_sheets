from requests import get
from bs4 import BeautifulSoup
import csv
url='https://ca.finance.yahoo.com/quote/TA/cash-flow?p=TA'
responce=get(url)
soup = BeautifulSoup(responce.text, 'html.parser')
print(soup.xpath('/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/section/div[3]/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/span').getText())
