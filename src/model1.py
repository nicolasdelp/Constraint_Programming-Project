from pycsp3 import *

n, E, edges = data

# Variables de décision
x = VarArray(size=n, dom=range(n))

# Contraintes
satisfy(
    AllDifferent(x)
)

# Fonction objectif
minimize(
   Maximum(Minimum(abs(x[u] - x[v]), n - abs(x[u] - x[v])) for u, v in edges)
)