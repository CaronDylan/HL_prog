import time


def era(nb) :
    ind = 0
    l = [a for a in range(2,nb+1)]
    while max(l) != l[ind] :
        for cpt in l :
            if (cpt != (l[ind]) and cpt % (l[ind]) == 0) :
                l.remove(cpt)
        ind = ind+1
    return (l)

def era2(nb) :
    l = [2]
    insert = True
    for cpt in [a for a in range(3,nb+1)] :
        for a in l :
            if (cpt % a == 0) :
                insert = False
        if(insert) :
                l.append(cpt)
        insert = True
    return(l)

deb = time.time()
print(era2(10000))
fin = time.time()
print(fin - deb)
