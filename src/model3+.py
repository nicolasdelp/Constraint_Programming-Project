from pycsp3 import *

# V = nombre de sommets | E = nombre d'arêtes | edges = les arètes
V, E, edges = data

# Valeur par défaut du cyclic-bandwidth
k = 1

# lecture de k
k = int(sys.argv[1])