# lyric
# https://programmers.co.kr/learn/courses/30/lessons/60060

from bisect import bisect_left, bisect_right


def solution(words, queries):
    d = {}
    f = {}
    b = {}
    answer = []
    words.sort()
    for query in queries:
        if query not in d:
            if query[0] == '?':
                res = back_query(query, words, b)
                answer.append(res)
                d[query] = res
            else:
                res = front_query(query, words, f)
                answer.append(res)
                d[query] = res
        else:
            answer.append(d[query])

    return answer


def front_query(query, words, f):
    temp = list(filter(lambda val: val != '?', query))
    str_temp = "".join(temp)
    if str_temp not in f:
        start = "".join(temp)
        temp[-1] = chr(ord(temp[-1]) + 1)
        end = "".join(temp)

        inter = words[bisect_left(words, start):bisect_left(words, end)]
        f[str_temp] = inter
        res = length(query, inter)
    else:
        res = length(query, f[str_temp])
    return len(res)


def back_query(query, words, b):
    temp = list(filter(lambda val: val != '?', query))
    if not temp:
        return len(length(query, words))
    if len(query) not in b:
        words_len = length(query, words)
        for idx, word in enumerate(words_len):
            words_len[idx] = word[::-1]
        words_len.sort()
        b[len(query)] = words_len
    else:
        words_len = b[len(query)]

    temp = temp[::-1]
    start = "".join(temp)
    temp[-1] = chr(ord(temp[-1]) + 1)
    end = "".join(temp)

    return bisect_left(words_len, end) - bisect_left(words_len, start)


def length(query, words):
    words_len = sorted(words, key=len)
    len_query = len(query)
    start = 0
    end = len(words_len)
    left = start
    right = end
    while start < end:
        mid = (start + end) // 2
        if len(words_len[mid]) < len_query:
            start = mid + 1
        else:
            end = mid

    left = start

    start = 0
    end = len(words_len)

    while start < end:
        mid = (start + end) // 2
        if len(words_len[mid]) > len_query:
            end = mid
        else:
            start = mid + 1

    right = start

    return words_len[left:right]