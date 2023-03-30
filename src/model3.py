from pysat.solvers import Glucose4
from pysat.formula import CNF
import json
import sys

# Choix du solveur
solver = Glucose4()

# Lecture des données depuis le fichier Json
data = json.load(open(sys.argv[2], 'r'))

V = data['V']
E = data['E']
edges = data['edges']

# Lecture de la valeur de k
k = int(sys.argv[1])

def cyclic_bandwidth_problem(n, E, edges, k):

    # Création de la formule CNF
    cnf = CNF()
    
    # Création des variables booléennes
    variables = {}
    for i in range(1, n+1):
        for j in range(1, n+1):
            variables[(i, j)] = len(variables) + 1
    
    # Contrainte 1 : T est toujours vrai
    cnf.append([variables[(1, 1)]])
    
    # Contrainte 2 : Au moins une étiquette pour chaque sommet
    for i in range(1, n+1):
        clause = []
        for j in range(1, n+1):
            clause.append(variables[(i, j)])
        cnf.append(clause)
    
    # Contrainte 3 : Deux sommets éloignés de plus de k ne peuvent pas avoir la même étiquette
    for i in range(1, n+1):
        for j in range(1, n+1):
            for h in range(1, n+1):
                if h != i:
                    for d in range(1, k+1):
                        if j-d >= 1:
                            cnf.append([-variables[(i, j)], -variables[(h, j-d)]])
                        if j+d <= n:
                            cnf.append([-variables[(i, j)], -variables[(h, j+d)]])
    
    # Contrainte 4 : Deux sommets adjacents ne peuvent pas avoir des labels incompatibles
    for (u, v) in E:
        for i in range(1, n+1):
            for j in range(1, n+1):
                if not edges[u][v][(i-1)%n][(j-1)%n]:
                    cnf.append([-variables[(u, i)], -variables[(v, j)]])
    
    # Contrainte 5 : Éviter les contraintes redondantes
    for i in range(1, n+1):
        for j in range(1, n+1):
            for k in range(1, n+1):
                if k != j:
                    cnf.append([-variables[(i, j)], -variables[(i, k)]])
    
    # Ajout de la variable y pour la satisfaction des contraintes
    y = len(variables) + 1
    cnf.append([y])
    for i in range(1, n+1):
        for j in range(1, n+1):
            cnf.append([-y, variables[(i, j)]])
    
    # Création du solveur et résolution du problème
    solver = Glucose4()
    solver.append_formula(cnf)
    if solver.solve():
        print("La contrainte de cyclic-bandwidth k =", k, "est satisfaite")
        # Récupération de la solution
        solution = []
        for i in range(1, n+1):
            for j in range(1, n+1):
                if solver.model[variables[(i, j)]-1] > 0:
                    solution.append((i, j))
        print("Sat")
    else:
        print("La contrainte est insatisfaite")

e = cyclic_bandwidth_problem(V, E, edges, k)
print(e)