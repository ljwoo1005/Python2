'''
4. 퀵 정렬(Quick Sort)
    분할 정복 알고리즘의 일종. 
    기준점(pivot)을 설정하고 pivot보다 작은 값을 왼쪽, 큰 값을 오른쪽으로 분할한 후 각 부분 리스트에 대해 재귀적으로 퀵 정렬을 수행하는 알고리즘.
    
    최악의 경우 시간복잡도 : O(n^2)
    최선의 경우 시간복잡도 : O(n*log n)
    평균 시간복잡도 : O(n*log n)
'''

# 퀵 정렬을 알고리즘으로 구현하는 함수
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    '''
    arr = [6, 5, 3, 1, 8, 7, 2, 4]
    
    pivot = 6
    left = []
    right = []
    equal = []
    
    a = 6
    a = pivot
    equal = [6]
    
    a = 5
    a < 6
    left = [5]
    
    a = 3
    3 < 6
    left = [5, 3]
    
    a = 1
    1 < 6
    left = [5, 3, 1]
    
    a = 8
    8 > 6
    right = [8]
    
    a = 7
    7 > 6
    right = [8, 7]
    
    a = 2
    2 < 6
    left = [5, 3, 1, 2]
    
    a = 4
    4 < 6
    left = [5, 3, 1, 2, 4]
    
    quick_sort([5, 3, 1, 2, 4])
        arr = [5, 3, 1, 2, 4]
        pivot = 5
        left = [3, 1, 2, 4]
        right = []
        equal = [5]
        
        quick_sort([3, 1, 2, 4])
            arr = [3, 1, 2, 4]
            pivot = 3
            left = [1, 2]
            right = [4]
            equal = [3]
            
            quick_sort([1, 2])
                arr = [1, 2]
                pivot = 1
                left = []
                right = [2]
                equal = [1]
                left + equal + right
                -> [1, 2]
            equal -> 3
            right -> 4
            left + equal + right
            -> [1, 2, 3, 4]
        equal -> 5
        right -> []
        left + equal + right
        -> [1, 2, 3, 4, 5]
    equal -> 6
    right -> [7, 8] # 과정 생략
    left + equal + right
    -> [1, 2, 3, 4, 5, 6, 7, 8]
    '''
    
    # pivot 값 설정
    pivot = arr[0]
    
    left, right, equal = [], [], []
    for a in arr:
        if a < pivot:
            left.append(a)
        elif a > pivot:
            right.append(a)
        else:
            equal.append(a)
    
    return quick_sort(left) + equal + quick_sort(right)

# 실행 코드
arr = [6, 5, 3, 1, 8, 7, 2, 4]
print(quick_sort(arr))