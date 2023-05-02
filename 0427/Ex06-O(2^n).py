'''
파일명 : Ex06-O(2^n).py

- O(2^n): 지수 시간 복잡도, 피보나치 수열처럼 재귀적 알고리즘
'''

'''
fibonacci(3)
3 <= 1 : false
fibonacci(2) + fibonacci(1)

    fibonacci(2)
    2 <= 1 : false
    fibonacci(1) + fibonacci(0)
    
        fibonacci(1)
        1 <= 1 : True
        return 1
        fibonacci(1) == 1

            fibonacci(0)
            0 <= 1 : True
            return 0
            fibonacci(0) == 0
    
    fibonacci(2) == 1 + 0 
        -> 1
    
fibonacci(3) == 1 + 1
    -> 2
'''

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(3))