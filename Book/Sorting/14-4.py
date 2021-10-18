# card sort
# https://www.acmicpc.net/problem/1715

n = int(input())
cards = []
for _ in range(n):
    cards.append(int(input()))

cards.sort()

result = 3e9
compare = [cards[0]]
temp = 0
for idx, card in enumerate(cards[1::]):
    for e in compare:
        if e <= card:
            