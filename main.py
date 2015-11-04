# Nodige imports
import statistics


# We maken een file variable aan die de data in de txt file opslaagd.
data_file = open('testdata.txt', 'r')

# We slagen de volledige data op in een string, en maken daarna een lijst met de verschillende lijnen.
data_string = data_file.read()
data_list = data_string.splitlines()

# Om al de waarden voor y_s te krijgen maken we een for lus die over alle elementen gaat van data_list
# Alle waarden voor y_s slagen we op in een lijst.
y_s_list = []
for lines in data_list:
    try:
        # omdat onze line variabele van de volgende vorm is:
        # "n1\tp1\tn2\tp2"
        # vinden we dat p1 = line[2] en p2 = line[6]
        y2 = float(lines[6])*0.1
        y1 = float(lines[2])*0.1

        X2 = 10.7 # Waarde voor groep 7
        X1 = 4.4

        rico = (y2 - y1)/(X2 - X1)

        y_s = y1 - (X1*rico)

        y_s_list.append(y_s)
    except:
        print("Er liep iets fout bij de berekening van y_s in de for lus.")
        break

# We berekenen de standaard afwijking met de statistics package uit python 3.4.
y_s_std = statistics.stdev(y_s_list)

print(str(y_s_std)) # Even testen of de waarden correct zijn.

