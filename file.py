import requests
from bs4 import BeautifulSoup
import csv

symbol_list=[
'FBS.TO',
'VNP.TO',
'AW.TO',
'FAP.TO',
'AAB.TO',
'ABT.TO',
'ADN.TO',
'AEF.TO',
'ACD.TO',
'ASP.TO',
'AEU.TO',
'DRX.TO',
'AAV.TO',
'AHY.TO',
'ARE.TO',
'AEZ.TO',
'AOI.TO',
'AFN.TO',
'ACR.TO',
'AGF.TO',
'AJX.TO',
'AEM.TO',
'AGU.TO',
'AGT.TO',
'AIM.TO',
'AC.TO',
'BOS.TO',
'AKT.TO',
'ASR.TO',
'AGI.TO',
'AD.TO',
'AF.TO',
'ADV.TO',
'AXR.TO',
'ALC.TO',
'AQN.TO',
'AQX.TO',
'ATD.TO',
'ABK.TO',
'ALB.TO',
'AP.TO',
'AMM.TO',
'ALA.TO',
'AXY.TO',
'ALS.TO',
'AIF.TO',
'AYA.TO',
'ACZ.TO',
'HOT.TO',
'USA.TO',
'ARG.TO',
'ANX.TO',
'ADW.TO',
'APY.TO',
'APS.TO',
'AQA.TO',
'ARZ.TO',
'ARX.TO',
'RGX.TO',
'AR.TO',
'ATZ.TO',
'AZ.TO',
'AX.TO',
'AKG.TO',
'MBB.TO',
'AOG.TO',
'AV.TO',
'AHF.TO',
'VIP.TO',
'AYM.TO',
'ACO.TO',
'ATH.TO',
'ATP.TO'
]

#symbol='USA.TO'
total_stock_list=[]

for symbol in symbol_list:
    

    url='https://in.finance.yahoo.com/quote/'+symbol+'/key-statistics?p='+symbol
    response = requests.get(url)
    soup=BeautifulSoup(response.text, 'html.parser')
    output = []
    result={}
    for table_num, table in enumerate(soup.find_all("table",class_='W(100%) Bdcl(c)')):    
        for tr in table.find_all('tr'):
            row = [''.join(cell.stripped_strings) for cell in tr.find_all(['td', 'th'])]
            it = iter(row) 
            res_dct = dict(zip(it, it))        
            result.update(res_dct)


    #stock_price = soup.find("span", attrs={"class": "price"}).getText().replace("\n", "").replace("\t", '').replace('\r', '')
    
    try:
        market_cap=result['Market cap (intra-day)5']
        total_cash=result['Total cash(mrq)']
        total_cash_per_share=result['Total cash per share(mrq)']
        total_debit=result['Total debt(mrq)']

        stocklist=[]
        stocklist.append(symbol)
        #stocklist.append(stock_price)
        stocklist.append(market_cap)
        stocklist.append(total_cash)
        stocklist.append(total_cash_per_share)
        stocklist.append(total_debit)
        total_stock_list.append(stocklist)
    except KeyError:
        continue
print(total_stock_list)


with open("temp.csv", "w", newline="") as f:
   writer = csv.writer(f)
   writer.writerows(total_stock_list)
