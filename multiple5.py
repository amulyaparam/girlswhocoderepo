import random

list = []
calc = 0

while int(calc) < 100:
    list.append(random.randint(10,99))
    calc = int(calc) + 1

for i in range(10,99,5):
    print(list[i])
