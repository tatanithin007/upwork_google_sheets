from requests import get
from bs4 import BeautifulSoup
import csv
url='https://in.finance.yahoo.com/quote/VLE.TO/key-statistics?p=VLE.TO'
responce=get(url)
soup = BeautifulSoup(responce.text, 'html.parser')
#print(soup.xpath('/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/section/div[3]/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/span').getText())

#print(soup.select_one('#Col1-0-KeyStatistics-Proxy > section > div.Mstart\(a\).Mend\(a\) > div:nth-child(1) > div > div > div > div > table > tbody > tr.Bxz\(bb\).H\(36px\).BdY.Bdc\(\$seperatorColor\).fi-row.Bgc\(\$hoverBgColor\)\:h > td.Fw\(500\).Ta\(end\).Pstart\(10px\).Miw\(60px\)'))

print(soup.find("td",attr={"class:":21}).getText())