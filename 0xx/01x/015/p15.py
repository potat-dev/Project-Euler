# t = [[1] * 20] + [[1] + [0] * 19] * 19 # при таком раскладе создаются копии массивов (указатели)

t = [[1 if x == 0 or y == 0 else 0 for x in range(21)] for y in range(21)]

for y in range(1, 21):
  for x in range(1, 21):
    t[y][x] = t[y-1][x] + t[y][x-1]

print(t[-1][-1])