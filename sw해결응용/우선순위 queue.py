# 우선 순위 큐
import heapq
arr = []
heapq.heappush(arr, 13)     # min heap (default 값 - 우선순위 높은 값)
heapq.heappush(arr, 5)
heapq.heappush(arr, 17)
heapq.heappush(arr, 9)
print(arr)

# 우선순위 높은 값부터 출력하는 두가지 방법(min heap 부터)
# 방법 1
for i in range(len(arr)):
    print(heapq.heappop(arr), end= ' ')

# 방법 2
'''
while arr:
    node = heapq.heappop(arr)
    print(node, end=' ')
'''
print()

# ----------------------------------------------

# max heap 부터 출력
# 방법 1 : Nlog(N) 의 속도
arr = [3, 234, 23, 12, 31]
heap = []
for i in range(len(arr)):
    heapq.heappush(heap, -arr[i])

for i in range(len(arr)):
    print(heapq.heappop(heap) * -1, end = ' ')

print()

# 방법 2 : O(n) 의 속도 <- 얘가 더 빠름
arr = [3, 234, 23, 12, 31]
arr = list(map(lambda x: -x, arr))   # arr 배열의 모든 원소에 - 붙인 후, arr에 재할당
heapq.heapify(arr)
for i in range(len(arr)):
    print(heapq.heappop(arr) * -1, end = ' ')

# =============================================

