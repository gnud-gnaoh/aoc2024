from queue import Queue

def read_input(file_path):
  with open(file_path, 'r') as file:
    return file.readlines()

pos_numpad = {
  '7': (0, 0), '8': (0, 1), '9': (0, 2),
  '4': (1, 0), '5': (1, 1), '6': (1, 2),
  '1': (2, 0), '2': (2, 1), '3': (2, 2),
  '0': (3, 1), 'A': (3, 2)
}

numpad = [
  ['7', '8', '9'],
  ['4', '5', '6'],
  ['1', '2', '3'],
  ['.', '0', 'A']
]

pos_keypad = {
  '^': (0, 1), 'A': (0, 2),
  '<': (1, 0), 'v': (1, 1), '>': (1, 2)
}

action_keypad = {
  '^': (-1, 0), 'v': (+1, 0),
  '<': (0, -1), '>': (0, +1),
  'A': (0, 0)
}

keypad = [
  ['.', '^', 'A'],
  ['<', 'v', '>']
]

def in_numpad(i, j):
  return i >= 0 and i < 4 and j >= 0 and j < 3 and (i, j) != (3, 0)

def in_keypad(i, j):
  return i >= 0 and i < 2 and j >= 0 and j < 3 and (i, j) != (0, 0)

def dist(a, b):
  return abs(a[0] - b[0]) + abs(a[1] - b[1])

def move(u, dx, dy, l):
  # print(u, dx, dy, l)
  if l == 0:
    i, j = pos_numpad[u[l]]
    if dx == 0 and dy == 0:
      return u
    else:
      i += dx
      j += dy
      if not in_numpad(i, j):
        return None
      return (numpad[i][j], u[1], u[2])

  assert(l != 0)
  i, j = pos_keypad[u[l]] 
  # press
  if dx == 0 and dy == 0:
    ndx, ndy = action_keypad[u[l]]
    return move(u, ndx, ndy, l-1)
  else:
    # move
    i += dx
    j += dy
    if not in_keypad(i, j):
      return None
    else:
      return u[:l] + (keypad[i][j],) + u[l + 1:]

d = {}
def bfs(st):
  dd = {st: 0}
  q = Queue()
  q.put(st)
  while not q.empty():
    u = q.get()

    def dak(dx, dy):
      v = move(u, dx, dy, 2)
      if v != None and v not in dd:
        dd[v] = dd[u] + 1
        q.put(v)
        # print(f"{u} -> {v} | {dd[v]}")
        
    # ^
    dak(-1, 0)
    # v
    dak(+1, 0)
    # <
    dak(0, -1)
    # >
    dak(0, +1)
    # A  
    dak(0, 0)

  return dd

def solve(code):
  lst = ('A', 'A', 'A')
  ans = 0
  for c in code:
    ans += d[lst][(c, 'A', 'A')]
    ans += 1 # press 
    lst = (c, 'A', 'A')
  return ans

if __name__ == "__main__":
  codes = list(map(lambda x: x.strip(), read_input("day21/input")))
  
  # print(move(('A', 'A', 'A'), 0, 0, 2))
  assert(move(('A', 'A', 'A'), 0, 0, 2) == ('A', 'A', 'A'))
  
  # bfs from all states
  for x in ['7', '8', '9', '4', '5', '6', '1', '2', '3', '0', 'A']:
    for y in ['^', '<', '>', 'v', 'A']:
      for z in ['^', '<', '>', 'v', 'A']:
        d[(x, y, z)] = bfs((x, y, z))
        print(x, y, z, '|', len(d[(x, y, z)]))

  ans = 0
  for code in codes:
    numeric = int(code[:-1])
    val = numeric * solve(code)
    print(f"{code} -> {val}")
    ans += val

  print(ans)
