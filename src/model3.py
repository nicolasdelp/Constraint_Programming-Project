from pycsp3 import *

# V = nombre de sommets | E = nombre d'arêtes | edges = les arètes
V, E, edges = data

# Valeur par défaut du cyclic-bandwidth
k = 10 

# Variables booléennes
x = [[ Var(id=f"x_{i}_{j}", dom=[False, True]) for j in range(V)] for i in range(V)]

# Contrainte de présence
cnf = CNF()
for i in range(V):
    clause = [x[i][j] for j in range(V)]
    cnf.append(clause)

# Contrainte de différence
for i in range(V):
    for j in range(i+1, V):
        for k in range(V):
            clause1 = [-x[i][k], -x[j][(k + i - j) % V]]
            clause2 = [-x[j][k], -x[i][(k + j - i) % V]]
            cnf.append(clause1)
            cnf.append(clause2)

# Contrainte de bande passante cyclique
for (i, j) in edges:
    for d in range(-k, k+1):
        if d != 0:
            clause = [-x[i][(j + d) % V], -x[j][(i + d) % V]]
            cnf.append(clause)

# Résolution du problème en utilisant Glucose 4
with Glucose3(bootstrap_with=cnf) as solver:
    if solver.solve():
        model = solver.get_model()
        solution = [0] * V
        for i in range(V):
            for j in range(V):
                if model[x[i][j]-1] > 0:
                    solution[j] = i
        print("Solution:", solution)
    else:
        print("Le problème est insatisfaisable")



# TODO
# Utiliser la table inverse pour être en CNF
# Trouver une propriété pour optimiser OU dicotomie
# Mettre le solveur dans le model
# py model1.py -data="..." -model=""