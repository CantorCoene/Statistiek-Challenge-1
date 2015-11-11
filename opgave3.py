# Nodige imports
import statistics, functions, math

# Open de data.
data = open('gr7.txt', 'r')
data_string = data.read()  # Slaag de data op en een string
data_split = data_string.splitlines()  # Maak een lijst aan waarvan elk element een string is die de respectievelijke lijnen voorsteld.
data_lines = list(map(functions.getnumbers, data_split))  # Op deze lijst voeren we de getnumbers functie. Zie functie.py voor uitleg
data.close()  # Sluit de file voor geheugen gebruik

# Eventueel werken met gemiddelde ys, hier nog eens de berekening.
try:
    ys2_list = []
    for l in data_lines:
        # Bereken y2 en y1 door gebruik te maken van de discrete hoogte van de sensor.
        y2b = int(l[3])*0.1 - 0.05
        y1b = int(l[1])*0.1 - 0.05

        # Gebruik de gegeven waarde voor de afstanden van de sensorplaat.
        x2 = 10.7
        x1 = 4.4

        # Bereken de richtingscoëficient van de baan van het deeltje.
        rico = (y2b - y1b)/(x2 - x1)

        # Los de vergelijking op van de richtingscoëficient maar nu met de punten (0,ys) en (x1, y1)
        ys2 = y1b - rico*x1
        ys2_list.append(ys2)
except:
    print('Something went wrong while calculating the ys values.')


resolutie2 = statistics.stdev(ys2_list)  # Bereken de standaard afwijking op de waarden van ys.
gemiddelde2 = functions.arit_average(ys2_list)  # Bereken de gemiddelde ys


print('De gemidelde waarde voor de positie van de bron is: {} cm.\n'
      'De resolutie van de data is: {} cm.\n'
      .format(gemiddelde2, resolutie2))  # Print de waarden uit naar de terminal.

# We schrijven de waarden van ys en hun frequentie uit op een .dat bestand voor GNUplot.
counted_ys2 = list(functions.makeCountedList(ys2_list))  # Maak een countedlist van ys waarden. Zie functions voor uitleg.
try:

    gr7dat2 = open('gr7dat2.dat', 'w')  # Maak een bestand aan gr7dat2.dat

    # Maak de string aan de we in de file gaan writen.
    sgr7dat2 = ''
    for i in counted_ys:
        sgr7dat += i
        sgr7dat += '\n'  # Zorg dat na het toevoegen van de counted ys strings we een nieuwe lijn starten.
    gr7dat2.write(sgr7dat2)
    print('\nPrinted ys data onto gr7dat2.dat')  # Zodat we weten dat het bestand is aangemaakt.
    gr7dat2.close() 
except:
    print('Error when printing data onto .dat file')
    gr7dat2.close()

# We maken twee lijsten met waarden voor de hoeken, respectievelijk vanuit de eerste en de tweede strip gezien.
try:
    #hoek1_list = []
    hoekk2_list = []
    for l in data_lines:
        # Bereken y2 en y1 door gebruik te maken van de discrete hoogte van de sensor.
        y2 = int(l[3])*0.1 - 0.05
        #y1 = int(l[1])*0.1 - 0.05

        # Herdefinieer het nulpunt als zijnde de hoogte van de bron (ys).
        yb = y2 - gemiddelde
        #ya = y1 - gemiddelde

        # Gebruik de gegeven waarde voor de afstanden van de sensorplaat.
        x2 = 10.7
        x1 = 4.4

        # Bereken de hoek gemeten vanuit de bron met de waarnemende pixel van de detector in graden.
        #hoek1 = math.atan2(ya, x1)
        #h1 = math.degrees(hoek1)
        hoek2 = math.atan2(yb, x2)
        h2 = math.degrees(hoek2)
        #hoek1_list.append(h1)
        hoekk2_list.append(h2)

except:
    print('Something went wrong while calculating.')

# Ter controle of waarden ergens steek houden, berekenen we de gemiddelden vaan de hoeken.
#average = functions.arit_average(hoek1_list)
averagee = functions.arit_average(hoekk2_list)
#resolution = statistics.stdev(hoek1_list)
resolutionn = statistics.stdev(hoekk2_list)

print(#'Gemiddelde hoek 1 is: {} graden.\n'
      'Gemiddelde hoek 2 is: {} graden.\n'
      #'Resolutie hoek 1 is: {} graden.\n'
      'Resolutie hoek 2 is: {} graden.\n'
      .format(averagee, resolutionn))
# Einde controle.


# We schrijven de waarden van de hoeken uit op een .dat bestand voor verder gebruik.


        
    
