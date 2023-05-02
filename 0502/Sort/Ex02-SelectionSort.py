'''
파일명: Ex02-SelectionSort.py
2. 선택정렬
  주어진 리스트에서 최소값을 찾아 맨 앞에 있는 값과 교체하는 알고리즘
  
  시간복잡도 : O(n^2)
'''


# 선택 정렬 알고리즘을 구현하는 함수
def selection_sort(arr):
    # 배열의 길이만큼 반복합니다. i는 현재 정렬할 원소의 인덱스입니다.
    for i in range(len(arr)):
        # 최소값의 인덱스를 저장할 변수 min_idx를 현재 인덱스 i로 초기화합니다.
        min_idx = i

        # i+1부터 배열의 끝까지 탐색하여 최소값을 찾습니다.
        for j in range(i + 1, len(arr)):
            # 현재 탐색 중인 원소 arr[j]가 최소값보다 작으면 min_idx를 j로 업데이트합니다.
            if arr[j] < arr[min_idx]:
                min_idx = j

        # 최소값을 찾은 후에 최소값과 현재 정렬할 원소(arr[i])를 교환합니다.
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    # 정렬이 완료된 배열을 반환합니다.
    return arr

# 실행코드 
arr = [5, 3, 4, 1, 2]
print(selection_sort(arr))