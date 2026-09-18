
name = 'BTAR'

# 인접행렬
MAP = [
    [0, 0, 0, 0],
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [1, 1, 0, 0]
]

n = int(input())
for i in range(4):  # 노드의 개수가 4개
    # n 번 노드가 누굴 좋아하냐?
    # if MAP[n][i] == 1:
    #     print(name[i])
    if MAP[n][i] == 0: continue
    print(name[i])

# # 인접리스트 VS 인접행렬
# # 인접리스트가 더 빠르다. 인접행렬은 0으로 채워져 있기 때문에
# # 그런데, 가중치가있는 경우 인접행렬이 더 편하다

# 인접 리스트

alist = [[] for _ in range(4)]

alist[1] = [0, 3]
alist[2] = [1, 3]

print(alist)