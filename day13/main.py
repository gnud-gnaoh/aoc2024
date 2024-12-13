def read_input(file_path):
  with open(file_path, 'r') as file:
    return file.readlines()

if __name__ == "__main__":
  a = list(filter(lambda x: x != "\n", read_input("day13/input")))
  
  n = len(a) // 3
  print(n)

  res = 0
  for i in range(n):
    button_a = tuple(map(int, a[i*3].strip().split(" ")))
    button_b = tuple(map(int, a[i*3+1].strip().split(" ")))
    goal = tuple(map(int, a[i*3+2].strip().split(" ")))
    print(button_a, button_b, goal)

    max_press = 101
    ans = 1e9
    for press_a in range(max_press):
      cur = (goal[0] - button_a[0] * press_a, goal[1] - button_a[1] * press_a)
      if cur[0] % button_b[0] == 0 and cur[1] % button_b[1] == 0 and cur[0] // button_b[0] == cur[1] // button_b[1]:
        press_b = cur[0] // button_b[0]
        ans = min(ans, press_a * 3 + press_b)

    if ans != 1e9:
      res += ans

  print(res)