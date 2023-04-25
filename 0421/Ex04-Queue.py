'''
큐(Queue)
    컴퓨터의 기본적인 자료 구조의 한 가지로, 먼저 집어넣은 데이터가 먼저 나오는 FIFO(First In First Out) 구조로 저장하는 형식을 말한다.
'''

def Queue():
    queue = []
    queue.append(1)
    queue.append(2)
    queue.append(3)
    queue.append(4)
    queue.append(5)
    while queue:
        print('Get Value :', queue.pop(0))
        
# 실행 코드
Queue()