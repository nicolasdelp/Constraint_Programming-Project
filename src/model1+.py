from pycsp3 import *

# V = nombre de sommets | E = nombre d'arêtes | edges = les arètes
V, E, edges = data

# Variables de décision
x = VarArray(size=V, dom=range(V))

# Contraintes (avec élimination des symétries)
satisfy(
    # fixe la position du premier sommet à 1
    x[0] == 1,
    # élimine les solutions symétriques dans lesquelles le premier sommet est placé à la position V-1 et le troisième sommet est placé à la position 2
    x[2] < x[V-1],
    AllDifferent(x)
)
# Fonction objectif
minimize(
   Maximum(Minimum(abs(x[u] - x[v]), V - abs(x[u] - x[v])) for u, v in edges)
)
