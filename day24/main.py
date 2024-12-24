def read_input(file_path):
  with open(file_path, 'r') as file:
    return file.readlines()

if __name__ == "__main__":
  inp = read_input("day24/input")
  split = inp.index("\n")
  vals = list(map(str.strip, inp[:split]))
  gates = list(map(str.strip, inp[split+1:]))

  print(vals, gates)

  mp = {}
  for val in vals:
    name, value = val.split(": ")
    mp[name] = int(value)
  
  print(mp)

  while True:
    changed = False
    for gate in gates:
      operation, output = gate.split(" -> ")
      first, op, second = operation.split(" ")

      # will do topo sort later
      if first in mp and second in mp and output not in mp:
        changed = True
        print(first, second)
        if op == "AND":
          mp[output] = mp[first] & mp[second]
        elif op == "OR":
          mp[output] = mp[first] | mp[second]
        elif op == "XOR":
          mp[output] = mp[first] ^ mp[second]
        else:
          assert(false)

    if not changed:
      break
  
  a = []
  for k, v in mp.items():
    if k[0] == 'z':
      a.append((k[1:], v))

  a.sort(key=lambda x: x[0])
  a.reverse()
  
  ans = 0
  for i in range(len(a)):
    ans = ans * 2 + a[i][1]
  
  print(ans)