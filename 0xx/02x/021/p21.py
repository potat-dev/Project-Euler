from itertools import chain
divs = lambda n: [1] + list(set(chain(*((d, n // d) for d in range(2, int(n ** 0.5) + 1) if n % d == 0))))

d = []
for i in range(10000):
  d.append(sum(divs(i)))

m = []
for i in range(10000):
  if d[i] < 10000:
    if d[d[i]] == i and d[i] != i:
      m += [i, d[i]]

print(sum(list(set(m))))