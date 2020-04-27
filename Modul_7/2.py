import re

a = open("Indonesia.txt", "r", encoding="latin1")
s = a.read()
a.close()
b = re.findall(r"di\w+", s)
print(b)
