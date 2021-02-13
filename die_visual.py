from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die


die =Die()
num_rolls = 1000
results = [die.roll() for _ in range(num_rolls)]
frequencies = [results.count(value) for value in range(1, die.num_sides + 1)]

x_values = list(range(1, die.num_sides + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title=f'Results of Rolling Single D6 Die {num_rolls} Times',
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='single_d6.html')