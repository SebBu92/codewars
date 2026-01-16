def number(bus_stops):
    counter = 0
    for pair in bus_stops:
        single_counter = pair[0] - pair[1]
        counter += single_counter
    print(counter)


number([[10, 0], [3, 5], [5, 8]])#, 5)
number([[3, 0], [9, 1], [4, 10], [12, 2], [6, 1], [7, 10]])#, 17)
number([[3, 0], [9, 1], [4, 8], [12, 2], [6, 1], [7, 8]])#, 21)

# index 0 steigt zu. index 1 steigt aus.