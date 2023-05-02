'''
5. 병합 정렬(Merge Sort)
    분할 정복 알고리즘의 일종으로 리스트를 절반으로 나눈 후 각각을 재귀적으로 합병 정렬하고, 다시 합치면서 정렬하는 알고리즘
    
    최악의 경우 시간복잡도 : O(n*log n)
    최선의 경우 시간복잡도 : O(n*log n)
    평균 시간복잡도 : O(n*log n)
'''


def merge_sort(arr):
    # 리스트의 길이가 1 이하이면 정렬이 이미 끝난것으로 그대로 반환

    if len(arr) <= 1: # 정렬할 요소가 없다면
        return arr
    
    # 리스트 중간 인덱스 계산
    mid = len(arr) // 2
    '''
    arr = [5, 2, 8, 6, 1, 9, 3, 7]
    mid = 4
    
    (1)
    left = merge_sort(arr[:4]) -> merge_sort([5, 2, 8, 6])
    arr = [5, 2, 8, 6]
    mid = 2
    
        (1-1) -> left = [2, 5] # result 반환
        left = merge_sort(arr[:2]) -> merge_sort([5, 2])
        arr = [5, 2]
        mid = 1
        
            (1-1-1) -> left = 5
            left = merge_sort(arr[:1]) -> merge_sort([5])
            arr = [5]
            return arr
            
            (1-1-2) -> right = 2
            right = merge_sort(arr[2])
            arr = [2]
            
            merge([5], [2]) -> result = [2, 5]
            
        (1-2) -> right = [6, 8] # result 반환
        right = merge_sort([8, 6])
        arr = [8, 6]
        mid = 1
        
            (1-2-1) left = 8 
            left = merge_sort([8])
            arr = [8]
            
            (1-2-2) right = 6
            right = merge_sort([6])
            arr = [6]
            
            merge_sort([8, 6]) -> result = [6, 8]
            
        merge([2, 5], [6, 8]) -> result = []
        
    (2)

    
    '''
    # 중간을 기준으로 리스트를 두개로 나누어 각각 재귀적으로 정렬
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    # 두 개의 리스트를 병합하여 정렬된 리스트 생성
    return merge(left, right)

'''
left = [2, 5]
right = [6, 8]

result = 
'''
def merge(left, right):
    # 결과를 저장할 리스트 생성
    result = []
    
    # 각각의 리스트에 대해 인덱스를 따로 만들어가며 비교하여 작은 값을 결과 리스트에 추가
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    # 아직 추가하지 못한 나머지 값들을 결과 리스트에 추가
    result += left[i:]
    result += right[j:]
    
    # 정렬된 리스트 반환
    return result

# 실행 코드
arr = [5, 2, 8, 6, 1, 9, 3, 7]
sorted_arr = merge_sort(arr)
print(sorted_arr)