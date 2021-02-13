from die import Die


die =Die()
num_rolls = 1000
results = [die.roll() for _ in range(num_rolls)]
frequencies = enumerate([results.count(value)
                         for value in range(1, die.num_sides + 1)], start=1)
print(*frequencies)