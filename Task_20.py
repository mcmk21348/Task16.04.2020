import random

a = []
for i in range(10):
    a.append(int(random.random() * 100))

print(a)

b = 0
c = 0 
for i in a:
    if i%2 == 0:
        b +=1
    else:
        c +=1
print('Четные ', b)
print('Не четные ', c)