import csv
import matplotlib.pyplot as plt
from datetime import datetime


filename = 'data\death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header = next(reader)
    i_name = header.index('NAME')
    i_date = header.index('DATE')
    i_min = header.index('TMIN')
    i_max = header.index('TMAX')
    high_temperatures, low_temperatures, dates = [], [], []
    for row in reader:
        try:
            name = row[i_name]
            date_ = datetime.strptime(row[i_date], '%Y-%m-%d')
            high = int(row[i_max])
            low = int(row[i_min])
        except ValueError:
            print(f"Data missing for {date_}")
        else:
            high_temperatures.append(high)
            low_temperatures.append(low)
            dates.append(date_)

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, high_temperatures, c='red', alpha=0.6)
ax.plot(dates, low_temperatures, c='blue', alpha=0.6)
plt.fill_between(dates,high_temperatures, low_temperatures,
                 facecolor='blue', alpha=0.2)
plt.title(f'Daily Low and High Tempertures in {name}, 2018', fontsize=18)
plt.xlabel('', fontsize=14)
fig.autofmt_xdate()
plt.ylabel('Temperature, F', fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()
