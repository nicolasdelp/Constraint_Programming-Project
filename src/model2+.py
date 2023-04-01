from pycsp3 import *

# V = nombre de sommets | E = nombre d'arêtes | edges = les arètes
V, E, edges = data

# Valeur par défaut du cyclic-bandwidth (largeur max de la bande cyclique)
k = 1

# lecture de k
k = int(sys.argv[1])

# Variables de décision
x = VarArray(size=V, dom=range(V))

# Table de contraintes pour le problème. 
# Cette table contient tous les paires (i, j) de sommets tels que la distance cyclique entre i et j 
# (c'est-à-dire la distance minimale sur le cycle) est inférieure ou égale à k.
table = {
    (i, j) for i in range(V) 
                for j in range(V)
                    if min(abs(i - j), V - abs(i - j)) <= k and i != j
        }

# Contraintes (avec élimination des symétries)
satisfy(
    # fixe la position du premier sommet à 1
    x[0] == 1,
    # élimine les solutions symétriques dans lesquelles le premier sommet est placé à la position V-1 et le troisième sommet est placé à la position 2
    x[2] < x[V-1],
    AllDifferent(x),
    [(x[u], x[v]) in table for u, v in edges]
)