# O(log n) : 로그 시간 복잡도. 이진 탐색처럼 문제를 절반으로 나누어 해결하는 알고리즘이다.
# 리스트가 정렬이 되어있어야 한다.

def binary_search(arr, x):
    # 검색 범위의 시작점 설정
    low = 0
    
    # 검색 범위의 끝점 설정
    high = len(arr) - 1
    
    '''
    arr = [1, 3, 5, 7, 8, 9, 10, 11, 21]
    x = 5
    
    while 0 <= 8
    low = 0
    high = 8
    mid = 4
    
    while 0 <= 3
    low = 0
    high = 3
    mid = 1
    
    while 2 <= 3
    low = 2
    high = 3
    mid = 2


    '''
    
    # 시작점이 끝점보다 작거나 같을 때까지 반복
    while low <= high:
        # 검색 범위의 중간점을 찾는다
        mid = (low + high) // 2
        
        # 중간점의 값이 찾고자 하는 값보다 작은 경우
        # 검색 범위의 시작점을 중간점 다음 인덱스로 결정
        if arr[mid] < x:
            low = mid + 1
            
        # 중간점의 값이 찾고자 하는 값보다 큰 경우
        # 검색 범위의 끝점을 중간점 이전 인덱스로 설정
        elif arr[mid] > x:
            high = mid - 1
        
        # 중간점의 값이 찾고자 하는 값과 같은 경우
        # 중간점의 인덱스를 반환
        else:
            return mid
    
    # 찾고자 하는 값이 없는 경우 -1 반환
    return -1

# 실행 코드
arr = [1, 10, 5, 7 , 8, 9, 3, 11, 21]
arr = sorted(arr)
print(arr)
print(binary_search(arr, 5))