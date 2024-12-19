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
    def ways(i):
      if i >= len(design):
        return 1
      
      if i in memo:
        return memo[i]

      cnt = 0
      for pattern in patterns:
        if design[i:i+len(pattern)] == pattern:
          cnt += ways(i+len(pattern))

      memo[i] = cnt
      return cnt
    
    print(design, ways(0))
    ans += ways(0)

  print(ans)