import math
a = int(input("сторона a: "))
b = int(input("сторона b: "))
c = int(input("сторона c: "))
p = (a+b+c) / 2
s = math.sqrt(p*(p-a)*(p-b)*(p-c))
print(s)