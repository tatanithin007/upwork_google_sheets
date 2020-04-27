from requests import get
from bs4 import BeautifulSoup
import bs4
import csv
import io
final_result=[]

url='https://in.finance.yahoo.com/quote/VLE.TO/key-statistics?p=VLE.TO'

r= get(url)
data=r.text
soup=BeautifulSoup(data)


result=soup.find_all("table",class_='W(100%) Bdcl(c)')
resultstr=str(result)
a=resultstr.replace('[','')
finalresult=a.replace(']','')

def detect_engine():
    try:
        import lxml
    except ImportError:
        engine = 'html.parser'
    else:
        engine = 'lxml'
    return engine

def convert( html_doc):
    soup = bs4.BeautifulSoup(html_doc,'html.parser' )
    output = []
    for table_num, table in enumerate(soup.find_all('table')):
        csv_string = io.StringIO()
        csv_writer = csv.writer(csv_string)
        for tr in table.find_all('tr'):
            row = [''.join(cell.stripped_strings) for cell in tr.find_all(['td', 'th'])]
            csv_writer.writerow(row)
        table_attrs = dict(num=table_num)
        output.append((csv_string.getvalue(), table_attrs))
    return output

# print(len(convert(finalresult)))
finalarray=[]
outputarray = convert(finalresult)
len(outputarray)
for i in (outputarray):
    for j in (1,len(i)-1):
        # print(j)
        finalarray.append((i[0]))
        print(finalarray)
    # print(i)

