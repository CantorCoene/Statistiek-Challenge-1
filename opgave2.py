# Nodige imports
import numpy
import matplotlib.pyplot as plt

# We lezen de data.
y1, x1, y2, x2 = numpy.loadtxt('gr7.txt', unpack=True)

# Opmerking: we moeten nulwaarden hier niet uitfilteren, deze zullen een staaf met hoogte nul definiëren.

# Eerste strip.
plt.bar(x1, y1, width=.35, align='center')
plt.title("Staafdiagram van hits bij eerste strip")
plt.xlabel("Pixel")
plt.ylabel("Aantal hits")
plt.show(block=False)

# Tweede strip.
plt.bar(x2, y2, width=.35, align='center')
plt.title("Staafdiagram van hits bij tweede strip")
plt.xlabel("Pixel")
plt.ylabel("Aantal hits")
plt.show(block=False)

# Volledige detector.    

# Input code here

plt.bar(xd, yd, width=.35, align='center')
plt.title("Staafdiagram van hits bij volledige detector")
plt.xlabel("Pixel")
plt.ylabel("Aantal hits")
plt.show(block=False)
    
