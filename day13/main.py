def read_input(file_path):
  with open(file_path, 'r') as file:
    return file.readlines()

def gcd(a, b):
  if b == 0:
    return (1, 0, a)
  (x1, y1, d) = gcd(b, a % b)
  x = y1
  y = x1 - y1 * (a // b)
  return (x, y, d)

def find_sol(a, b, c):
  (x0, y0, g) = gcd(abs(a), abs(b))
  if c % g != 0:
    return (False, 0, 0, 0)
  x0 *= c // g
  y0 *= c // g
  if a < 0:
    x0 = -x0
  if b < 0:
    y0 = -y0
  return (True, x0, y0, g)

if __name__ == "__main__":
  a = list(filter(lambda x: x != "\n", read_input("day13/input")))
  n = len(a) // 3
  print(n)

  add = 10000000000000

  tot = 0
  for i in range(n):
    button_a = tuple(map(int, a[i*3].strip().split(" ")))
    button_b = tuple(map(int, a[i*3+1].strip().split(" ")))
    goal = tuple(map(int, a[i*3+2].strip().split(" ")))
    goal = (goal[0] + add, goal[1] + add)
    print(button_a, button_b, goal)

    (x1, y1) = button_a
    (x2, y2) = button_b
    (x3, y3) = goal

    # a.x1 + b.x2 = x3
    # a.y1 + b.y2 = y3
    (res, a0, b0, g) = find_sol(x1, x2, x3)
    if res == False:
      continue
    
    (ress, a1, b1, gg) = find_sol(y1, y2, y3)
    if ress == False:
      continue
    
    print(a0, b0, g)
    print(a1, b1, gg)
    assert(a0 * x1 + b0 * x2 == x3)
    assert(a1 * y1 + b1 * y2 == y3)

    # all solutions:
    # a = a0 + k * (x2 // g)
    # b = b0 - k * (x1 // g)

    # must satisfy the other equation
    if (y3 - (a0 * y1 + b0 * y2)) % (((x2 // g) * y1 - (x1 // g) * y2)) != 0:
      continue
    
    k = (y3 - (a0 * y1 + b0 * y2)) // (((x2 // g) * y1 - (x1 // g) * y2))
    print("k", k)

    aa = a0 + k * (x2 // g)
    bb = b0 - k * (x1 // g)
    ans = 3 * aa + bb
    print(aa, bb, ans)
    tot += ans

    # solution with min 3a + b
    # 3a + b = 3(a0 + k * (x2 // g)) + (b0 - k * (x1 // g))
    #         = 3a0 + 3k * (x2 // g) + b0 - k * (x1 // g)
    #         = 3a0 + b0 + k * (3 * (x2 // g) - (x1 // g))
    #         = 3a0 + b0 + k * (3 * x2 - x1) // g

    # kmin = ceil(-a0 / (x2 // g))
    # kmax = floor(b0 / (x1 // g))
    # if 3 * x2 < x1:
    #   # 3 * x2 - x1 < 0 => find max k
    #   a = a0 + kmax * (x2 // g)
    #   b = b0 - kmax * (x1 // g)
    #   ans = min(ans, 3 * a + b)
    # elif 3 * x2 > x1:
    #   # 3 * x2 - x1 > 0 => find min k
    #   a = a0 + kmin * (x2 // g)
    #   b = b0 - kmin * (x1 // g)
    #   ans = min(ans, 3 * a + b)
    # else:
    #   # 3 * x2 - x1 == 0 => all solutions have same sum
    #   a = a0 + kmin * (x2 // g)
    #   b = b0 - kmin * (x1 // g)
    #   ans = min(ans, 3 * a + b)

    # print(i, ans)
    # tot += ans

  print(tot)