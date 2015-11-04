# Neemt een string van getallen die gesplits zijn door '/t' en geeft de getallen in een lijst terug.
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
