'''
파일명 : Ex05-O(n^2).py

- O(n^2): 제곱 시간 복잡도, 중첩 반복문을 사용하는 알고리즘

선택 정렬
'''

def selection_sort(arr):
    '''
    arr = [5, 3, 4, 1, 2]
    len = 5
    
    1-1
    i = 0
    j = 1
    min_idx = 1
    
    1-2
    i = 0
    j = 2
    min_idx = 1
    
    1-3
    i = 0
    j = 3
    min_idx = 3
    
    1-4
    i = 0
    j = 4
    min_idx = 3
    
    1-5
    i = 0
    j = 5
    min_idx = 3
    arr = [1, 3, 4, 5, 2]
    
    이것이 한 바퀴 루틴이다. i값이 1씩 늘어가면서 최소값을 찾으며 정렬의 위치를 바꾼다.
    '''
    
    for i in range(len(arr)): # i는 0부터 4까지
        min_idx = i
        
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        # =를 기준으로 첫 번째끼리, 두 번째끼리 값이 바뀐다. arr[i]가 arr[min_idx]로, arr[min_idx]가 arr[i]로 바뀜. 파이썬에만 이런 수식이 가능하다.
        '''
        다른 언어에서는 이런 수식 사용이 불가능하고 임시저장변수를 이용해 서로의 값을 바꾸는 것이 가능하다.
        temp = arr[i]
        arr[i] = arr[min_idx]
        arr[min_idx] = temp
        '''

    return arr

# 실행 코드
arr = [5, 3, 4, 1, 2]
print(selection_sort(arr))