from numpy import prod
t = ''.join([''.join(str(i)) for i in range(1, 10**6)])
print(prod([int(t[10**i-1]) for i in range(7)]))