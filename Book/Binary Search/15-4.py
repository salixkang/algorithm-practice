# lyric
# https://programmers.co.kr/learn/courses/30/lessons/60060

from bisect import bisect_left, bisect_right


def solution(words, queries):
    d = []
    answer = []
    words.sort()
    for query in queries:
        if query[0] == '?':
            res = back_query(query, words)
        else:
            res = front_query(query, words)
            print(res)

    return answer


def front_query(query, words):
    temp = []
    for i in query:
        if i != '?':
            temp.append(i)
        else:
            break

    start = "".join(temp)
    temp[-1] = chr(ord(temp[-1]) + 1)
    end = "".join(temp)

    inter = words[bisect_left(words, start):bisect_left(words, end)]
    inter.sort(key=len)
    res = 0
    for i in inter:
        if len(i) == len(query):
            res += 1
        elif len(i) >= len(query):
            break

    return res


def back_query(query, words):
    return 0