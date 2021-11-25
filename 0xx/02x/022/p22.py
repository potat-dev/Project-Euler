import requests as r
import json as j
url = "https://projecteuler.net/project/resources/p022_names.txt"
data = j.loads("[" + r.get(url).text + "]")

score = lambda w: sum(ord(c) - ord("A") + 1 for c in w)
data = sum([score(w) * (i+1) for i, w in enumerate(sorted(data))])
print(data)