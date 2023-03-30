import json
import time
import sys
from pysat.solvers import Glucose4

# Lecture des données depuis le fichier Json
data = json.load(open(sys.argv[2], 'r'))
V = data['V']
E = data['E']
edges = data['edges']

# Lecture de la valeur de k
k = int(sys.argv[1])

# Début du timer
start = time.time()

# Créer un solveur SAT
solver = Glucose4()

# Créer une variable booléenne pour chaque permutation possible des sommets
perms = {}
for i in range(V):
    for j in range(V):
        perms[(i, j)] = solver.nof_vars()

# Contraintes de domaine: chaque variable doit être soit vraie, soit fausse
for i in range(V):
    for j in range(V):
        solver.add_clause([perms[(i, j)], -perms[(i, j)]])

# Contraintes de cycle: chaque sommet doit apparaître exactement une fois dans chaque cycle
for i in range(V):
    cycle_vars = []
    for j in range(V):
        cycle_vars.append(perms[(i, j)])
    solver.add_clause(cycle_vars)

# Contraintes de largeur de bande: pour chaque arête, la différence entre les positions de ses extrémités
# doit être inférieure ou égale à k
for edge in edges:
    u, v = edge
    for i in range(V):
        for j in range(V):
            if i < j:
                if (i == u and j == v) or (i == v and j == u):
                    continue
                # Si les deux sommets ne sont pas voisins dans l'arête, leur différence doit être supérieure à k
                if abs(i - j) > k + 1:
                    solver.add_clause([-perms[(i, u)], -perms[(j, v)]])
                    solver.add_clause([-perms[(i, v)], -perms[(j, u)]])
                # Sinon, leur différence doit être inférieure ou égale à k
                else:
                    solver.add_clause([perms[(i, u)], perms[(j, v)]])
                    solver.add_clause([perms[(i, v)], perms[(j, u)]])

# Vérifier si le problème est satisfaisable
if solver.solve():
    print("Le problème est satisfaisable.")
else:
    print("Le problème est insatisfaisable.")

end = time.time()
print("Temps d'execution :", end - start)