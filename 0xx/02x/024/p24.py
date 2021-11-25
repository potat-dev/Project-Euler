from itertools import permutations
print(["".join(i) for i in permutations("0123456789")][999999])