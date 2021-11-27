f1, f2, n = 1, 1, 2
while len(str(f2)) < 1000:
  f1, f2, n = f2, f1+f2, n+1
print(n)