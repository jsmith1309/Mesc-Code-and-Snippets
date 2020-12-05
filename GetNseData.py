import datetime
from jugaad_data.nse import stock_csv

class GetNseData:
    def data(self, symbol, date1, date2):
        path = "/home/pi/Documents/py/{}.csv".format(symbol)
        stock_csv(symbol, from_date=date1, to_date=date2, series="EQ", output=path)

def get_dates():
    date_entry = input('Enter a start date in DD-MM-YYYY format: ')
    day, month, year = map(int, date_entry.split('-'))
    date1 = datetime.date(year, month, day)
    date_entry = input('Enter a end date in DD-MM-YYYY format: ')
    day, month, year = map(int, date_entry.split('-'))
    date2 = datetime.date(year, month, day)
    return date1, date2

def get_symbols():
    file = open("./xyz.txt")
    lines = file.read().splitlines()
    file.close()

symbols = get_symbols()
start_date, end_date = get_dates()

for i in symbols:
    stock = i
    i = GetNseData()
    i.data(stock, start_date, end_date)
