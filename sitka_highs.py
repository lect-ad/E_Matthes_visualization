import csv
import matplotlib.pyplot as plt
from datetime import datetime


filename = 'data\sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header = next(reader)
    high_temperatures = [int(row[5]) for row in reader]
    dates = [datetime.strptime(row[2], '%Y-%m-%d') for row in reader]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, high_temperatures, c='red')
plt.title('Daily High Tempertures, July 2018', fontsize=22)
plt.xlabel('', fontsize=14)
plt.ylabel('Temperature, F', fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()
