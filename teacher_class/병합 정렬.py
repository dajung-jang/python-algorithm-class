# 분할 : 문제를 더 작은 부분으로 나눈다
# 정복 : 나눈 부분을 각각 해결한다
# 병합 : 하위 문제를 합쳐 해결책을 만든다

def merge_sort(arr):
    # 배열의 길이가 1이하면 이미 정렬되었다 return 처리
    if len(arr) <= 1: return arr

    # 배열을 반으로 나누기 위해 middle 구하기
    mid = len(arr) // 2
    # 왼쪽 절반을 재귀적으로 정렬
    left = merge_sort(arr[:mid])
    # 오른쪽 절반을 재귀적으로 정렬
    right = merge_sort(arr[mid:])
    # 정렬된 왼쪽과 오른쪽 배열을 병합
    result = merge(left, right)

    return result

def merge(left, right):
    result = []
    # 왼쪽과 오른쪽
    i, j = 0, 0
    # 왼쪽과 오른쪽 배열을 비교하면서 병합 -> while문
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            # 왼쪽 element가 작거나 같으면 result에 append
            result.append(left[i])
            # 그 다음 element로 이동
            i += 1
        else:
            # 오른쪽 element가 작으면 result에 append
            result.append(right[j])
            # 그 다음 element로 이동
            j += 1
    # 왼쪽 배열에 남은 것들을 result에 extend
    result.extend(left[i:])
    # 오른쪽 배열에 남은 것들을 result에 extend
    result.extend(right[j:])
    # 병합 끝났으면 결과 반환
    return result

# 하드코딩
arr = [64, 34, 25, 12, 22, 11, 90]
# 병합 정렬 함수 호출
sorted_arr = merge_sort(arr)

print(sorted_arr)