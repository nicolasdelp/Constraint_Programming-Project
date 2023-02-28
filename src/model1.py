from pycsp3 import *

n, E, edges = data


# Nos étiquettes
etiq = [i+1 for i in range(n)] 

# Variables de décision

e = VarArray(size=n, dom=etiq) # Domaine
print("Domain of any variable: ", e[0].dom)

# Contraintes

satisfy(
    AllDifferent(e)
)

# Fonction objectif
minimize(
    Maximum( min( abs( e[i]-e[j], n - abs( e[i]-e[j] )) for i,j in n))
)
