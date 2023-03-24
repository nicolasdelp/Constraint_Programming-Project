from pycsp3 import *

# V = nombre de sommets | E = nombre d'arêtes | edges = les arètes
V, E, edges = data

# Variables de décision
x = VarArray(size=V, dom=range(V))

# Contraintes
satisfy(
    AllDifferent(x)
)

# Fonction objectif
minimize(
   Maximum(Minimum(abs(x[i] - x[j]), V - abs(x[i] - x[j])) for i, j in edges)
)
