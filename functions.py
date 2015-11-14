# Neemt een string van getallen die uit elkaar gezet zijn door '\t' en geef een lijst met die getallen terug.
def getnumbers(arg_string):
    lister = list(arg_string)
    st = ''
    retu = []
    for s in lister:
        if s.isspace():
            retu.append(st)
            st = ''

        else:
            st += s
    retu.append(st)
    return retu

# Gegeven een lijst met floats, int's geeft deze functie het rekenkundig gemiddelde.
def arit_average(arg_list):
    av = 0
    for i in arg_list:
        av += i
    av = av/len(arg_list)
    return av

# Geeft een set terug van strings van de vorm 'Waarde   frequentieVanWaarde', gegeven een lijst van waarden.
def makeCountedList(arg_list):
     countedlist = set([])

     for var in arg_list:
         c = arg_list.count(var)
         countedlist.add('{}\t{}'.format(var, c))

     return countedlist
