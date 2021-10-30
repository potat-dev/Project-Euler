# Простые делители числа 13195 - это 5, 7, 13 и 29.
# Каков самый большой делитель числа 600851475143, являющийся простым числом?

def divs(n):
  arr = []
  for i in range(1, int(n**0.5+1)):
    if n % i == 0:
      arr += [i, n // i]
  return sorted(arr)

for n in divs(600851475143)[::-1]:
  if divs(n) == [1, n]:
    print(n)
    exit()