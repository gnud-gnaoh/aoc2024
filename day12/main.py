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
        print(i, j)
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
        
        # print(lst)
        area = len(lst)
        peri = area * 4
        for x, y in lst:
          for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            # if can find (nx, ny) in lst, subtract that side
            if (nx, ny) in lst:
              peri -= 1
        
        ans += area * peri
  
  print(ans)