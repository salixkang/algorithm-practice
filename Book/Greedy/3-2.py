# law of large numbers

n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
first = data[n-1]
second = data[n-2]

result = 0

rec = m // (k+1)
mod = m % (k+1)

result = first*k*rec + second*rec + first*mod

print(result)
