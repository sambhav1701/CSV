#handle error checking using try and except
#change file to use death valley file

import csv
from datetime import datetime

infile = open('death_valley_2018_simple.csv', 'r')
csvfile = csv.reader(infile)

header_row = next(csvfile)

for index, column_header in enumerate(header_row):
    print(index, column_header)

highs = []
lows = []
dates = []

mydate = datetime.strptime('2018-07-01','%Y-%m-%d')



for row in csvfile:
    try:
        high = int(row[4])
        low = int(row[5])
        thedate = datetime.strptime(row[2],'%Y-%m-%d')
    except ValueError:
        print(f'Missing data for {row[2]}')
    else:
        highs.append(high)
        lows.append(low)
        dates.append(thedate)
        

#print(highs)
#print(lows)

import matplotlib.pyplot as plt

fig = plt.figure()

plt.plot(dates, highs, c = 'red', alpha = 0.5)  #alpha is for darkness of the line color
plt.plot(dates, lows, c = 'blue', alpha = 0.5)

plt.title("Daily and low high temperatures - 2018", fontsize=16)
plt.xlabel("")
plt.ylabel("Temperature(F)", fontsize=12)
plt.tick_params(axis="both", which="major", labelsize=12)
plt.fill_between(dates, highs, lows, color='green', alpha = 0.1)

fig.autofmt_xdate()

plt.show()