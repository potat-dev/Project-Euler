from itertools import chain
divs = lambda n: sorted(chain(*(set([d, n // d]) for d in range(1, int(n**0.5) + 1) if n % d == 0)))
abundant = [i for i in range(1, 28123) if sum(divs(i)[:-1]) > i]
summs = set([a+b for a in abundant for b in abundant])

s = 0
for i in range(28123):
  s += i if not i in summs else 0
print(s) # 7 seconds