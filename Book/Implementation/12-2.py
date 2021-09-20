# string rearrangement

string_input = str(input())

asc = []
result = 0
for i in string_input:
    x = ord(i)
    if x in range(48, 58):
        result += int(i)
    elif x in range(65, 91):
        asc.append(x)

asc.sort()

for i in asc:
    print(chr(i), end = '')

print(result)