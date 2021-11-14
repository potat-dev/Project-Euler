from num2words import num2words
# это конечно читерство, но мне как-то пофиг, используем силу питона

s = ""
for i in range(1000):
  s += num2words(i+1).replace(" ", "").replace("-", "")
print(len(s))