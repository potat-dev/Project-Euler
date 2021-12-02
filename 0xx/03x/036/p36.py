from tqdm import trange

summ = 0
is_palind = lambda n: str(n) == str(n)[::-1] and bin(n)[2:] == bin(n)[2:][::-1]
for i in trange(1, 10**6):
  if is_palind(i):
    summ += i

print(summ)