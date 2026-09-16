# for 문 사용해서 12345 출력하려면?

for i in range(1, 6):
    print(i, end=' ')

print()

# 만약
# 12345
# 12345
# 12345
# 출력하고 싶다면?

# 중첩 for 문(2중 for문)
for i in range(3):
    for i in range(1, 6):
        print(i, end=' ')
    print() # 줄바꿈

# --------------------------------------------------
# 순회: 행순회, 열순회, 지그재그순회 ...
# 탐색 : 내가 원하는 것을 찾는 것
# 완전탐색 : 모든 경우의 수를 전부 확인하는 것

# ex1) 탐색하여 1이 몇개인지 counting
arr = [1, 4, 6, 1, 1, 9, 6]
# 1. 전체 순회
# 2. cnt 변수 활용

cnt = 0
for a in arr:
    if a == 1: cnt += 1

print(cnt)

# --------------------------------------------------

# [0] * 4 1차원 배열 -> 4번 반복
arr = []
# for _ in range(4):
#     arr.append([0] * 4)

arr = [[0] * 4 for _ in range(4)]

print(arr)

# --------------------------------------------------

# 2차원 리스트 입력 받기

# 기본 방식 (어떤 흐름으로 받아지는지 이해)
arr = []
for _ in range(4):
    lst = list(map(int, input().split()))   # 1차원 리스트
    arr.append(lst)

# 리스트 컴프리헨션 사용 방식
arr = [list(map(int, input().split())) for _ in range(4)]

# --------------------------------------------------
