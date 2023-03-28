from pycsp3 import *

# V = nombre de sommets | E = nombre d'arêtes | edges = les arètes
V, E, edges = data

# Valeur par défaut du cyclic-bandwidth (largeur max de la bande cyclique)
k = 10 

# Variables de décision
x = VarArray(size=V, dom=range(V))

# Table de contraintes pour le problème. Cette table contient tous les paires (i, j) 
# de sommets tels que la distance cyclique entre i et j (c'est-à-dire la distance minimale sur le cycle)
# est inférieure ou égale à k. Cette table est utilisée dans la contrainte 2
table = {
    (i, j) for i in range(V) 
                for j in range(V)
                    if min(abs(i - j), V - abs(i - j)) <= k and i != j
        }


satisfy(
    # Assure que chaque variable x[i] est différente des autres variables x[j]
    AllDifferent(x),
    # Vérifie que toutes les arêtes du graphe (représentées par la liste d'arêtes "edges") sont telles que
    # la paire (x[i], x[j]) est présente dans la table de contraintes définie précédemment.
    [(x[i], x[j]) in table for i, j in edges]
    
)