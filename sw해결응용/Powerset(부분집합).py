name = 'ABC'

def abc(level, path):
    if level == 3:
        print(*path)
        return

    abc(level + 1, path)
    abc(level + 1, path + [name[level]])

abc(0, [])

# 비트연산자
# 함수 없이 for 문으로만 할 경우
arr = ['A', 'B', 'C']
n = len(arr)

for tar in range(1 << n):
    answer = []
    for i in range(n):
        if tar & 1:        # if tar & 0x1: <- 이렇게 써도 됨 / 같은 의미
            answer.append(arr[i])
        tar >>= 1
    print(answer)

# 함수 사용
arr = ['A', 'B', 'C']
n = len(arr)

def get_sub(tar):
    for i in range(n):
        if tar & 0x1:
            print(arr[i], end=' ')
        tar >>= 1       # 검사한 한 자리를 제거
for tar in range(1 << n):   # range(0, 8)
    print('{', end= ' ')
    get_sub(tar)
    print('}')

# ---------------------------
# 친구와 카페 방문
# 민철이 친구가 arr
# 이 중 최소 2명 이상의 친구와 함께 카페에 가려고 할 때 총 몇가지 경우가 가능한가요?

arr = ['A', 'B', 'C', 'D', 'E']
n = len(arr)

for tar in range(1 << n):
    answer = []
    for i in range(n):
        if tar & 1:        # if tar & 0x1: <- 이렇게 써도 됨 / 같은 의미
            answer.append(arr[i])
        tar >>= 1
    if len(answer) >= 2:
        print(answer)