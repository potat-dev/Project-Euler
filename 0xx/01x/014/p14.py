def seq(n):
  c, k = 1, n
  while k > 0 and k != 1:
    if k % 2 == 0:
      k, c = k // 2, c+1
    else:
      k, c = 3*k+1, c+1
  return c+1

print(sorted([(seq(i), i) for i in range(10**6)], key=lambda x: x[0])[-1][1])