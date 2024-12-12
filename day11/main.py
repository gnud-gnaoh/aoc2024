import os

def read_input(file_path):
  with open(file_path, 'r') as file:
    return file.readlines()

mp = {}
def calc(x, steps):
  if steps == 0:
    return 1

  if mp.get((x, steps)):
    return mp[(x, steps)]
  
  ans = 0
  if x == 0:
    ans = calc(1, steps - 1)
  elif len(str(x)) % 2 == 0:
    tmp = str(x)
    ans = calc(int(tmp[:len(tmp)//2]), steps - 1) + calc(int(tmp[len(tmp)//2:]), steps - 1)
  else:
    ans = calc(x * 2024, steps - 1)

  mp[(x, steps)] = ans
  return ans

if __name__ == "__main__":
  a = [int(x) for x in read_input("day11/input")[0].split(' ')]

  ite = 75
  ans = 0
  for x in a:
    ans += calc(x, ite)
  
  print(ans)
  