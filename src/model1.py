from pycsp3 import *

# Instance didactique
n = 5


# Nos étiquettes
etiq = [i+1 for i in range(n)] 

# Variables de décision

e = VarArray(size=n, dom=etiq) # Domaine
print("Domain of any variable: ", e[0].dom)

# Contraintes

satisfy(
    AllDifferent(e)
);

# Fonction objective
minimize(
    Maximum( min( abs( e[i]-e[j], n - abs( e[i]-e[j] )) for i,j in n))
)
print(objective())