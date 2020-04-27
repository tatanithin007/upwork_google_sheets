from requests import get
from bs4 import BeautifulSoup
import csv
from lxml import etree
import html2csv
import HTMLParser
import sys, getopt, os.path, glob, HTMLParser, re

final_result=[]

url='https://in.finance.yahoo.com/quote/VLE.TO/key-statistics?p=VLE.TO'

r= get(url)
data=r.text
soup=BeautifulSoup(data)


result=soup.find_all("table",class_='W(100%) Bdcl(c)')
resultstr=str(result)
a=resultstr.replace('[','')
finalresult=a.replace(']','')



# htmlfile = open(htmlfilename, 'rb')
# csvfile = open( outputfilename, 'w+b')

data = finalresult

HTMLParser.HTMLParser.feed(data)

csvdata=HTMLParser.HTMLParser.getCSV(True)
print(csvdata)
# while data:
#     parser.feed( data )
#     csvfile.write( parser.getCSV() )
#     sys.stdout.write('%d CSV rows written.\r' % parser.rowCount)
#     data = htmlfile.read(8192)
# csvfile.write( parser.getCSV(True) )
# csvfile.close()
# htmlfile.close()

def getCSV(self,purge=False):
    ''' Get output CSV.
        If purge is true, getCSV() will return all remaining data,
        even if <td> or <tr> are not properly closed.
        (You would typically call getCSV with purge=True when you do not have
        any more HTML to feed and you suspect dirty HTML (unclosed tags). '''
    if purge and self.inTR: self.end_tr()  # This will also end_td and append last CSV row to output CSV.
    dataout = self.CSV[:]
    self.CSV = ''
    return dataout




