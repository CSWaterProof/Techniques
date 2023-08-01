from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import maximum_bipartite_matching
# This function implements the Hopcroft–Karp algorithm

graph = csr_matrix([[0, 0, 1], [1, 1, 0]])
print(maximum_bipartite_matching(graph, perm_type='column'))

print(maximum_bipartite_matching(graph, perm_type='row'))
