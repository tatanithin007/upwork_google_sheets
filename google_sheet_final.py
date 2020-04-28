import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
from file import update_rows

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("cred.json", scope)

client = gspread.authorize(creds)

sheet = client.open('tsx').sheet1  # Open the spreadhseet

dataset = sheet.get_all_records()  # Get a list of all records

count=sheet.row_count
print(count)


for i in range(1050,len(dataset)+1):
        value=sheet.cell(i,1).value
        total_stock_list=update_rows(value)
        if total_stock_list:
                sheet.update_cell(i,11, total_stock_list[2])  # Update one cell
                sheet.update_cell(i,12, total_stock_list[3])  
                sheet.update_cell(i,13, total_stock_list[4])  
        i=i+1
