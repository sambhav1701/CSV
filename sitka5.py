import csv
from datetime import datetime

file1 = open('death_valley_2018_simple.csv', 'r')
file2 = open('sitka_weather_2018_simple.csv', 'r')
csvfile1 = csv.reader(file1)
csvfile2 = csv.reader(file2)

header_row1 = next(csvfile1)
header_row2 = next(csvfile2)

date_index = header_row1.index('DATE')
highs_index = header_row1.index('TMAX')
lows_index = header_row1.index('TMIN')
name_index = header_row1.index('NAME')

highs = []
lows = []
dates = []



for row in csvfile1:
    try:
        mydate = datetime.strptime(row[date_index],'%Y-%m-%d')
        high = int(row[highs_index])
        low = int(row[lows_index])
        name1 = row[name_index]
    except:
        print(f'Missing date for {mydate}')
    else:
        highs.append(high)
        lows.append(low)
        dates.append(mydate)


date_index1 = header_row2.index('DATE')
highs_index1 = header_row2.index('TMAX')
lows_index1 = header_row2.index('TMIN')
name_index1 = header_row2.index('NAME')

highs1 = []
lows1 = []
dates1 = []

for row in csvfile2:
    try:
        mydate = datetime.strptime(row[date_index1],'%Y-%m-%d')
        high = int(row[highs_index1])
        low = int(row[lows_index1])
        name2 = row[name_index1]
    except:
        print(f'Missing date for {mydate}')
    else:
        highs1.append(high)
        lows1.append(low)
        dates1.append(mydate)


import matplotlib.pyplot as plt

fig = plt.figure()


plt.suptitle("Temperature comparison between " + name2 + " and " + name1,  fontsize=16)
plt.subplot(2,1,1)
plt.plot(dates1, highs1, c = 'red', alpha = 0.5)  #alpha is for darkness of the line color
plt.plot(dates1, lows1, c = 'blue', alpha = 0.5)


plt.title(name2,  fontsize=16)
plt.xlabel("")
plt.ylabel("Temperature(F)", fontsize=12)
plt.tick_params(axis="both", which="major", labelsize=12)
plt.fill_between(dates1, highs1, lows1, color='green', alpha = 0.1)


plt.subplot(2,1,2)
plt.plot(dates, highs, c = 'red', alpha = 0.5)  #alpha is for darkness of the line color
plt.plot(dates, lows, c = 'blue', alpha = 0.5)

plt.title(name1,  fontsize=16)
plt.xlabel("")
plt.ylabel("Temperature(F)", fontsize=12)
plt.tick_params(axis="both", which="major", labelsize=12)
plt.fill_between(dates, highs, lows, color='green', alpha = 0.1)



plt.show()


