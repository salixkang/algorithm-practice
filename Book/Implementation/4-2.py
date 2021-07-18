# time

n = int(input())

count = 0
for hour in range(n+1):
    if hour % 10 == 3:
        count += 60 * 60
    else:
        for minute in range(60):
            if minute % 10 == 3 or minute // 10 == 3:
                count += 60
            else:
                for second in range(60):
                    if second % 10 == 3 or second // 10 == 3:
                        count += 1

print(count)