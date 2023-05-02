'''
연결 리스트(Linked List)
    저장된 각 데이터가 (데이터)+(다음 데이터의 포인터==주소값)로 이루어진 것으로 한 방향으로만 탐색 가능한 구조
    연결 리스트의 각 요소는 node라고 부른다.
'''

class Node:
    def __init__(self, data, next=None):
        self.data = data # 노드에 저장될 데이터
        self.next = next # 다음 노드를 가리키는 포인터
        
class LinkedList: # 연결 리스트를 총괄하는 클래스
    def __init__(self):
        self.head = None # 머리 노드를 저장하는 멤버 변수

    # 연결 리스트에 노드(요소)를 추가하는 메서드
    def add_node(self, data):
        new_node = Node(data) # 새로운 노드 생성
        
        if self.head is None: # 연결 리스트가 비어있는 경우
            self.head = new_node # self.head와 new_node는 같은 주소값을 공유하게 된다.(초회 한정)
            return
        
        current = self.head # current와 self.head는 같은 주소값을 공유하게 된다.
        while current.next is not None: # 연결 리스트의 끝까지 이동
            current = current.next
            
        current.next = new_node # 새로운 노드를 연결 리스트의 끝에 추가
        # current 노드의 .next에 새로 추가된 데이터의 주소값을 공유한다. 
        
    def insert_node(self, find_data, insert_data):
        if self.head is None: # 연결 리스트가 비어 있는 경우
            return
        
        if self.head.data == find_data: # 머리 노드를 찾은 경우
            self.head = Node(insert_data, self.head)
            return
        
        current = self.head
        while current.next is not None: # 연결 리스트를 따라가면서 원하는 노드 찾기
            if current.next.data == find_data:
                new_node = Node(insert_data, current.next)
                current.next = new_node
                return
            current = current.next
        
        # 원하는 노드를 찾지 못한 경우, 연결 리스트의 끝에 새로운 노드 추가
        self.add_node(insert_data)
        
    def delete_node(self, del_data):
        if self.head is None: # 연결 리스트가 비어있는 경우
            return
        
        if self.head.data == del_data: # 머리 노드를 삭제하는 경우
            self.head = self.head.next
            return
        
        current = self.head
        while current.next is not None: # 연결 리스트를 따라가면서 원하는 노드 찾기
            if current.next.data == del_data:
                current.next = current.next.next
                return
            current = current.next
        
        
    def print_list(self):
        current = self.head
        while current is not None: # 연결 리스트를 따라가며 데이터 출력
            print(current.data, end=' ')
            current = current.next

# 실행 코드
linked_list = LinkedList()
linked_list.add_node(7)
linked_list.add_node(3)
linked_list.add_node(9)
linked_list.add_node(1)
linked_list.add_node(6)

#linked_list.insert_node(9, 99) # 9 다음에 99 삽입

#linked_list.delete_node(1)

linked_list.print_list()