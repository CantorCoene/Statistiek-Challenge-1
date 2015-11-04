# Nodige imports
import statistics, functions

# Open de data en slaag de informatie op in een lijst van strings.
# Elk lijstelement is een lijn uit de data.
data = open('gr7.txt', 'r')
data_string = data.read()
data_split = data_string.splitlines()
data_lines = list(map(functions.getnumbers, data_split))

ys_list = []
for l in data_lines:
    y2 = int(l[3])*0.1
    y1 = int(l[1])*0.1

    x2 = 10.7
    x1 = 4.4

    rico = (y2 - y1)/(x2 - x1)

    ys = y1 - rico*x1
    ys_list.append(ys)

resolutie = statistics.stdev(ys_list)
print(resolutie)
