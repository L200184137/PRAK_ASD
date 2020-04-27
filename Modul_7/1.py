import re

a = open("Indonesia.txt", "r", encoding="latin1")
s = a.read()
a.close()
b = re.findall(r"\w*me\w*", s)
print(b)
