pan = lambda n: all([str(n).count(str(i)) == 1 for i in range(1, 10)])

def check_pan(num):
  t, n = "", 2
  while len(str(t)) < 10:
    t = ''.join([''.join(s) for s in [str(num*i) for i in range(1, n+1)]])
    if pan(t): return t
    n += 1
  return ""

max = 0
for i in range(1, 100000):
  n = check_pan(i)
  if n != "" and len(n) == 9:
    if int(n) > max: max = int(n)

print(max)