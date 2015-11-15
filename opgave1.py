# Nodige imports
import statistics, functions, numpy
import matplotlib.pyplot as plt

# We lezen de data.
data = numpy.loadtxt('gr7.txt')

# We maken een lijst aan met alle ys waarden.
try:
    ys_list = []
    for l in data:
        # We filteren de nulwaarden uit de data.
        if int(l[0]) is not 0 and int(l[2]) is not 0:
            # Bereken y2 en y1 door gebruik te maken van de discrete hoogte van de sensor.
            y2 = float(l[3])*0.1-0.05
            y1 = float(l[1])*0.1-0.05
            # We beschouwen de posities van de sensorstrips.
            x1 = 4.4
            x2 = 10.7
            # Bereken de richtingscoëficient van de baan van het deeltje.
            rico = (y2 - y1)/(x2 - x1)
            # Los de vergelijking op van de richtingscoëficient maar nu met de punten (0,ys) en (x1, y1)
            ys = y1 - rico*x1
            ys_list.append(ys)
        else:
            # Deze waarden mogen niet meegerekend worden en dan gaan we naar de volgende.
            continue
except:
    print('Something went wrong while calculating the ys values.')

# We bereken het gemiddelde en de resolutie van de lijst van ys-waarden en laten deze weergeven als output.
resolutie = statistics.stdev(ys_list)
gemiddelde = functions.arit_average(ys_list)
print('De gemiddelde waarde voor de positie van de bron is: {} cm.\n'
      'De resolutie van de data is: {} cm.\n'
      .format(gemiddelde, resolutie))

# We plotten de waarden van ys volgens een histogram.
plt.hist(ys_list)
plt.title("Histogram van bronhoogte")
plt.xlabel("Hoogte (cm)")
plt.ylabel("Frequentie")
plt.show()



