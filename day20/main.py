from queue import Queue

def read_input(file_path):
  with open(file_path, 'r') as file:
    return file.readlines()

if __name__ == "__main__":
  a = list(map(lambda x: list(x.strip()), filter(lambda x: x != "\n", read_input("day20/input"))))
  print(a)

  n = len(a)
  start = None
  end = None
  for i in range(n):
    for j in range(n):
      if a[i][j] == 'S':
        start = (i, j)
      elif a[i][j] == 'E':
        end = (i, j) 

  def bfs():
    dist = [[-1 for _ in range(n)] for _ in range(n)]
    q = Queue(maxsize=n*n)
    q.put(start)
    dist[start[0]][start[1]] = 0
    
    while not q.empty():
      i, j = q.get()
      for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
        if 0 <= ni < n and 0 <= nj < n and a[ni][nj] != '#' and dist[ni][nj] == -1:
          dist[ni][nj] = dist[i][j] + 1
          q.put((ni, nj))
    return dist[end[0]][end[1]]

  init = bfs()
  print("init", init)

  cnt = 0
  for i in range(n - 1):
    for j in range(n - 1):
      print(i, j)
      # i+1
      if a[i][j] == '#' and a[i+1][j] != '#':
        ocur = a[i][j]
        onxt = a[i+1][j]
        a[i][j] = '.';
        a[i+1][j] = '.';
        cur = bfs()
        # print(i, j, i+1, j, cur)
        if init - cur >= 100:
          cnt += 1
        a[i][j] = ocur
        a[i+1][j] = onxt

      if a[i][j] == '#' and a[i][j+1] != '#':
        # j+1
        ocur = a[i][j]
        onxt = a[i][j+1]
        a[i][j] = '.';
        a[i][j+1] = '.';
        cur = bfs()
        # print(i, j, i, j+1, cur)
        if init - cur >= 100:
          cnt += 1
        a[i][j] = ocur
        a[i][j+1] = onxt      

  print(cnt)