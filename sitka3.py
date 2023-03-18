#changing the file to include all the data for the year 2018
#change the title to daily and low high temperature - 2018
#extract low temps from the file and add to chart
#shade in the area between high and low

import csv
from datetime import datetime

infile = open('sitka_weather_2018_simple.csv', 'r')
csvfile = csv.reader(infile)

header_row = next(csvfile)

for index, column_header in enumerate(header_row):
    print(index, column_header)

highs = []
lows = []
dates = []

mydate = datetime.strptime('2018-07-01','%Y-%m-%d')

for row in csvfile:
    highs.append(int(row[5]))
    thedate = datetime.strptime(row[2],'%Y-%m-%d')
    dates.append(thedate)
    lows.append(int(row[6]))

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

#plt.show()

plt.subplot(2, 1, 1)
plt.plot(dates, highs, c='blue')
plt.title("Highs")

plt.subplot(2, 1, 2)
plt.plot(dates, lows, c='red')
plt.title("Lows")

plt.suptitle("Highs and Lows of Sitka, Alaska")

plt.show()