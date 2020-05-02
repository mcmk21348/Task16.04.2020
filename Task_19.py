a = (input())
b = a.replace(' ', '')
print(b)
c = b.lower()
if c[::1] == c[::-1]:
    print(True)
else:
    print(False)