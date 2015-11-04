# Nodige imports
import statistics, functions

# Open de data.
data = open('gr7.txt', 'r')
data_string = data.read()  # Slaag de data op en een string
data_split = data_string.splitlines()  # Maak een lijst aan waarvan elk element een string is die de respectievelijke lijnen voorsteld.
data_lines = list(map(functions.getnumbers, data_split))  # Op deze lijst voeren we de getnumbers functie. Zie functie.py voor uitleg
data.close()  # Sluit de file voor geheugen gebruik

# We maken een lijst aan met alle ys waarden.
try:
    ys_list = []
    for l in data_lines:
        # Berken y2 en y1 door gebruik te maken van de discrete hoogte van de sensor.
        y2 = int(l[3])*0.1
        y1 = int(l[1])*0.1

        # Gebruik de gegeven waarde voor de afstanden van de sensorplaat.
        x2 = 10.7
        x1 = 4.4

        # Bereken de richtingscoëficient van de baan van het deeltje.
        rico = (y2 - y1)/(x2 - x1)

        # Los de vergelijking op van de richtingscoëficient maar nu met de punten (0,ys) en (x1, y1)
        ys = y1 - rico*x1
        ys_list.append(ys)
except:
    print('Something went wrong while calculating the ys values.')


resolutie = statistics.stdev(ys_list)  # Bereken de standaard afwijking op de waarden van ys.
gemmidelde = functions.arit_average(ys_list)  # Bereken de gemmiddelde ys


print('De gemmidelde waarde voor de positie van de bron is: {} cm.\n'
      'De resolutie van de data is: {}\n'
      .format(gemmidelde, resolutie))  # Print de waarden uit naar de terminal.

# We schrijven de waarden van ys en hun frequentie uit op een .dat bestand voor GNUplot.
counted_ys = list(functions.makeCountedList(ys_list))  # Maak een countedlist van ys waarden. Zie functions voor uitleg.
try:

    gr7dat = open('gr7dat.dat', 'w')  # Maak een bestand aan gr7dat.dat

    # Maak de string aan de we in de file gaan writen.
    sgr7dat = ''
    for i in counted_ys:
        sgr7dat += i
        sgr7dat += '\n'  # Zorg dat na het toevoegen van de counted ys strings we een nieuwe lijn starten.
    gr7dat.write(sgr7dat)
    print('\nPrinted ys data onto gr7dat.dat')  # Zodat we weten dat het bestand is aangemaakt.
    gr7dat.close() 
except:
    print('Error when printing data onto .dat file')
    gr7dat.close()




