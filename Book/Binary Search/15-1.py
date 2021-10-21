# bisect

from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
lst = list(map(int, input().split()))

print(bisect_right(lst, x + 0.1) - bisect_left(lst, x - 0.1))