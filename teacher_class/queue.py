# ====================== Queue ==========================
'''
* stack(후입선출) : append, pop -> DFS의 흔적배열(path) -> 재귀호출
* queue(선입선출) : append, pop(0) -> BFS에 응용 -> 재귀호출X
* BFS + 우선순위 큐 => 다익스트라

* queue 동작 원리
arr = []
arr.append(1)
arr = [1]
arr.append(2)
arr = [1, 2]
arr.append(3)
arr = [1, 2, 3]

선입선출 : 먼저 들어온게 먼저 빠진다

arr.pop(0) == 1
arr.pop(0) == 2
arr.pop(0) == 3


* import deque 를 사용하는 이유
    - pop(0) 의 단점: 안에 element들이 앞으로 한칸씩 이동함(땡겨짐) -> n개면 시간복잡도가 O(n)
    그런데, popleft()를 쓰면 맨 앞의 element 만 제거 -> 시간복잡도가 O(1) -> 더 빠름
    ==> popleft() 는 import deque를 해야 사용 가능
'''

# ====================== 우선순위 Queue ==========================
'''
* 4, 7, 2, 5, 6, 8 -> 최소값을 pop하고 싶다 -> 정렬 sort() : 시간복잡도 O(NlogN) -> 느림
                                       ==> 그래서 우선순위 Queue 쓰는 거임 : 시간복잡도 O(logN) ==> 최소힙 이라고 부름
                                       
* 우선순위 큐 시간 복잡도
push : O(logN)      pop : O(logN)       top : O(1)

우선순위 큐 : 우선순위가 높은 것을 우대한다. (단, 파이썬은 최소힙) 
: java, c++ : default 가 최대힙, python : default 가 작은값이 우선순위가 높다(최소힙)

* 힙트리 : 이진트리인데 왼쪽부터 채워져야한다.

* heap.heappush
1. 힙트리 구조 (heap이라고 불리는 tree 로 구현)
2. 항상 부모가 자식보다 작아야 한다. (힙속성)  ===> 부모-자식 이 바뀌는 시간 복잡도 : O(logN)

* heap.heappop
1. 힙트리 구조
2. 맨 위의(조상) 노드가 제거(반환)
3. 마지막 노드가 맨위의 노드로 대체
4. 부모가 자식보다 작아야 한다.

=> heappop 으로 pq가 빌 때까지 반복 -> while pq

'''

import heapq

pq = []
heapq.heappush(pq, 5)
heapq.heappush(pq, 2)
heapq.heappush(pq, 8)
heapq.heappush(pq, 1)
heapq.heappush(pq, 9)

print(pq)   # 결과 : [1, 2, 8, 5, 9]

# ====================== BFS ==========================
'''
* 노드 (node) : 노드번호, 노드값
* 간선 (edge) : 단방향, 양방향

* 트리와 그래프의 차이
    - 그래프가 더 넓은 넘위
    - 트리는
        1. cycle이 없다 (자기 자신으로 돌아올 수 있어야 함)
        2. 부모 자식 관계가 있다
    - cycle 이 있는 그래프 : cycle 이 있기 때문에 무한 루프에 빠질 수 있음
                            -> cycle 방지 코드 : visited 배열, used 배열 (dat 응용)         
'''

# ====================== 코드 ==========================

# 최소힙, 최대힙
# 다중조건 힙 -> 다익스트라 (BFS + 가중치)

# 1. 최소힙
import heapq
pq = []

heapq.heappush(pq, 3)
heapq.heappush(pq, 1)
heapq.heappush(pq, 8)
heapq.heappush(pq, 4)

print(pq)   # 힙트리 구조

while pq:
    print(heapq.heappop(pq), end=' ')

# 2. 최대힙
pq = []

# 2-1. heappush 할 때 음수로
heapq.heappush(pq, -3)
heapq.heappush(pq, -1)
heapq.heappush(pq, -8)
heapq.heappush(pq, -4)

print(pq)   # 힙트리 구조

while pq:
    # 2-2. heappop 한 후 다시 -를 붙여서
    print(-heapq.heappop(pq), end=' ')

# 3. 다중조건 힙 -> 1순위: 정수(작은것 부터) / 만약 같은 정수면 문자열 순서로 정렬
pq = []
heapq.heappush(pq, (2, 'A'))    # (정수, 문자열)
heapq.heappush(pq, (2, 'B'))
heapq.heappush(pq, (4, 'C'))
heapq.heappush(pq, (3, 'C'))

while pq:
    print(heapq.heappop(pq), end=' ')