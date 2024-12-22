from queue import Queue

def read_input(file_path):
  with open(file_path, 'r') as file:
    return file.readlines()

def apply(x):
  x = x ^ (x << 6)
  x = x & ((1 << 24)-1)
  x = x ^ (x >> 5)
  x = x & ((1 << 24)-1)
  x = x ^ (x << 11)
  x = x & ((1 << 24)-1)
  return x

if __name__ == "__main__":
  nums = list(map(lambda x: int(x.strip()), read_input("day22/input")))

  print(nums)

  mp = {}
  for num in nums:
    ite = 2000
    price = []
    price.append(num % 10)
    for _ in range(ite):
      num = apply(num)
      price.append(num % 10)

    change = [price[i+1] - price[i] for i in range(ite)]
    vis = set()
    for x, v in zip(zip(change, change[1:], change[2:], change[3:]), price[4:]):
      if x not in vis:
        vis.add(x)
        if x not in mp:
          mp[x] = v
        else:
          mp[x] += v

  ans = 0
  for k, v in mp.items():
    ans = max(ans, v)

  print(ans)