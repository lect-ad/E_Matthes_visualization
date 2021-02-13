import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline


filename = 'data\eq_data_1_day_m1.json'
with open(filename) as f:
    eq_data = json.load(f)
readable = 'data\\readable_eq_data.json'
with open(readable, 'w') as f:
    json.dump(eq_data, f, indent=4)

all_eq_dicts = eq_data['features']
magnitudes, longitudes, latitudes = [], [], []
for eq in all_eq_dicts:
    magnitudes.append(eq['properties']['mag'])
    longitudes.append(eq['geometry']['coordinates'][0])
    latitudes.append(eq['geometry']['coordinates'][1])

data = [Scattergeo(lon=longitudes, lat=latitudes)]
my_layout = Layout(title='Global Map of Earthquakes')
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_map_eqs.html')
