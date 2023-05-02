'''
힙(Heap)
    최대값 및 최소값 찾아내는 연산을 빠르게 하기 위해 고안된 완전 이진트리를 기본으로 한 자료구조
    라이브러리가 구현되어 있다.
'''

import heapq

class MinHeap:
    def __init__(self):
        self.heap = []
        
    def push(self, val):
        heapq.heappush(self.heap, val)
        
    def pop(self):
        return heapq.heappop(self.heap)
    
# 실행코드
heap = MinHeap()
heap.push(3)
heap.push(1)
heap.push(4)
heap.push(2)
                      
print('=== MinHeap ===')
print(heap.pop())
print(heap.pop())
print(heap.pop())
print(heap.pop())

# heapq 라이브러리는 MinHeap을 기준으로 만들어졌다. MaxHeap을 하기 위해선 value값에 -1을 하여 음수로 만들어주면 최소값이 최대값이 된다.
class MaxHeap:
    def __init__(self):
        self.heap = []
        
    def push(self, val):
        heapq.heappush(self.heap, -val)
        
    def pop(self):
        return -heapq.heappop(self.heap)
    
# 실행코드
heap2 = MaxHeap()
heap2.push(3)
heap2.push(1)
heap2.push(4)
heap2.push(2)

print('=== MaxHeap ===')
print(heap2.pop())
print(heap2.pop())
print(heap2.pop())
print(heap2.pop())