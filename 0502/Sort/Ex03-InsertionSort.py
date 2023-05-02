'''
3. 삽입 정렬(Insertion Sort)
    리스트의 모든 요소를 앞에서부터 차례대로 이미 정렬된 부분과 비교하여 자신의 위치를 찾아 삽입
    
    최악의 경우 시간복잡도 : O(n^2)
    최선의 경우 시간복잡도 : O(n)
    평균 시간복잡도 : O(n^2)
'''

# 삽입 정렬 알고리즘을 구현하는 함수
def insertion_sort(arr):
    
    '''
    arr = [6, 5, 3, 1, 8, 7, 2, 4]
    n = 8
    
    첫번째
    i = 1
    key = 5
    j = 0
    
    0 >= 0 and arr[0] > 5 : True
    arr[0 + 1] = arr[0] 
    arr = [6, 6, 3, 1, 8, 7, 2, 4]
    j = -1
    
    -1 >= 0 and arr[-1] > key : False
    
    arr[-1 + 1] = key : arr[0] = 5
    arr = [5, 6, 3, 1, 8, 7, 2, 4]
    
    두번째
    i = 2
    key = 3
    j = 1
    
    1 >= 0 and arr[1] > 3 : True
    arr[1 + 1] = arr[1]
    arr = [5, 6, 6, 1, 8, 7, 2, 4]
    j = 0
    
    0 >= 0 and arr[0] > 3 : True
    arr[0 + 1] = arr[0]
    arr = [5, 5, 6, 1, 8, 7, 2, 4]
    j = -1
    
    -1 >= 0 and arr[-1] > key : False
    
    arr[-1 + 1] = key : arr[0] = 3
    arr = [3, 5, 6, 1, 8, 7, 2, 4]
    '''
    n = len(arr) # 배열의 길이
    
    for i in range(1, n):
        # 현재 원소의 값을 key 변수에 저장
        key = arr[i]
        
        #현재 원소의 이전 원소 인덱스를 j 변수에 저장
        j = i - 1
        
        # 이전 원소부터 첫번쨰 원소까지 역순으로 반복하면서 key값보다 큰 원소들을 한 칸씩 오른쪽으로 이동시킨다.
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        # key값을 적절한 위치에 저장
        arr[j + 1] = key
        
    return arr

# 실행 코드
arr = [6, 5, 3, 1, 8, 7, 2, 4]
print(insertion_sort(arr))