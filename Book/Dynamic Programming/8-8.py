# monetary composition

n, m = map(int, input().split())

d = [10001] * (10001) # 1부터 m 까지의 저장 공간. 10001은 존재할 수 없는 결과값 (m의 최대값 / n의 최소값 < 10001)
d[0] = 0
q = [0] * n
money = []
for _ in range(n):
    money.append(int(input()))

money.sort(reverse=True)

for i in range(n):
    d[money[i]] = 1

for i in range(1, m+1):
    result = 10001 # d[i] 의 불가능한 값. 이 경우 -1 을 출력한다.
    for j in range(n):
        q[j] = i//money[j] # i 를 각 화폐 단위로 나누었을 때 몫을 저장

    for k in range(n): # n 개의 화폐 단위 순회
        a = q[k]
        while a != 0 :
            x = i - money[k] * a # x는 i 에서 k 번째 화폐단위를 l 값을 곱한 값을 뺀 값
            if d[x] != 10001 : # d[x] 가 존재할 때
                result = min(result, a + d[x])
                d[i] = result # d[i] 값은 지금까지의 result 와 l + d[x] 중 minimum 값
            a -= 1

# for i in range(n):
#     for j in range(money[i], m+1):
#         if d[j-money[i]] != 10001:
#             d[j] = min(d[j], d[j-money[i]] + 1)

if d[m] == 10001:
    print('-1')
else :
    print(d[m])

