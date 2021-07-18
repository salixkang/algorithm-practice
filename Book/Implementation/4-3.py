# knight of the kingdom

input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

moves = [(2, 1), (2, -1), (1, 2), (1, -2), (-2, 1), (-2, -1), (-1, 2), (-1, -2)]
count = 0

for move in moves:
    if column + move[0] < 1 or column + move[0] > 8:
        continue
    elif row + move[1] < 1 or row + move[1] > 8:
        continue
    else:
        count += 1

print(count)