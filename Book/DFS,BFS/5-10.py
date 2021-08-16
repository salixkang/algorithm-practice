# Ice maker

N, M = map(int, input().split())
# state N x M list
mycraft = [list(map(int, input())) for _ in range(N)]

# for i in range(N):
#     mycraft[i] = list(map(int, input().split()))

ice_num = 0

def make(list, i, j) :
    if list[i][j] == 0:
        list[i][j] = 1
        if i != 0 :
            make(list, i-1, j)
        if i != N-1 :
            make(list, i+1, j)
        if j != 0 :
            make(list, i, j-1)
        if j != M-1 :
            make(list, i, j+1)
        return True
    return False

for i in range(N):
    for j in range(M):
        if make(mycraft, i, j) :
            ice_num += 1

print(ice_num)
