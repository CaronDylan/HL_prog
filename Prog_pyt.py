#Programme réalisé par: CARON Dylan
#Groupe : BROHAN Romain, GASCOIN Samy, CARON Dylan
#Version peu efficace (voir pas du tout)

def era(nb) :
    #Initialisation
    l = [2] #Je stocke le 1er nombre premier
    insert = True
    #On parcours tous les nombre entre 3 et celui passé en paramètre
    for cpt in [a for a in range(3,nb+1)] :
        #On test la divisiblité du nombre en cours (cpt) par les nombres premiers déjà stockés
        for a in l :
            #Si le nombre en cours est divisible par au moins un nombre premier alors on passe Insert à Faux et on ne l'insère pas
            if (cpt % a == 0) :
                insert = False
        if(insert) :
                l.append(cpt)
        #Ré-initialisation de la variable d'insertion
        insert = True
    return(l)
