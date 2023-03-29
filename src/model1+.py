from pycsp3 import *

# V = nombre de sommets | E = nombre d'arêtes | edges = les arètes
V, E, edges = data

# Variables de décision
x = VarArray(size=V, dom=range(V))

# Contraintes (avec élimination des symétries)
satisfy(
    x[0] == 1,
    x[2] < x[V-1],
    AllDifferent(x)
)
# Fonction objectif
minimize(
   Maximum(Minimum(abs(x[u] - x[v]), V - abs(x[u] - x[v])) for u, v in edges)
)
