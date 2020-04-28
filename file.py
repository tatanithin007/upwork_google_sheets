import requests
from bs4 import BeautifulSoup
import csv
#from yahoo_fin import stock_info as si
#from variables2 import symbol_list

#symbol='USA.TO'
total_stock_list=[]


def update_rows(symbol):    

    

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
        
        stocklist.append(market_cap)
        stocklist.append(total_cash)
        stocklist.append(total_cash_per_share)
        stocklist.append(total_debit)
        if stocklist == None:
            return(['NA','NA','NA','NA','NA'])
        else:
            return(stocklist)
    except KeyError:
        print("error")
