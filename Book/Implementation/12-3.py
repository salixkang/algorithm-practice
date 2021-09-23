# string zip
# https://programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    min_result = len(s)
    for x in range(1, len(s)):
        array = []
        for i in range(0, len(s), x):
            if i + x > len(s):
                array.append(s[i:len(s)])
            else:
                array.append(s[i:i + x])
        result = [[array[0], 1]]

        n = 0

        for i in array[1:len(array)]:
            if i == result[n][0]:
                result[n][1] += 1
            else:
                n += 1
                result.append([i, 1])
        temp = 0
        for i in result:
            if i[1] == 1:
                temp += len(i[0])
            else:
                temp += len(i[0]) + len(str(i[1]))
        min_result = min(min_result, temp)

    answer = min_result
    return answer

print(solution("ababcdcdababcdcd"))