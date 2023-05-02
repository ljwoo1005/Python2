'''
빅오 표기법(Big O notation)
    알고리즘의 시간 복잡도와 공간 복잡도를 분석할 때 사용되는 표기법
    입력 크기 n에 대한 함수 f(n)의 실행 시간이나 메모리 사용량을 나타낸다.
    !!빅오 표기법은 최악의 경우에 대한 성능 표현
    
빅오 표기법의 규칙
    상수는 무시 : O(2n) -> O(n), O(3n^2) -> O(n^2)
    낮은 차수의 항은 무시 : O(n^2 + n) -> O(n^2), O(n^3 + 100n^2) -> O(n^3)
'''

# O(1) : 상수 시간 복잡도. 입력 크기와 상관없이 일정한 시간이 걸린다.

def return_first_value(arr):
    '''
    안쪽에 매개변수를 포함하지 않은 어떠한 코드를 넣더라도 시간복잡도는 1이다.
    print(1)이 1천개 들어가도 O(1)이다.
    '''
    return arr[0]

# 실행 코드
arr = [1, 3, 5, 7, 8]
print(return_first_value(arr))

# python.exe -m pip install --upgrade pip