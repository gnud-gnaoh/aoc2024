import bisect

def read_input(file_path):
  with open(file_path, 'r') as file:
    return file.readlines()

if __name__ == "__main__":
  edges = list(map(lambda x: x.strip().split('-'), read_input("day23/input")))

  print(edges)

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
  
  ans = set()
  for u in range(n):
    if nodes[u][0] == 't':
      for v in adj[u]:
        for t in adj[v]:
          for z in adj[t]:
            if z == u:
              tmp = [nodes[u], nodes[v], nodes[t]]
              tmp.sort()
              ans.add(tuple(tmp))
  
  print(len(ans))