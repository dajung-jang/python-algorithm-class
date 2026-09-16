# DAT (Direct Address Table) 자료 구조

# 카운팅 정렬 -> O(n+k)
# 대부분 다른 정렬은 -> O(n^2) 이상

# 자료구조 -> data 를 어떻게 저장할 것인가 선택의 힘이 생긴다.
# 스택에 저장할 지, 큐에 저장할 지, 힙에 저장할지, 그래프에 저장할지

# DAT = "값을 인덱슬 쓰는 자료구조"

# 예시 코드
arr = [4, 2, 4, 4, 2] # 값은 최대 4

dat = [0] * 5   # 인덱스는 0부터 4까지
idx = 0

for i in range(len(arr)):
    idx = arr[i]    # 값을 인덱스로 할당
    dat[idx] += 1   # counting

for i in range(len(arr)):
    if dat[i] > 0 : print(f'{i} : {dat[i]}개')
