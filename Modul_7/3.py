import re

a = open("Indonesia.txt", "r", encoding="latin1")
s = a.read()
a.close()
b = re.findall(r"di\s\w+", s)
print(b)
