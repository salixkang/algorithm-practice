# column and girder
# https://programmers.co.kr/learn/courses/30/lessons/60061

def solution(n, build_frame):
    answer = []

    for i in build_frame:
        x, y, stuff, opr = i[0], i[1], i[2], i[3]
        if opr == 1:
            answer.append([x, y, stuff])
            if possible(answer) == False:
                answer.remove([x, y, stuff])
        elif opr == 0:
            answer.remove([x, y, stuff])
            if possible(answer) == False:
                answer.append([x, y, stuff])

    answer = sorted(answer, key=lambda x: (x[0], x[1], x[2]))
    return answer


def possible(answer):
    for i in answer:
        x, y, stuff = i[0], i[1], i[2]
        if stuff == 0:
            if y == 0 or ([x, y, 1] in answer) or ([x - 1, y, 1] in answer) or ([x, y - 1, 0] in answer):
                continue
            else:
                return False
        elif stuff == 1:
            if ([x, y - 1, 0] in answer) or ([x + 1, y - 1, 0] in answer) or (
                    ([x - 1, y, 1] in answer) and ([x + 1, y, 1] in answer)):
                continue
            else:
                return False
        return True

print(solution(5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0,0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]))