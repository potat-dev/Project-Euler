# 2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.
# Какое самое маленькое число делится нацело на все числа от 1 до 20?

# как решаем:
# каждое число раскладываем на простые множители и потом
# находим максимальную степень каждого простого множителя

from math import prod

def Factor(n):
  Ans, d = [], 2
  while d * d <= n:
    if n % d == 0:
      Ans.append(d)
      n //= d
    else:
      d += 1
  if n > 1: Ans.append(n)
  return Ans

arr = {}
for k in range(1, 21):
  f = Factor(k)
  for i in list(set(f)):
    if i in arr.keys():
      if f.count(i) > arr[i]:
        arr.update({i: f.count(i)})
    else:
      arr.update({i: f.count(i)})

print(prod([x**p for x, p in zip(arr.keys(), arr.values())]))