# card sort
# https://www.acmicpc.net/problem/1715
import heapq

n = int(input())
cards = []
for _ in range(n):
    cards.append(int(input()))
heapq.heapify(cards)

result = 0
while len(cards) > 2:
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    tray = a + b
    result += tray
    heapq.heappush(cards, tray)

if n != 1:
    result += cards[0] + cards[1]
else:
    result = cards[0]
print(result)


