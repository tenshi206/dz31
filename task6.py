n=[1, 3, 4, 5]
m=[4, 5, 6, 7]
x = []
for i in m:
    if i not in n:
        x.append(i)
print(x)
