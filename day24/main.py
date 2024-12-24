from random import randint

def read_input(file_path):
  with open(file_path, 'r') as file:
    return file.readlines()

gates = {}

def calc(x, y):
  mp = {}
  for i in range(45):
    mp['x' + str(i).zfill(2)] = (x >> i) & 1
    mp['y' + str(i).zfill(2)] = (y >> i) & 1
  z = x + y

  while True:
    changed = False
    for output in gates:
      if output not in mp:
        first, op, second = gates[output]
        if first in mp and second in mp:
          changed = True
          if op == "AND":
            mp[output] = mp[first] & mp[second]
          if op == "OR":
            mp[output] = mp[first] | mp[second]
          if op == "XOR":
            mp[output] = mp[first] ^ mp[second]
          
          if output[0] == 'z' and mp[output] != (z >> int(output[1:]) & 1):
            return False

    if not changed:
      break
  
  for i in range(46):
    name = 'z' + str(i).zfill(2)
    if name not in mp:
      return False

  return True
  
if __name__ == "__main__":
  inp = read_input("day24/input")
  split = inp.index("\n")
  vals = list(map(str.strip, inp[:split]))
  for gate in inp[split+1:]:
    operation, output = gate.strip().split(" -> ")
    gates[output] = operation.split(" ")
    
  print(vals, gates)
  
  def check(b):
    for _ in range(100):
      # generate random number with b bits
      randx = randint(0,pow(2,b)-1)
      randy = randint(0,pow(2,b)-1)
      if not calc(randx, randy):
        return False
    return True
  
  swaps = []
  n = len(gates)
  for b in range(1, 46):
    if len(swaps) == 8:
      break

    print("checking ", b)
    if not check(b):
      found = False
      for g1 in gates.keys():
        if found:
          break

        for g2 in gates.keys():
          if g2 <= g1:
            continue
    
          temp = gates[g1]
          gates[g1] = gates[g2]
          gates[g2] = temp

          if check(b+1):
            print('swapping',g1,g2)
            swaps.append(g1)
            swaps.append(g2)
            found = True
            break
              
          temp = gates[g1]
          gates[g1] = gates[g2]
          gates[g2] = temp
      assert(found)
  swaps.sort()
  print(','.join(swaps))
  assert(check(45))