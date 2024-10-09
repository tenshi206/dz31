from random import randint
n = []
for i in range(10):
    n.append(randint(1,100))
print(n)
print(sum(n)/len(n))
