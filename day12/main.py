def read_input(file_path):
  with open(file_path, 'r') as file:
    return file.readlines()

if __name__ == "__main__":
  a = read_input("day12/input")
  a = [list(line.strip()) for line in a]

  n = len(a)
  m = len(a[0])
  vis = [[False for _ in range(m)] for _ in range(n)]
  ans = 0
  for i in range(n):
    for j in range(m):
      if not vis[i][j]:
        print("pos", i, j)
        vis[i][j] = True
        lst = []
        
        # bfs from (i, j)
        q = [(i, j)]
        while q:
          x, y = q.pop(0)
          lst.append((x, y))
          for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if nx >= 0 and nx < n and ny >= 0 and ny < m and a[nx][ny] == a[x][y] and not vis[nx][ny]:
              vis[nx][ny] = True
              q.append((nx, ny))
        
        area = len(lst)

        # idea: count the number of corners instead of sides
        zero = 0
        one = 0
        two = 0
        for x, y in lst:
          cur = 0
          for dx, dy in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
            nx, ny = x + dx, y + dy
            nnx, nny = x + dx, y
            nnnx, nnny = x, y + dy
            cnt = 0
            if (nx, ny) in lst:
              cnt += 1
            if (nnx, nny) in lst:
              cnt += 1
            if (nnnx, nnny) in lst:
              cnt += 1

            # AX
            # XX
            if cnt == 0:
              zero += 1
            # AA
            # AX
            elif cnt == 2:
              two += 1
            # AX
            # XA
            elif cnt == 1 and (nx, ny) in lst: # opposite of each other
              one += 1

        # case 2 will be repeated 3 times
        corner = zero + two // 3 + one
        print(area, corner)
        ans += area * corner
  
  print(ans)