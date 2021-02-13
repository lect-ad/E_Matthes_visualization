import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline


filename = 'data\eq_data_30_day_m1.json'
with open(filename) as f:
    eq_data = json.load(f)
readable = 'data\\readable_eq_data.json'
with open(readable, 'w') as f:
    json.dump(eq_data, f, indent=4)

all_eq_dicts = eq_data['features']
magnitudes, longitudes, latitudes, hints = [], [], [], []
for eq in all_eq_dicts:
    magnitudes.append(eq['properties']['mag'])
    longitudes.append(eq['geometry']['coordinates'][0])
    latitudes.append(eq['geometry']['coordinates'][1])
    hints.append(eq['properties']['title'])
map_title = eq_data['metadata']['title']

data = [
    {
        'type': 'scattergeo',
        'lon': longitudes,
        'lat': latitudes,
        'text': hints,
        'marker': {
            'size': [6 * mag for mag in magnitudes],
            'color': magnitudes,
            'colorscale': 'ylorrd',
            'colorbar': {'title': 'Magnitude'}
                    }
    }
        ]
my_layout = Layout(title=f'{map_title}')
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_map_eqs.html')
