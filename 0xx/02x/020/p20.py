f = lambda n: n*f(n-1) if n > 1 else 1
print(sum([int(i) for i in str(f(100))]))