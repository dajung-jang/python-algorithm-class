
# 중복  순열 - 재귀함수 사용

# level = 3
# branch = 4

card = 'ABCD'
path = [""] * 3 # 경로 저장하는 배열의 크기는 = level

# path에 새로운 값 덮어씌움
def abc(level):
    if level == 3:
        for i in range(level):
            print(path[i], end=' ')
        print()
        return

    for i in range(4):
        # 일단 들어갈 곳을 적고 들어갈거임
        path[level] = card[i]
        abc(level+1)

abc(0)

# path에 원래 있던 값 지우고 새로운 값 넣기
def abc(level):
    if level == 3:
        for i in range(level):
            print(path[i], end=' ')
        print()
        return

    for i in range(4):
        # 일단 들어갈 곳을 적고 들어갈거임
        path[level] = card[i]
        abc(level+1)
        path[level] = 0
abc(0)

# =================
# 주사위 n개 던졌을 때 나올 수 있는 경우의 수
n = int(input())
path = [0] * n

def abc(level):
    if level == n:
        print(*path)
        return

    for i in range(1, 7):
        path[level] = i # 내가 앞으로 들어갈 곳을 path에 기록하고 다음으로 들어감
        abc(level+1)

abc(0)

# 카드 4개 중에 3개 뽑는 경우의 수 (그냥 순열 -> 중복 X)
card = "ABCD"
path = [''] * 3
used = [0] * 4  # branch 크기
def abc(level):
    if level == 3:
        print(*path)
        return

    for i in range(4):
        if used[i] == 1: continue   # 방문한 적이 있는지 확인
        used[i] = 1                 # 방문 체크해주기
        path[level] = card[i]       # 앞으로 들어갈 경로 적기
        abc(level+1)                # 다음 함수 들어가기
        path[level] = 0             # 경로 적었던 것 지우고
        used[i] = 0                 # 방문 체크 해제

abc(0)
print()


# 누적합 구하기

# 지역ㅂ변수
arr = [3, 4, 7, 1, 6]
cnt = 0
def abc(level, Sum):
    global cnt
    if Sum > 10:    # 가지치기
        return
    if level == 3:
        if Sum == 10:
            cnt += 1
        return

    for i in range(5):
        abc(level+1, Sum+arr[i])    # level 1씩 증가 / Sum 내가 앞으로 들어갈 가지 더하기

abc(0, 0)
print(cnt)

# 전역변수
arr = [3, 4, 7, 1, 6]
cnt = 0
Sum = 0
def abc(level):
    global cnt, Sum

    if level == 3:
        if Sum == 10:
            cnt += 1
        return

    for i in range(5):
        Sum += arr[i]
        abc(level+1)
        Sum -= arr[i]   # 전역변수로 사용하면 더하고 들어갔으면 나올때 빼줘야하는 것 잊지 말기

abc(0)
print(cnt)