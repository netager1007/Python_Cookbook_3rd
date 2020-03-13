# 6.1 Reading and Writing CSV Data
import csv
with open('stocks.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        print(row)

from collections import namedtuple
with open('stocks.csv') as f:
    f_csv = csv.reader(f)
    headings = next(f_csv)
    Row = namedtuple('Row', headings)
#    print(headings)
    for r in f_csv:
        row = Row(*r)
        print(row.Symbol, row.Change, row.Date, row.Time, row.Change, row.Volume)

import csv
with open('stocks.csv') as f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
        print(row['Symbol'], row['Date'])

# To write CSV data, you also use the csv module but create a writer object. For example:
headers = ['Symbol','Price','Date','Time','Change','Volume']
rows = [('AA', 39.48, '6/11/2007', '9:36am', -0.18, 181800),
        ('AIG', 71.38, '6/11/2007', '9:36am', -0.15, 195500),
        ('AXP', 62.58, '6/11/2007', '9:36am', -0.46, 935000),
        ]

with open('stocks1.csv', 'w') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(rows)

headers = ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']
rows = [{'Symbol':'AA', 'Price':39.48, 'Date':'6/11/2007', 'Time':'9:36am', 'Change':-0.18, 'Volume':181800},
        {'Symbol':'AIG', 'Price': 71.38, 'Date':'6/11/2007', 'Time':'9:36am', 'Change':-0.15, 'Volume': 195500},
        {'Symbol':'AXP', 'Price': 62.58, 'Date':'6/11/2007', 'Time':'9:36am', 'Change':-0.46, 'Volume': 935000},
        ]
with open('stocks2.csv', 'w') as f:
    f_csv = csv.DictWriter(f, headers)
    f_csv.writeheader()
    f_csv.writerows(rows)


# Discussion
# You should almost always prefer the use of the csv module over manually trying to split
# and parse CSV data yourself. For instance, you might be inclined to just write some
# code like this:
with open('stocks.csv') as f:
    for line in f:
            row = line.split(',')
            print(row)

# The problem with this approach is that you’ll still need to deal with some nasty details.
# For example, if any of the fields are surrounded by quotes, you’ll have to strip the quotes.
# In addition, if a quoted field happens to contain a comma, the code will break by producing
# a row with the wrong size.
# By default, the csv library is programmed to understand CSV encoding rules used by
# Microsoft Excel. This is probably the most common variant, and will likely give you the
# best compatibility. However, if you consult the documentation for csv, you’ll see a few
# ways to tweak the encoding to different formats (e.g., changing the separator character,
# etc.). For example, if you want to read tab-delimited data instead, use this:

# Example of reading tab-separated values
with open('stocks.csv') as f:
    f_tsv = csv.reader(f, delimiter='\t')
    for row in f_tsv:
        pass
        # Process row

# If you’re reading CSV data and converting it into named tuples, you need to be a little
# careful with validating column headers. For example, a CSV file could have a header
# line containing nonvalid identifier characters like this:
#    Street Address,Num-Premises,Latitude,Longitude
#    5412 N CLARK,10,41.980262,-87.668452

# This will actually cause the creation of a namedtuple to fail with a ValueError exception.
# To work around this, you might have to scrub the headers first. For instance, carrying
# a regex substitution on nonvalid identifier characters like this:
import re
with open('stocks.csv') as f:
    f_csv = csv.reader(f)
    headers = [re.sub('[^a-zA-Z_]', '_', h) for h in next(f_csv)]   # '-' to '_'
    Row = namedtuple('Row', headers)
    for r in f_csv:
        row = Row(*r)
        # Process row