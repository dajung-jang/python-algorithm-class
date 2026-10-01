# 동전 잔돈 구하기
coin = [500, 50, 100, 10]
target = 1110
coin.sort(reverse=True)

cnt = 0
for i in range(4):
    temp = target // coin[i]
    cnt += temp
    target -= (temp * coin[i])
print(cnt)