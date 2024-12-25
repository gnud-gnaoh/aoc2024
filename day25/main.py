def read_input(file_path):
  with open(file_path, 'r') as file:
    return file.readlines()
  
def fit(key, lock):
  cnt = [0] * 5
  for col in range(5):
    for row in range(7):
      if key[row][col] == '#':
        cnt[col] += 1
      if lock[row][col] == '#':
        cnt[col] += 1
  
  return max(cnt) <= 7
  
if __name__ == "__main__":
  inp = list(map(str.strip, read_input("day25/input")))
  print(inp)

  locks = []
  keys = []
  for i in range(0, 4000, 8):
    cur = inp[i:i+7]
    if cur[0] == "#####":
      locks.append(cur)
    else:
      keys.append(cur)

  ans = 0
  for lock in locks:
    for key in keys:
      if fit(key, lock):
        ans += 1
  
  print(ans)