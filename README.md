# matplotlib_csv
Advanced Python - Matplotlib - using CSV files

this project is to teach students how to use CSV files in python
this project also teaches students how to visualize the data using matplotlib



Sitka file contains the code to generate the daily high temperatures for Sitka in a line graph for the month of July, 2018 from that particular file. 
Sitka2 file contains the code to generate the daily high temperatures for Sitka in a line chart for the month of July, 2018 from that particular file using the datetime module.
Sitka3 file contains the code to generate the daily high and low temperatures for Sitka in separate line graphs with separate sub headings for the year 2018 from that particular file.
Sitka4 contains the code to generate the daily high and low temperatures for Sitka in the same dual line graph with color fill inside for the year 2018 from that particular file.
Sitka5 file contains the code to generate a comparison of high and low temperatures for Sitka and Death Valley in separate dual line graphs with color fills inside and separate sub headings for the year 2018 from that particular file.

Understanding the code for Sitka5
Import the csv, datetime and matplotlib.pyplot modules.
Open both the Sitka and Death Valley files and read them on csv after the headers
Define the index for date, name, min and max temoeratures in the header row
Create empty lists for date, min and max temperatures which can be appended when we further read the file
Now we read all the rows in file 1 and try to find the date, min and max temperature.
In case we can't find it, we term it as missing data under except.
And else we append all our lists with the data.
We do the same for the 2nd file
To create the visualization, We first add the title.
Then under first graph we add the high and low temperatures.
Add the sub title for the first graph.
Define the x and y labels and its tickers and fill the in between space of high and low temperatures.
Repeat the same for the 2nd graph.
Here, we had defined our name, date, min and max temperatures to avoid hard coding.

