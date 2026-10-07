# 보스는 자기 자신으로 초기화
boss = [i for i in range(10)]

# Union함수, Find함수 암기!!!
def Find(n):
    if boss[n] == n:   # 가리키는 보스가 자기 자신이면
        return n    # -> 최종 보스니까 그대로 출력

    result = Find(boss[n])  # 재귀호출
    boss[n] = result    # 경로압축 (이 코드 한줄이면 더 효율적)
    return result

def Union(t1, t2):
    a = Find(t1)    # t1의 보스가 a다
    b = Find(t2)    # t2의 보스가 b다
    if a == b: return   # 이미 보스가 같으면 탈락 -> return
    boss[b] = a     # b의 보스가 a다

Union(7, 3)
Union(2, 4)
Union(2, 6)
Union(3, 4)

a, b = map(int, input().split())
# 논리 : 보스가 같으면 같은 그룹이다.
if Find(a) == Find(b): print('O')
else: print('X')