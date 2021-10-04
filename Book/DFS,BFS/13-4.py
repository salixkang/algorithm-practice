# bracket
# https://programmers.co.kr/learn/courses/30/lessons/60058

def solution(p):
    answer = ''
    if not p:
        return answer

    u = []
    v = []

    check = [0] * 3
    for idx, var in enumerate(p):
        if var == '(':
            check[0] += 1
        elif var == ')':
            check[1] += 1
            if check[1] > check[0]:
                check[2] = 1
        u.append(var)
        if check[0] == check[1]:
            if idx + 1 < len(p):
                v = p[idx + 1:]
                break
            else:
                v = []
                break

    result = []
    print(u)

    if check[2] != 1:
        result = u + [solution(v)]
    else:
        result = ['('] + [solution(v)] + [')']
        for i in u[1:-1]:
            if i == '(':
                result.append(')')
            elif i == ')':
                result.append('(')

    answer = "".join(result)

    return answer



