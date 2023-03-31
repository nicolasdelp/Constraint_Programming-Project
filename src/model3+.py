import json
from pysat.solvers import Glucose4, Solver
from pysat.formula import CNF
import time
import sys
import numpy as np


solve = False

# Lecture des données depuis le fichier Json
data = json.load(open(sys.argv[2], 'r'))
V = data['V']
E = data['E']
edges = data['edges']


# Lecture de la valeur de k
k = int(sys.argv[1])


# Début du timer
start = time.time()


# Initialisatio du solveur
solver = Glucose4()


# Initialisation de la variable booléenne X[i][j]
X = [[False for i in range(V)] for j in range(V)]

 
P = np.full((V, V), False)
for i in range(V):
    for j in range(V):
        if min(abs(j - i), V - abs(j - i)) <= k:
            P[i][j] = True

# Initialisation des clauses
cnf = CNF()


# Ajout des clauses pour chaque sommet i
for i in range(V):
    # chaque sommet doit avoir au moins une étiquette
    clause = [X[i][j] for j in range(V)]
    cnf.append(clause)
    
    # chaque étiquette j ne peut être utilisée qu'une seule fois pour tous les sommets i
    for j1 in range(V):
        for j2 in range(j1+1, V):
            clause = [-X[i][j1], -X[i][j2]]
            cnf.append(clause)


# Ajout des clauses pour chaque étiquette j
for j in range(V):
    # chaque étiquette j doit être assignée à un et un seul sommet i
    clause = [X[i][j] for i in range(V)]
    cnf.append(clause)
    
    # chaque sommet i ne peut avoir qu'une seule étiquette assignée
    for i1 in range(V):
        for i2 in range(i1+1, V):
            clause = [-X[i1][j], -X[i2][j]]
            cnf.append(clause)




# Ajout des clauses pour chaque paire de sommets (i, j) telle que i != j
for i in range(V):
    for j in range(V):
        if i != j:
            # chaque paire de sommets (i, j) ne peut pas être éloignée de plus de k
            for l in range(1, k+1):
                if j+l < V:
                    cnf.append([-X[i][j], -X[j+l][i]])
                if i+l < V:
                    cnf.append([-X[i][j], -X[j][i+l]])



# Deux sommets éloignés de plus de k ne peuvent pas avoir la même étiquette
# (pour chaque paire de sommets i et j différents, si la distance 
# entre eux est supérieure à k, alors pour tout entier k entre 1 et k,
# il ne peut pas être vrai que les sommets i et j ont l'étiquette k.
for i in range(V-1):
    for j in range(V-1):
        if i != j:
            for k in range(1, V-1):
                    if k != i:
                        cnf.append([-X[i][k-1], -X[j][(k-1)]])

P = np.full((V, V), False)
for i in range(V):
    for j in range(V):
        if min(abs(j - i), V - abs(j - i)) <= k:
            P[i][j] = True
            X[i][j] = True

#Résultat
if solver.solve():
    print("Le problème est satisfaisable.")
else:
    print("Le problème est insatisfaisable.")

# Afficher le temps d'exécution
end = time.time()
print("Temps d'execution :", end - start)