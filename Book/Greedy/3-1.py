# Minimum number of coins to exchange N with 500, 100, 50, 10

N = 10023450

coin_num = 0

coin_num = N // 500

N = N % 500

coin_num += N // 100

N = N % 100

coin_num += N // 50

N = N % 50

coin_num += N // 10

print(coin_num)







