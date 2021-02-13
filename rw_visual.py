import matplotlib.pyplot as plt

from random_walk import RandomWalk


while True:
    rw = RandomWalk(100_000)
    rw.fill_walk()

    point_numbers = range(rw.num_points)
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15, 9))
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
               edgecolors='none', s=0.1)
    ax.scatter(0, 0, c='green', s=100, edgecolors='none')
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', s=100,
               edgecolors='none')
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break