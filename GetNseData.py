import datetime
from jugaad_data.nse import stock_csv

class GetNseData:
    def data(self, symbol, date1, date2):
        path = "/home/pi/Documents/py/{}.csv".format(symbol)
        stock_csv(symbol, from_date=date1, to_date=date2, series="EQ", output=path)
    
list1 = ["SBIN", "ACC"]

date_entry = input('Enter a start date in DD-MM-YYYY format: ')
day, month, year = map(int, date_entry.split('-'))
date1 = datetime.date(year, month, day)

date_entry = input('Enter a end date in DD-MM-YYYY format: ')
day, month, year = map(int, date_entry.split('-'))
date2 = datetime.date(year, month, day)

for i in list1:
    stock = i
    i = GetNseData()
    i.data(stock, date1, date2)
    



