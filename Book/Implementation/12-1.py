# Lucky Straight

n = int(input())

digit = 0

element = []

for i in range(8):
    q = n // (10**i)
    r = q % 10
    element.append(r)
    if q in range(1, 10):
        digit = i + 1
        break

print(digit)
left = sum(element[:digit//2])
right = sum(element[digit//2:digit])

print(left)
print(right)
if left == right:
    print("LUCKY")
else:
    print("READY")