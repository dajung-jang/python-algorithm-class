# =============== 인접 행렬 DFS ===============
# = 가능한 모든 정점 1번씩 탐색
'''
name = 'BACD'
arr = [
    [0, 0, 1, 1],
    [1, 0, 1, 0],
    [1, 0, 0, 1],
    [0, 0, 0, 0]
]
used = [0] * 4  # 정점의 개수 만큼

def dfs(now):
    print(name[now], end = ' ')
    for i in range(4):  # 정점의 개수만큼 반복
        if arr[now][i] == 1 and used[i] == 0:
            used[i] = 1
            dfs(i)

used[1] = 1 # 탐색 시작 인덱스에 1 중복 체크
dfs(1)  # 탐색 시작 인덱스
'''

# ==================================================================
# =========== 인접 리스트 DFS (메모리 낮음, 수행시간 짧음) ===============
'''
#  - 가능한 모든 정점 1번씩 탐색

# 입력 예시
# 4 6
# 0 2
# 0 3
# 1 0
# 1 2
# 2 0
# 2 3
name = 'BACD'
# 입력 받은 내용 저장
n, m = map(int, input().split())    # 정점, 간선 정보의 개수
arr = [[] for _ in range(n)]  # 정점의 개수만큼
for _ in range(m):
    start, end = map(int, input().split())
    arr[start].append(end)
    # 만약 무방향일 경우 반대의 상황도 추가로 arr에 저장해주면 됨
    # arr[end].append(start)
used = [0] * n

def dfs(now):

    print(name[now], end = ' ')
    for i in arr[now]:
        if used[i] == 0:
            used[i] = 1
            dfs(i)

used[1] =1  # DFS 시작 인덱스에 1 체크
dfs(1)
'''

# ------------------------------------------------------------
#  - 시작점부터 도착지까지 갈수 있는 경로가 몇가지 있는지? (한 정점(시작점)에서 다른 정점(도착지)까지의 도착할 수 있는 방법이 몇가지?)

# a ~ d 까지의 방법 개수
name = 'BACD'
# 입력 받은 내용 저장
n, m = map(int, input().split())    # 정점, 간선 정보의 개수
arr = [[] for _ in range(n)]  # 정점의 개수만큼
for _ in range(m):
    start, end = map(int, input().split())
    arr[start].append(end)
used = [0] * n
cnt = 0

def dfs(now):
    global cnt
    if now == 3:    # if name[now] == 'D' -> 같은 의미
        cnt += 1

    for i in arr[now]:
        if used[i] == 0:
            used[i] = 1
            dfs(i)
            used[i] = 0

used[1] =1  # DFS 시작 인덱스에 1 체크
dfs(1)
print(cnt)