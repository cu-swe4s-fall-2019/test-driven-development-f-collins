import math

def list_mean(L):
    if L == None:
        return None

    for l in L:
        if not isinstance(l, (int, float)):
            print("Non number " + l + " in list, dropping.")
            L.remove(l)

    if len(L) == 0:
        return None

    return sum(L)/len(L)

def list_stdev(L):
    if L == None:
        return None
    if len(L) == 0:
        return None

    mean = list_mean(L)

    stdev = 0

    for l in L:
        stdev += (l - mean) ** 2

    return math.sqrt((1 / len(L)) * stdev)




