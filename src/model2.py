from pycsp3 import *

k = 1 # Valeur par défaut du cyclic-bandwidth

# On vérifie si k n'a pas été donné comme entrée (présence de k=<un nombre> à l'appel de
# model2.py). Si c'est le cas, on prendra alors le k donné au lieu de celui par défaut
expr_k = "k=[0-9]+"
rule = re.compile(expr_k)
for arg in sys.argv[1:]:
    if rule.match(arg):
        k = int(arg.split("=")[1])

n, E, edges = data

x = VarArray(size=n, dom=range(n))

table = {(i, j) for i in range(n) for j in range(n)
                if min(abs(i - j), n - abs(i - j)) <= k
                   and i != j}

satisfy(
    AllDifferent(x),
    [(x[u], x[v]) in table for u, v in edges]
)