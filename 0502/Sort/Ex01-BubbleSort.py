'''
1. 버블 정렬(Bubble Sort)
    인접한 두 원소를 비교하여 정렬하는 알고리즘 중 하나로, 간단한 정렬 알고리즘 중 하나이다.

    최악의 경우 시간복잡도 : O(n^2)
    최선의 경우 시간복잡도 : O(n)
    평균 시간복잡도 : O(n^2)
'''

# 버블 정렬 알고리즘 함수
def bubble_sort(arr):
    # 배열의 길이
    n = len(arr)
    
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                tmp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = tmp
                # 위의 코드 3줄은 arr[j], arr[j + 1] = arr[j + 1], arr[j]과 같다.
    
    return arr

# 실행 코드
arr = [6, 5, 3, 1, 8, 7, 2, 4]
print(bubble_sort(arr))