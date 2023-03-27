from pycsp3 import *

# V = nombre de sommets | E = nombre d'arêtes | edges = les arètes
V, E, edges = data

# Valeur par défaut du cyclic-bandwidth
k = 10 

# Variables de décision
x = VarArray(size=V, dom=range(V))

table = {
    (i, j) for i in range(V) 
                for j in range(V)
                    if min(abs(i - j), V - abs(i - j)) <= k and i != j
        }

satisfy(
    AllDifferent(x),
    [(x[i], x[j]) in table for i, j in edges]
    (x[0] == 0)  # on peut fixer la position du premier sommet à 0 sans perte de généralité
)