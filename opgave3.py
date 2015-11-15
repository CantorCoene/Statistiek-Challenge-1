# Nodige imports
import statistics, functions, math, numpy
import matplotlib.pyplot as plt

# We lezen de data.
data = numpy.loadtxt('gr7.txt')

# Bereken en oplijsten van de waarden voor de hoeken die we zoeken.
try:
    hoek_list = []
    for l in data:
        # Uitfilteren nulwaarden.
        if int(l[0]) is not 0 and int(l[2]) is not 0:
            # Bereken y2 en y1 door gebruik te maken van de discrete hoogte van de sensor.
            y2 = float(l[3])*0.1 - 0.05
            y1 = float(l[1])*0.1 - 0.05

            # We gebruiken de gegeven posities van de detectiestrips.
            x1 = 4.4
            x2 = 10.7

            # Bereken de richtingscoëficient van de baan van het deeltje.
            hoek = math.atan2((y2 - y1),(x2 - x1))
            hoek_list.append(hoek)
        else:
            # Deze waarden mogen niet meegerekend worden en dan gaan we naar de volgende.
            continue        
except:
    print('Something went wrong while calculating the angle values.')

# Ter controle of waarden steek houden, berekenen we de gemiddelden van de hoeken.
average = functions.arit_average(hoek_list)
resolution = statistics.stdev(hoek_list)
print('Gemiddelde hoek is: {} rad.\n'
      'Resolutie hoek is: {} rad.\n'
      .format(average, resolution))
# Einde controle.

# We maken een histogramplot van de waarden voor de hoeken.
plt.hist(hoek_list)
plt.title("Histogram van angulaire verdeling")
plt.xlabel("Hoek (rad)")
plt.ylabel("Frequentie")
plt.show() 
