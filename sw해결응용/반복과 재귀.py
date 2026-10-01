# 주사위 3개 던졌을 때 나올 수 있는 경우 (= for )

for k in range(1, 7):
    for i in range(1, 7):
        for j in range(1, 7):
            print(k, i, j)

# 주사위 n개 던졌을 때 나올 수 있느 ㄴ경우
# -> for 문으로 못함 => 재귀함수

n = int(input())
path = [0] * n

def abc(level):
    if level == n:
        print(*path)
        return
    for i in range(1, 7):
        path[level] = i
        abc(level + 1)

abc(0)

# =========================
def kfc(test):
    print(test)
    print('!!')

def abc(test):
    print('#')
    print(test)
    kfc(456)
    print('**')
    print(test)

def bbq():
    abc(123)
    print('@')

bbq()

# =========================
# 재귀함수

def abc(level):
    # 레벨 확인용 print -> 출력 결과 0 1 2
    print(level, end=' ')
    # 함수 종료 조건
    if level == 2:
        return

    abc(level + 1)
    # 레벨 확인용 print -> 출력 결과 1 0
    print(level, end=' ')

abc(0)

print()
# -----------------------
# 출력 해야하는 것
# 0 1 2 3 2 1 0
def fun1(x):
    print(x, end= ' ')
    if x == 3:
        return
    fun1(x + 1)
    print(x, end= ' ')
fun1(0)

print()

# 0 1 2 3 4 5 5 4 3 2 1 0
def fun2(x):
    if x == 6:
        return
    print(x, end=' ')
    fun2(x + 1)
    print(x, end= ' ')

fun2(0)
print()
# ================ 누적합 구하기=================
# 재귀 DFS 구현시 변수를 global 선언하는가? 매개변수에 선언하는가? 에 따른 사이

arr = [1, 3, 5, 7]

# global 선언 시
Sum = arr[0]

def abc(level):
    global Sum

    if level == 3:
        print(Sum, end=' ')
        return

    Sum += arr[level+1]
    abc(level+1)
    # 전역 변수기때문에 최종 합만 계속 출력됨 -> 출력 결과 16, 16, 16, 16
    # print(Sum, end= ' ')
    # 그래서 sum에 누적해서 빼줘야 하나씩 누적된 합이 출력됨
    Sum -= arr[level+1]
    print(Sum, end= ' ')

abc(0)

print()
# 지역변수
def abc(level, Sum):
    if level == 3:
        print(Sum, end=' ')
        return
    abc(level+1, Sum+arr[level+1])
    print(Sum, end= ' ')
abc(0, arr[0])

# ============================
# 함수 두번 호출 될 경우

arr = [1, 3, 5, 7]

def abc(level):
    if level == 2:
        return
    abc(level+1)
    abc(level+1)
abc(0)

# ---------# 찍어서 프린트 되는 순간 연습 (print 위치 바꿔가면서 출력, 아래는 print를 넣을수 있는 모든 위치)
def abc(level):
    print('#', end=' ')
    if level == 2:
        print('#', end= ' ')
        return
    print('#', end=' ')
    for i in range(2):
        print('#', end=' ')
        abc(level + 1)
        print('#', end=' ')
    print('#', end=' ')
abc(0)