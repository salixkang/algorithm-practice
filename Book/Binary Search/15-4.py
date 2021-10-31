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
            answer.append(res)
        else:
            res = front_query(query, words)
            answer.append(res)

    return answer


def front_query(query, words):
    temp = list(filter(lambda val: val != '?', query))
    print(temp)
    # for i in query:
    #     if i != '?':
    #         temp.append(i)
    #     else:
    #         break

    start = "".join(temp)
    temp[-1] = chr(ord(temp[-1]) + 1)
    end = "".join(temp)

    inter = words[bisect_left(words, start):bisect_left(words, end)]
    res = length(query, inter)

    return res


def back_query(query, words):
    temp = list(filter(lambda val: val != '?', query))
    if not temp:
        return length(query, words)
    len_q = len(words) - len(temp)

    return 0


def length(query, words):
    words.sort(key=len)
    len_query = len(query)
    start = 0
    end = len(words)
    left = start
    right = end
    while start < end:
        mid = (start + end) // 2
        if len(words[mid]) < len_query:
            start = mid + 1
        else:
            end = mid

    left = start

    start = 0
    end = len(words)

    while start < end:
        mid = (start + end) // 2
        if len(words[mid]) > len_query:
            end = mid
        else:
            start = mid + 1

    right = start

    return len(words[left:right])
