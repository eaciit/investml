import csv
import os

with open('company_list.csv', 'rb') as f:
    reader = csv.reader(f)
    company_list = list(reader)

for cp in company_list:
    command = "wget -O " + cp[1] + ".csv \"https://ichart.finance.yahoo.com/table.csv?d=0&e=0&f=2017&g=d&a=0&b=0&c=2000&ignore=.csv&s=" + cp[1] + ".JK\""
    os.system(command)
