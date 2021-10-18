# score

n = int(input())
array = []
for _ in range(n):
    lst = list(input().split())
    for i in range(3):
        lst[i + 1] = int(lst[i + 1])
    array.append(lst)

array.sort(key = lambda score: (-score[1], score[2], -score[3], score[0]))

for student in array:
    print(student[0])