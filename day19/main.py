def read_input(file_path):
  with open(file_path, 'r') as file:
    return file.readlines()

if __name__ == "__main__":
  a = list(filter(lambda x: x != "\n", read_input("day19/input")))
  print(a)

  patterns = a[0].strip().split(", ")
  print(patterns)

  designs = a[1:]
  print(designs)

  ans = 0
  for design in designs:
    design = design.strip()
    print(design)

    memo = {}
    def check(i):
      if i >= len(design):
        return True
      
      if i in memo:
        return memo[i]

      good = False
      for pattern in patterns:
        if design[i:i+len(pattern)] == pattern:
          good |= check(i+len(pattern))

      memo[i] = good
      return good
    
    if check(0):
      print("OK ", design)
      ans += 1

  print(ans)