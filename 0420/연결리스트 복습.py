'''
연결리스트(Linked List)
    저장된 각 데이터가 (데이터)+(다음 데이터의 포인터(주소값))로 이루어진 것으로
    한 방향으로만 탐색 가능한 구조이다.
    각 데이터는 노드(Node)라고 부른다.
'''

# 노드를 생성하는 클래스
class Node:
    def __init__(self, data, next=None):
        self.data = data # 노드에 저장될 데이터
        self.next = next # 다음 노드를 가리키는 포인터. Node 클래스 객체의 data의 주소값을 가진다.
# Node 클래스의 객체를 만들면 data와 next 2개의 값을 가지게 된다.

# 연결리스트 클래스 생성
class LinkedList:
    def __init__(self):
        self.head = None # 머리 노드(첫 번째 노드)를 저장하는 멤버 변수
        
    def add_node(self, data):
        new_node = Node(data) # 새로운 Node 클래스 객체를 생성하고 data 매개변수를 받는다.
        
        '''
        [7, 3노드 주소값] -> [3, 9노드 주소값] -> [9, None]
        '''
        
        if self.head is None: # 머리 노드가 없는 경우 : 연결리스트가 비어있는 경우
            self.head = new_node
            return
        
        current = self.head # current를 머리 노드로 이동시킴
        while current.next is not None: # current.next가 None이 아닌 경우 : current.next가 None일 때 까지 무한루틴
            current = current.next # current.next의 주소값을 current에 대입한다.
            
        current.next = new_node # 새로운 노드의 data를 연결 리스트의 끝(next)과 주소값을 공유
        '''
        [7, 3]
        '''
        
    # 데이터 삽입 메서드. find_data 앞에 데이터가 삽입된다.
    def insert_node(self, find_data, insert_data):
        if self.head is None: # 연결리스트가 비어있는 경우
            return
        
        '''
        7, 3, 9, 1, 6, 
        '''
        
        if self.head.data == find_data: # 머리 노드를 찾는 경우
            self.head = Node(insert_data, self.head)
            return
        
        current = self.head # current에 머리노드값을 대입
        while current.next is not None: # current.next가 None이 아닐 때 무한반복 : 연결리스트를 따라가며 원하는 노드 찾기
            if current.next.data == find_data: # current.next.data 즉, 현재 노드의 다음 노드의 데이터값이 찾고자 하는 데이터값이라면
                new_node = Node(insert_data, current.next) # 삽입할 노드 생성. current의 다음 노드가 되고, 삽입된 후에도 뒷 노드와 이어져야하기 때문에 data에 넣고자 하는 데이터와 next에 원래 current의 다음노드의 주소값을 넣는다.
                current.next = new_node # current.next(다음 노드의 주소값)에 new_node의 데이터 주소를 넣음. 이제 current의 다음 노드는 new_node임
                return
            current = current.next # current에 .next값을 넣음 : 다음 노드값을 받음
        
        # 원하는 노드를 찾지 못한 경우, 연결리스트의 끝에 새로운 노드 추가
        self.add_node(insert_data)
        
        
        
    def print_list(self):
        current = self.head # current를 머리 노드로 이동시킴
        while current is not None: # current가 None이 아닐 때까지 무한반복 : 연결리스트를 따라가며 데이터 출력
            print(current.data, end=' ') # current의 data를 출력
            current = current.next 
            
# 실행 코드
linked_list = LinkedList() # 연결리스트 클래스 객체 선언
linked_list.add_node(7) # 연결리스트 클래스의 add_node 메서드 호출
linked_list.add_node(3)
linked_list.add_node(9)
linked_list.add_node(1)
linked_list.add_node(6)

linked_list.insert_node(9, 99) # 9 다음에 99 삽입

linked_list.print_list()





