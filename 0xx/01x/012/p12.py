from itertools import chain

triangle = lambda n: sum([i for i in range(1, n + 1)])
dels = lambda n: [i for i in range(1, n + 1) if n % i == 0]
divs = lambda n: chain(*((d, n // d) for d in range(1, int(n ** 0.5) + 1) if n % d == 0))

i = 1
while len(list(divs(triangle(i)))) <= 500:
  i += 1

print(triangle(i))