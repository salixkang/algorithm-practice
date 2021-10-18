# single input
# n = int(input())

#
# multi-variable input
# n, m = map(int, input().split())
#

#
# graph input
# graph = [list(map(int, input())) for _ in range(n)]
# or
# for i in range(n):
#     graph[i] = list(map(int, input().split()))
#

#
# array input
# array = []
# for i in range(n):
#     array.append(int(input()))
#

#
# tuple input
# array = []
# for i in range(n):
#     input_data = input().split()
#     array.append((input_data[0], int(input_data[1])))
#

#
# array input
# arrayA = list(map(int, input().split()))
#

#
# set input
# set = set(map(int, input().split()))
#

#
# list input(with string, integer)
# lst = list(input().split())
#

#
# quick input
# import sys
# input_data = sys.stdin.readline().rstrip()
# print(input_data)
#

#
# sort library
# array = sorted(array)
# array = sorted(array, reverse = True)
# array.sort()
# array.sort(reverse = True)
#

#
# tuple sort
# array = sorted(array, key=lambda student:student[1])
#

#
# Binary Search by recursive function
# def binary_search(array, target, start, end):
#     if start>end:
#         return None
#     mid = (start + end) // 2
#     if array[mid] == target:
#         return mid
#     elif array[mid] > target:
#         return binary_search(array, target, start, mid-1)
#     else:
#         return binary_search(Array, target, mid+1, end)
#

#
# binary search by loop
# def binary_search(array, target, start, end):
#     while start <= end:
#         mid = (start + end) // 2
#         if array[mid] == target:
#             return mid
#         elif array [mid] > target:
#             end = mid - 1
#         else:
#             start = mid + 1
#     return None
#

#
# if statement
# if x = 0 :
# elif x = 1:
# else :
#

#
# dictionary
# data = dict()
# data['사과'] = 'Apple'
# data['바나나'] = 'Banana'
# data['코코넛'] = 'Coconut'
#

#
# copy list
# list1 = list2.copy()
#

#
# delete element
# array.remove(a)'
#

#
# for variable by list slicing
# for x in data[1: -1]:
#     indegree[i] += 1
#     graph[x].append(i)
#

#
# list slicing
# a[start:end:step]
#

#
# list sorting
# from operator import itemgetter, attrgetter
# answer = sorted(answer, key = itemgetter(0, 1, 2))
#

#
# abs
# abs(-99) = 99
#

#
# deque
# from collections import deque
# lst = deque()
#

#
# heapq
# import heapq
# heap = []
# heapq.heappush(heap, 1)
#

#
# itertools
# import itertools
# for i in list(itertools.permutations(array, 3)):
#