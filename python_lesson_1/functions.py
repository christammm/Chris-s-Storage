import random


__author__ = 'Jabari'


def f(x):
    return 2 * x + 1


for x in range(int(input("f(x) for range...? "))):
    print(f(x))

print("")


rand_num = random.randrange(0, 10)

while rand_num != 5:
    print(rand_num)
    rand_num = random.randrange(0, 10)

