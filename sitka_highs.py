import csv
import matplotlib.pyplot as plt
from datetime import datetime


filename = 'data\sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header = next(reader)
    high_temperatures, low_temperatures, dates = [], [], []
    for row in reader:
        high_temperatures.append(int(row[5]))
        low_temperatures.append(int(row[6]))
        dates.append(datetime.strptime(row[2], '%Y-%m-%d'))

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, high_temperatures, c='red')
ax.plot(dates, low_temperatures, c='blue')
plt.title('Daily Low and High Tempertures, 2018', fontsize=22)
plt.xlabel('', fontsize=14)
fig.autofmt_xdate()
plt.ylabel('Temperature, F', fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()
