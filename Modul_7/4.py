import re

a = open("KEI.html", "r", encoding="latin1")
s = a.read()
a.close()

pola =  r'(\w+)</a></td>\
<td>\d\.\d\d</td>\
<td>\d\.\d\d</td>\
<td>\d\.\d\d</td>\
<td>(\d.\d\d)'

b = re.findall(pola, s)
c = []
for i in b:
    c.append((i[0], float(i[1])))
print(c)
