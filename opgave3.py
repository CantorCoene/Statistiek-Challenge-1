# Nodige imports
import statistics, functions, math
import matplotlib.pyplot as plt

# Open de data.
data = open('gr7.txt', 'r')
data_string = data.read()  # Slaag de data op en een string
data_split = data_string.splitlines()  # Maak een lijst aan waarvan elk element een string is die de respectievelijke lijnen voorsteld.
data_lines = list(map(functions.getnumbers, data_split))  # Op deze lijst voeren we de getnumbers functie. Zie functie.py voor uitleg
data.close()  # Sluit de file voor geheugen gebruik

# Eventueel werken met gemiddelde ys, hier nog eens de berekening.
try:
    hoek_list = []
    for l in data_lines:
        # Uitfilteren nulwaarden.
        if int(l[1]) is not 0 and int(l[3]) is not 0:
            # Bereken y2 en y1 door gebruik te maken van de discrete hoogte van de sensor.
            y2 = int(l[3])*0.1 - 0.05
            y1 = int(l[1])*0.1 - 0.05

            # Gebruik de gegeven waarde voor de afstanden van de sensorplaat.
            x2 = 10.7
            x1 = 4.4

            # Bereken de richtingscoëficient van de baan van het deeltje.
            hoek = math.atan2((y2 - y1),(x2 - x1))
            hoek_list.append(hoek)
        else:
            # Deze waarden mogen niet meegerekend worden en dan gaan we naar de volgende.
            l += l        
except:
    print('Something went wrong while calculating the angle values.')

# Ter controle of waarden ergens steek houden, berekenen we de gemiddelden vaan de hoeken.
average = functions.arit_average(hoek_list)
resolution = statistics.stdev(hoek_list)

print('Gemiddelde hoek is: {} graden.\n'
      'Resolutie hoek is: {} graden.\n'
      .format(average, resolution))
# Einde controle.


# We schrijven de waarden van de hoeken uit op een .dat bestand voor verder gebruik.
counted_hoek = list(functions.makeCountedList(hoek_list))
try:

    gr7dat2 = open ('gr7dat2.dat', 'w')

    sgr7dat2 = ''
    for i in counted_hoek:
        sgr7dat2 += i
        sgr7dat2 += '\n'
    gr7dat2.write(sgr7dat2)
    print('\nPrinted angle data onto gr7dat2.dat')
    gr7dat2.close()
except:
    print('Error')
    gr7dat2.close()

# We maken een histogramplot van de waarden voor de hoeken.
try:
    plt.hist(hoek_list)
    plt.title("Histogram van angulaire verdeling")
    plt.xlabel("Hoek (rad)")
    plt.ylabel("Frequentie")
    plt.show()
    print('\nPlot made succesfully')
except:
    print('\n Something went wrong while plotting')
    
