# ============= merge sort =====================
# 핵심코드 -> 잘 이용하면 다른데에 다 그대로 적용하면 풀릴거임

# 반으로 나눴을때 오름차순으로 되는 배열인걸 가정했을때
# arr = [2, 3, 5, 7, 1, 2, 5, 9]
# start = 0
# end = 7
# mid = (start + end) // 2
#
# a = start
# b = mid + 1
# result = []
#
# while 1:
#     if a > mid and b > end: break
#     # a가 먼저 절반으로 나눈 배열의 끝에 다다랐을때 남은 b를 배열에 넣어줌
#     if a > mid:
#         result.append(arr[b])
#         b += 1
#     # b가 먼저 절반으로 나눈 배열의 끝에 다다랐을때 남은 a를 배열에 넣어줌
#     elif b > end:
#         result.append(arr[a])
#         a += 1
#     elif arr[a] <= arr[b]:
#         result.append(arr[a])
#         a += 1
#     else:
#         result.append(arr[b])
#         b += 1
#
# print(*result)

# ------merge sort 실전 코드--------
# arr = [2, 7, 5, 3, 1, 5, 9, 2]
#
# def merge(start, end):
#     if start == end:
#         return
#     mid = (start + end) // 2
#
#     merge(start, mid)
#     merge(mid+1, end)
#
#     a = start
#     b = mid + 1
#     result = []
#
#     while 1:
#         if a > mid and b > end: break
#         # a가 먼저 절반으로 나눈 배열의 끝에 다다랐을때 남은 b를 배열에 넣어줌
#         if a > mid:
#             result.append(arr[b])
#             b += 1
#         # b가 먼저 절반으로 나눈 배열의 끝에 다다랐을때 남은 a를 배열에 넣어줌
#         elif b > end:
#             result.append(arr[a])
#             a += 1
#         elif arr[a] <= arr[b]:
#             result.append(arr[a])
#             a += 1
#         else:
#             result.append(arr[b])
#             b += 1
#     for i in range(len(result)):
#         arr[start+i] = result[i]
#
# merge(0, 7)
# print(*arr)

# =================== Quick Sort ======================
# 핵심 코드 -> pivot 기준으로 왼쪽은 pivot 보다 작은값들만, 오른쪽은 pivot 보다 큰 값들만 들어가 있음
#            (근데 그 왼쪽 오른쪽 영역안에서는 오름차순으로 정렬되어 있지는 않음)

# arr = [4, 7, 1, 6, 2, 8, 5, 3, 9]
# start = 0
# end = 8
# pivot = start
# a = start + 1
# b = end
#
# while 1:
#     # a 가 배열 범위 안이고, a 의 값이 pivot 보다 작다면 a 값을 계속 증가 시킴
#     while a <= end and arr[a] <= arr[pivot]: a += 1
#     # b 가 배열 범위 안이고, b의 값이 privot 보다 크다면 b 값 계속 감소 시킴
#     while b >= start and arr[b] > arr[pivot]: b -= 1
#     if a > b: break
#     arr[a], arr[b] = arr[b], arr[a]
# arr[b], arr[pivot] = arr[pivot], arr[b]
# print(*arr)

# ------quick sort 실전 코드--------
arr = [4, 7, 1, 6, 2, 8, 5, 3, 9]

def quick(start, end):
    if start >= end:
        return
    pivot = start
    a = start + 1
    b = end

    while 1:
        # a 가 배열 범위 안이고, a 의 값이 pivot 보다 작다면 a 값을 계속 증가 시킴
        while a <= end and arr[a] <= arr[pivot]: a += 1
        # b 가 배열 범위 안이고, b의 값이 privot 보다 크다면 b 값 계속 감소 시킴
        while b >= start and arr[b] > arr[pivot]: b -= 1
        if a > b: break
        arr[a], arr[b] = arr[b], arr[a]
    arr[b], arr[pivot] = arr[pivot], arr[b]

    quick(start, b-1)
    quick(b+1, end)

quick(0, 8)
print(*arr)