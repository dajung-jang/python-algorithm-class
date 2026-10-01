# 이미 정렬된 배열이어야지 이진 탐색이 의미가 있음
# 정렬된 data를 logN 속도로 계산

arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
# 지금 배열은 정렬 되어 있긴 하지만 정렬 안돼있을 배열일 경우를 위해
arr.sort()
target = 20
check = False

# ------- while 사용할 경우 ( for 이나 while 사용 가능할 경우 재귀보단 for, while 사용하는게 좋음)
# start = 0
# end = len(arr) - 1
#
# while 1:
#     mid = (start + end) // 2
#     if arr[mid] == target:
#         check = True
#         break
#     if arr[mid] < target:   # 찾고자 하는 값이 중간값 보다 크다면 : 우측 탐색
#         start = mid + 1
#     if arr[mid] > target:   # 찾고자 하는 값이 중간값 보다 작다면 : 좌측 탐색
#         end = mid - 1
#     if start > end:
#         break
# if check:
#     print("찾았음")
# else: print('못찾음')

# --------- 재귀 사용할 경우 (공부삼아 하는거지 이진 검색 구현할 일 있으면 while 로 사용 권장)

def binary_search(start, end):
    global check
    if start > end:
        return
    mid = (start + end) // 2
    if target == arr[mid]:
        check = True
        return
    if arr[mid] < target:
        binary_search(mid+1, end)
    else:
        binary_search(start, mid-1)

binary_search(0, 14)
if check:
    print('찾았음')
else:
    print('못찾음')

# ========================================
# ------------- parametric search ---------------------
# binary serch 랑 코드가 똑같음

bettery = '*******___'

def parametric_search(start, end):
    Max = -1
    while 1:
        mid = (start + end) // 2
        if bettery[mid] == '_':
            end = mid - 1
        elif bettery[mid] == '*':
            Max = mid
            start = mid + 1
        if start > end:
            break
    return Max + 1

answer = parametric_search(0, 9)
print(answer)