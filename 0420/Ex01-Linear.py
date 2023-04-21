'''
선형리스트(LinearList)
    간단한 자료구조 중 하나로, 데이터를 일렬로 나열한 것이다.
'''

class LinearList():
    def __init__(self):
        self.linear = [] # 멤버변수로 빈 리스트 생성
        
    # 순차적으로 데이터를 추가하는 메서드
    def add_data(self, data): # 리스트에 데이터 추가 메서드
        linear = self.linear # 멤버변수를 메서드의 객체로 사용
        linear.append(None) # 리스트에 빈 칸 추가
        linearSize = len(linear) # 리스트의 현재 크기
        linear[linearSize - 1 ] = data # 리스트의 빈 칸에 데이터 삽입
    
    # 리스트 출력 메서드
    def print_list(self):  
        linear = self.linear
        for list in linear:
            print(list, end=' ') # 리스트 타입의 출력이 아니라 요소들을 하나하나 꺼내서 출력
            
    # 중간에 데이터를 삽입하는 메서드
    # 먼저 리스트 맨 끝에 빈 칸을 생성하고, 삽입하고자 하는 위치의 인덱스부터 뒷부분을 뒤로 한 칸씩 밀어낸다.
    # 삽입하고자 하는 위치의 인덱스가 빈 칸이 되고, 그 곳에 데이터를 삽입한다.
    def insert_data(self, position, data): # 매개변수로 삽입할 위치와 삽입할 데이터를 설정
        linear = self.linear
        if position < 0 or position > len(linear): # 유효성 검사
            print('데이터를 삽입할 범위를 벗어났습니다.')
            return
        
        linear.append(None) # 빈칸 추가
        linearSize = len(linear) # 리스트의 현재 크기
        
        # 삽입할 위치의 인덱스부터 뒷부분 요소들을 한 칸 씩 뒤로 이동
        # 리스트가 [1, 2, 3, 4, 5] 총 5개의 요소가 있다고 가정해보자.
        # 위의 코드에서 공백을 추가하여 리스트는 [1, 2, 3, 4, 5, None]이 되었다.
        # 만약 인덱스 3번에 데이터를 삽입하고자 한다면 3번 인덱스를 4번으로, 4번 인덱스를 5번으로 밀어내야 한다.
        # 공백이 마지막에 있기 때문에 뒤에서부터 데이터를 뒤로 밀어내야 한다.
        for i in range(linearSize-1, position, -1): # 리스트 요소를 역순으로 읽어와야 한다.
            linear[i] = linear[i-1] # i가 5일 때, linear[5]의 자리에 linear[4]를 대입한다.
            linear[i-1] = None # linear[4]를 빈 칸으로 만든다.
            
        linear[position] = data # 리스트에 데이터 삽입
        
    # 데이터 삭제 메서드
    def delete_data(self, position): # 삭제할 데이터의 인덱스를 매개변수로 설정
        linear = self.linear
        
        if position < 0 or position > len(linear): # 유효성 검사
            print('데이터를 삽입할 범위를 벗어났습니다.')
            
        linear[position] = None # 해당 위치 데이터 삭제
        linearSize = len(linear)
        
        # 삭제한 위치 이후의 요소들을 한 칸 씩 앞으로 이동
        for i in range(position + 1 , linearSize): # 이번엔 공백이 앞에 있기 때문에 요소를 앞에서부터 읽어온다.
            linear[i - 1] = linear[i] # i가 3일 때, linear[2]의 자리에 linear[3]를 대입한다. 
            linear[i] = None # linear[3]을 비운다.
            
        del(linear[linearSize -1]) # 최종적으로 맨 마지막 요소는 None이 된다. 그것을 제거한다.


# 실행 코드
linear = LinearList() # linear에 클래스 LinearList()를 선언
linear.add_data(3)
linear.add_data(5)
linear.add_data(4)
linear.add_data(2)
linear.add_data(6)

linear.insert_data(3, 99)

linear.delete_data(2)

linear.print_list() # 리스트 출력
