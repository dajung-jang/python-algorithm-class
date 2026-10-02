# N-Queens 문제
# N * N 사이즈의 체스판에 N개의 퀸을 방해 없이 놓을 수 있는 경우 그 경우가 몇가지??

# branch 4 // level 4
# vertical = [j]
# seven = [i+j]
# five = [i-j+n]

n = int(input())    # 체스판의 크기
vertical = [0] * n
seven = [0] * (2 * n)
five = [0] * (2 * n)

cnt = 0
def abc(level):
    global cnt
    if level == n:
        cnt += 1
        return

    for j in range(n):
        if vertical[j] == 1: continue
        if seven[level + j] == 1 or five[level - j + n] == 1: continue  # 가지치기
        vertical[j], seven[level + j], five[level - j + n] = 1, 1, 1
        abc(level + 1)
        vertical[j], seven[level + j], five[level - j + n] = 0, 0, 0    # 백트래킹 개념

abc(0)
print(cnt)
