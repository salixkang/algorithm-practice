# column and girder
# https://programmers.co.kr/learn/courses/30/lessons/60061

def solution(n, build_frame):
    from operator import itemgetter, attrgetter

    answer = []

    column = []
    girder = []
    girder_end = []
    column_end = []

    for i in build_frame:
        if i[2] == 0:
            if i[3] == 1:
                if i[1] == 0 or (i[0], i[1]) in column_end or (i[0], i[1]) in girder or (i[0], i[1]) in girder_end:
                    column.append((i[0], i[1]))
                    column_end.append((i[0], i[1] + 1))
            elif i[3] == 0:
                if ((i[0], i[1] + 1) in column and (i[0], i[1] + 1) not in girder and (
                i[0], i[1] + 1) not in girder_end) or ((i[0], i[1] + 1) in girder and (
                        ((i[0], i[1] + 1) not in girder_end or (i[0] + 1, i[1] + 1) not in girder) or (
                i[0] + 1, i[1] + 1) not in column_end)) or ((i[0], i[1] + 1) in girder_end and (
                        ((i[0] - 1, i[1] + 1) not in girder_end or (i[0], i[1] + 1) not in girder) or (
                i[0] - 1, i[1] + 1) not in column_end)):
                    continue
                else:
                    column.remove((i[0], i[1]))
                    column_end.remove((i[0], i[1] + 1))

        elif i[2] == 1:
            if i[3] == 1:
                if (i[0], i[1]) in column_end or (i[0] + 1, i[1]) in column_end or (
                        (i[0], i[1]) in girder_end and (i[0] + 1, i[1]) in girder):
                    girder.append((i[0], i[1]))
                    girder_end.append((i[0] + 1, i[1]))

            elif i[3] == 0:
                if (i[0], i[1]) in column and ((i[0], i[1]) not in column_end and (i[0], i[1]) not in girder_end) or (
                        (i[0], i[1]) in girder_end and (i[0], i[1]) not in column_end and (
                i[0] - 1, i[1]) not in column_end) or (
                        (i[0] + 1, i[1]) in girder and (i[0] + 1, i[1]) not in column_end and (
                i[0] + 2, i[1]) not in column_end):
                    continue
                girder.remove((i[0], i[1]))
                girder_end.remove((i[0] + 1, i[1]))

    for i in column:
        answer.append([i[0], i[1], 0])

    for i in girder:
        answer.append([i[0], i[1], 1])

    answer = sorted(answer, key=itemgetter(0, 1, 2))
    return answer