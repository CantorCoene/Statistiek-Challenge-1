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

# Gegeven een lijst met floats, int's geeft deze functie het rekenkundig gemmidelde.
def arit_average(arg_list):
    av = 0
    for i in arg_list:
        av += i
    av = av/len(arg_list)
    return av

# Geeft een set terug van strings van de vorm 'frequentieVanWaarde   Waarde'. Gegeven een lijst van waarden.
def makeCountedList(arg_list):
     countedlist = set([])

     for ys in arg_list:
         c = arg_list.count(ys)
         countedlist.add('{}\t{}'.format(c, ys))

     return countedlist

