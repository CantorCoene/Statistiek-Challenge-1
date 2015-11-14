# Nodige imports
import statistics, functions, math
import matplotlib.pyplot as plt

# Open de data.
data = open('gr7.txt', 'r')
data_string = data.read()  # Slaag de data op en een string
data_split = data_string.splitlines()  # Maak een lijst aan waarvan elk element een string is die de respectievelijke lijnen voorsteld.
data_lines = list(map(functions.getnumbers, data_split))  # Op deze lijst voeren we de getnumbers functie. Zie functie.py voor uitleg
data.close()  # Sluit de file voor geheugen gebruik

# Bereken en oplijsten van de waarden voor de hoeken die we zoeken.
try:
    hoek_list = []
    for l in data_lines:
        # Uitfilteren nulwaarden.
        if int(l[1]) is not 0 and int(l[3]) is not 0:
            # Bereken y2 en y1 door gebruik te maken van de discrete hoogte van de sensor.
            y2 = float(l[3])*0.1 - 0.05
            y1 = float(l[1])*0.1 - 0.05

            # Bereken de richtingscoëficient van de baan van het deeltje.
            hoek = math.atan2((y2 - y1),(10.7 - 4.4)) # x-positie van de strips in de noemer
            hoek_list.append(hoek)
        else:
            # Deze waarden mogen niet meegerekend worden en dan gaan we naar de volgende.
            continue        
except:
    print('Something went wrong while calculating the angle values.')

# Ter controle of waarden steek houden, berekenen we de gemiddelden vaan de hoeken.
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
