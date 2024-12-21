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

memo_digit = {}
# min cost to move from (i, j) to (ii, jj) and activate, given last char of the next pad ('A' to press)
def digit_solve(i, j, ii, jj, lst='A'):
  if (i, j) == (ii, jj):
    return key_solve(*pos_keypad[lst], *pos_keypad['A']) # move from lst to 'A' to press

  if (i, j, ii, jj, lst) in memo_digit:
    return memo_digit[(i, j, ii, jj, lst)]

  ans = 1e18

  # move up or down
  if i != ii:
    if i < ii:
      if not (i+1 == 3 and j == 0):
        ans = min(ans, digit_solve(i+1, j, ii, jj, 'v') + key_solve(*pos_keypad[lst], *pos_keypad['v']))
    else:
      ans = min(ans, digit_solve(i-1, j, ii, jj, '^') + key_solve(*pos_keypad[lst], *pos_keypad['^']))

  # move left or right
  if j != jj:
    if j < jj:
      ans = min(ans, digit_solve(i, j+1, ii, jj, '>') + key_solve(*pos_keypad[lst], *pos_keypad['>']))
    else:
      if not (j-1 == 0 and i == 3):
        ans = min(ans, digit_solve(i, j-1, ii, jj, '<') + key_solve(*pos_keypad[lst], *pos_keypad['<']))

  memo_digit[(i, j, ii, jj, lst)] = ans
  return ans

memo_key = {}
# min cost to move from (i, j) to (ii, jj) and activate, n for position, given last char of the next pad ('A' to press)
def key_solve(i, j, ii, jj, n=25, lst='A'):
  if n == 0:
    return 1 # human press
  
  if (i, j, ii, jj, n, lst) in memo_key:
    return memo_key[(i, j, ii, jj, n, lst)]

  if (i, j) == (ii, jj):
    return key_solve(*pos_keypad[lst], *pos_keypad['A'], n-1) # move from lst to 'A' to press

  ans = 1e18

  # move up or down
  if i != ii:
    if i < ii:
      ans = min(ans, key_solve(i+1, j, ii, jj, n, 'v') + key_solve(*pos_keypad[lst], *pos_keypad['v'], n-1))
    else:
      if not (i-1 == 0 and j == 0):
        ans = min(ans, key_solve(i-1, j, ii, jj, n, '^') + key_solve(*pos_keypad[lst], *pos_keypad['^'], n-1))

  # move left or right
  if j != jj:
    if j < jj:
      ans = min(ans, key_solve(i, j+1, ii, jj, n, '>') + key_solve(*pos_keypad[lst], *pos_keypad['>'], n-1))
    else:
      if not (j-1 == 0 and i == 0):
        ans = min(ans, key_solve(i, j-1, ii, jj, n, '<') + key_solve(*pos_keypad[lst], *pos_keypad['<'], n-1))

  memo_key[(i, j, ii, jj, n, lst)] = ans
  return ans

def solve(code):
  lst = 'A'
  ans = 0
  for c in code:
    ans += digit_solve(*pos_numpad[lst], *pos_numpad[c]) 
    lst = c
  return ans

if __name__ == "__main__":
  codes = list(map(lambda x: x.strip(), read_input("day21/input")))

  ans = 0
  for code in codes:
    numeric = int(code[:-1])
    val = numeric * solve(code)
    print(f"{code} -> {val}")
    ans += val

  print(ans)
