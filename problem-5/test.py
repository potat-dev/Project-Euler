# тестовое решение [не работает]

def divs(n):
  arr = set()
  for i in range(1, int(n**0.5+1)):
    if n % i == 0:
      arr.add((i, n // i))
  return arr

is_prime = lambda n: divs(n) == [1, n]

def fact(n):
  arr, temp = divs(n), set()
  while not all([is_prime(i) for i in arr]):
    for i in arr:
      if is_prime(i):
        temp.add(i)
      else:
        temp.add(fact(i))
    arr = temp
  return arr


arr = set()
for i in range(20):
  arr.add(fact(i + 1))

print(arr)