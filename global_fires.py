import csv
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline


filename = 'data\MODIS_C6_Global_24h.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header = next(reader)
    i_lat = header.index('latitude')
    i_long = header.index('longitude')
    i_power = header.index('brightness')
    i_daynight = header.index('daynight')
    longs, lats, powers, daynights = [], [], [], []
    for row in reader:
        try:
            long = row[i_long]
            lat = row[i_lat]
            power = float(row[i_power])
            daynight = 'Day' if row[i_daynight] == 'D' else 'Night'
        except ValueError:
            print(f"Data missing for {long}, {lat}")
        else:
            longs.append(long)
            lats.append(lat)
            powers.append(power)
            daynights.append(daynight)

data = [
    {
        'type': 'scattergeo',
        'lon': longs,
        'lat': lats,
        'text': daynights,
        'marker': {
            'size': [0.04 * pow for pow in powers],
            'color': powers,
            'colorscale': 'ylorrd',
            'colorbar': {'title': 'Brightness'}
                    }
    }
        ]
my_layout = Layout(title=f'Global Fires Map for past 24h')
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_map_fires.html')
