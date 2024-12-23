import bisect

def read_input(file_path):
  with open(file_path, 'r') as file:
    return file.readlines()

if __name__ == "__main__":
  edges = list(map(lambda x: x.strip().split('-'), read_input("day23/input")))

  nodes = set()
  for edge in edges:
    nodes.add(edge[0])
    nodes.add(edge[1])

  nodes = list(nodes)
  nodes.sort()

  def index(a, x):
    'Locate the leftmost value exactly equal to x'
    i = bisect.bisect_left(a, x)
    if i != len(a) and a[i] == x:
      return i
    raise ValueError

  n = len(nodes)
  adj = [[] for _ in range(n)]
  for edge in edges:
    u = index(nodes, edge[0])
    v = index(nodes, edge[1])
    adj[u].append(v)
    adj[v].append(u)
  
  # find the maximal clique of adj
  def bron_kerbosch(R, P, X, adj, cliques):
    if not P and not X:
      cliques.append(R)
      return
    for v in P[:]:
      bron_kerbosch(R + [v], [u for u in P if u in adj[v]], [u for u in X if u in adj[v]], adj, cliques)
      P.remove(v)
      X.append(v)

  def find_maximal_clique(adj):
    cliques = []
    n = len(adj)
    bron_kerbosch([], list(range(n)), [], adj, cliques)
    max_clique = max(cliques, key=len)
    return max_clique
  
  max_clique = find_maximal_clique(adj)
  max_clique = [nodes[i] for i in max_clique]
  max_clique.sort()
  print(','.join(max_clique))