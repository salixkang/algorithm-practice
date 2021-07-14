#up down left right

n = int(input())
direction = list(map(str, input().split()))

row = 1
column = 1

for i in direction:
    if i == "U":
        if row == 1:
            continue
        else:
            row -= 1
    elif i == "D":
        if row == n:
            continue
        else:
            row += 1
    elif i == "L":
        if column == 1:
            continue
        else:
            column -= 1
    elif i == "R":
        if column == n:
            continue
        else:
            column += 1
    else:
        break

print(row, column)
