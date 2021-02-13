from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die


die_1 =Die()
die_2 = Die(10)
num_rolls = 50000
max_result = die_1.num_sides + die_2.num_sides

results = [die_1.roll() + die_2.roll() for _ in range(num_rolls)]
frequencies = [results.count(value) for value in range(2, max_result + 1)]

x_values = list(range(2, max_result + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(
    title=f'Results of Rolling A D6 & D10 Dice {num_rolls} Times',
    xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d10_d6.html')
