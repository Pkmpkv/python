import random as R

li = []
for _ in range(10):
    li.append(R.randint(1,100))

print(li)
li.sort(reverse=True)
print(li)