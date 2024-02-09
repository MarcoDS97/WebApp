import random

a =  set([numero for numero in range(1,100)])
print(a)

for i in range(100):
    b = a.pop()
    print(b)