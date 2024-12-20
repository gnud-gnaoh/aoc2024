from queue import Queue

def read_input(file_path):
  with open(file_path, 'r') as file:
    return file.readlines()

if __name__ == "__main__":
  a = list(map(lambda x: list(x.strip()), filter(lambda x: x != "\n", read_input("day20/input"))))
  # print(a)

  n = len(a)
  start = None
  end = None
  for i in range(n):
    for j in range(n):
      if a[i][j] == 'S':
        start = (i, j)
      elif a[i][j] == 'E':
        end = (i, j) 

  def bfs(s):
    dist = [[-1 for _ in range(n)] for _ in range(n)]
    q = Queue(maxsize=n*n)
    q.put(s)
    dist[s[0]][s[1]] = 0
    
    while not q.empty():
      i, j = q.get()
      for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
        if 0 <= ni < n and 0 <= nj < n and a[ni][nj] != '#' and dist[ni][nj] == -1:
          dist[ni][nj] = dist[i][j] + 1
          q.put((ni, nj))
          
    return dist

  distS = bfs(start)
  distE = bfs(end)

  init = distS[end[0]][end[1]]
  print("init", init)

  cnt = 0
  for i in range(n):
    for j in range(n):
      if a[i][j] == '#' or distS[i][j] == -1:
        continue
      
      print(i, j)
      
      for ii in range(n):
        for jj in range(n):
          if a[ii][jj] == '#' or distE[ii][jj] == -1:
            continue

          # print(i, j, ii, jj)

          d = abs(i - ii) + abs(j - jj)
          if d > 20:
            continue
          
          cur = distS[i][j] + d + distE[ii][jj]

          # print(i, j, ii, jj, cur)
          if init - cur >= 100:
            cnt += 1

  print(cnt)