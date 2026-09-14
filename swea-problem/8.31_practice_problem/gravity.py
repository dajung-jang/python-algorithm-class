# 가로 N 세로 100 크기의 방에 상자들이 쌓여있다. 방이 오른쪽으로 90도 회전하여 상자들이 중력의 영향을 받아 낙하한다고 할 때, 가장 큰 낙차를 구하여라
# [제약 사항]
# 중력은 회전이 완료된 후 적용된다.
# 상자들은 모두 한쪽 벽면에 붙여진 상태로 쌓여 2차원의 형태를 이루며 벽에서 떨어져서 쌓인 상자는 없다.
# 방의 세로 길이는 항상 100이다. 즉, 상자는 최소 0, 최대 100 높이로 쌓을 수 있다
# [입력]
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스의 첫 줄에는 방의 가로길이가 주어지고 그 다음 줄부터는 쌓여있는 상자의 수가 주어진다.
# [출력]
# #부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스에 대한 답을 출력한다.
# [그림 설명]
# 총 26개의 상자가 회전 후, 오른쪽 방 그림의 상태가 된다. A 상자의 낙차가 7로 가장크므로 7을리턴하면 된다.
# 회전 결과, B상자의 낙차는6, C상자의 낙차는 1이다.

T = int(input())

for i in range(1, T+1):
    # 가로 길이
    N = int(input())
    arr = list(map(int, input().split()))

    max_v = 0

    for x in range(N-1):
        cnt = 0
        for y in range(1, N):
            if N <= x + y : break
            if arr[x] > arr[x + y]: cnt += 1
        if cnt > max_v : max_v = cnt
    print(f'#{i} {max_v}')



    # ===========================================

    # # 비교용 arr 새로 생성
    # arr_n = arr.copy()
    # for x in range(len(arr)-1, 0, -1):
    #     for y in range(x):
    #         if arr_n[y] > arr_n[y+1]:
    #             arr_n[y], arr_n[y+1] = arr_n[y+1], arr_n[y]
    #
    # max_v = 0
    # for x in range(len(arr)):
    #     if arr[x] - arr_n[x] > max_v: max_v = arr[x] - arr_n[x]
    #
    # print(f'#{i} {max_v}')