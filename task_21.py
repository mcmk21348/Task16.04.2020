a =input('Введите строку: ')
b = a.split()
print(b)
count=0
for i in b:
    if len(i)>count:
        count=len(i)
        word=i    
print('Самая длинная слово: ',word)
