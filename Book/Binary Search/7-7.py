# by set()

n = int(input())

goods = set(map(int, input().split()))

m = int(input())

find = list(map(int, input().split()))

for i in find:
    if i in goods:
        print('yes', end = ' ')
    else :
        print('no', end = ' ')

