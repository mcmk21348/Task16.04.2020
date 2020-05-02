import random

a = []
for i in range(10):
    a.append(int(random.random() * 20) - 10)

print(a)

poloj = []
otris = []
for i in a:
    if i > 0:
        poloj.append(i)
    else:
        otris.append(i)

print(poloj)
print(otris)
