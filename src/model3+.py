import pysat.formula as f
from pysat.solvers import Glucose4
import sys
import json

# Choix du solveur
solver = Glucose4()

# Lecture des données depuis le fichier Json
data = json.load(open(sys.argv[2], 'r'))

V = data['V']
E = data['E']
edges = data['edges']

# Lecture de la valeur de k
k = int(sys.argv[1])