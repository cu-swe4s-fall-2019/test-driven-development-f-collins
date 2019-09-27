
def list_mean(L):
    if L == None:
        return None

    for l in L:
        if not isinstance(l, (int, float)):
            print("None number " + l + " in list, dropping.")
            L.remove(l)

    if len(L) == 0:
        return None

    return sum(L)/len(L)

def list_stdev(L):
    if L == None:
        return None
    if len(L) == 0:
        return None
