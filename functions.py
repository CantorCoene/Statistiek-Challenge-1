# Gegeven een lijst met floats, int's geeft deze functie het rekenkundig gemiddelde.
def arit_average(arg_list):
    av = 0
    for i in arg_list:
        av += i
    av = av/len(arg_list)
    return av
