'''
파일명 : Ex06-BinaryTree.py

트리 자료구조
  단 하나의 루트 노드가 있고, 루트 노드에서 하위 노드들이 연결된
  비선형 계층구조이다.

이진트리(Binary Tree)
  모든 노드가 최대 2개의 자식 노드를 가질 수 있는 구조를 말한다.
  왼쪽 서브 트리의 값은 루트의 값보다 작고, 오른쪽 서브트리의 값은 루트보다 
  큰 값을 가지도록 구성한다.
'''
class TreeNode:
    def __init__(self, value): # 생성자
        self.value = value # 노드의 값
        self.left = None # 왼쪽 서브트리 노드
        self.right = None # 오른쪽 서브트리 노드

# 이진 트리를 생성하고 순회, 탐색, 삽입, 삭제를 하는 클래스
class BinaryTree: # 인수로 5를 받음
    def __init__(self, root):
        self.root = TreeNode(root) # BinaryTree객체.root는 현재 TreeNode의 객체이고 value값이 5인 상황. 루트 노드라고 하고, 최상단의 노드이다.
        
    # 삽입

    def insert(self, value):
        if not self.root: # BinaryTree객체의 root가 비어있다면
            self.root = TreeNode(value) # 인수로 받은 value값을 TreeNode클래스에 넣고 BinaryTree객체.root를 TreeNode 객체로 선언한다. 
        else: # BinaryTree객체에 root가 존재한다면
            self._insert(value, self.root) # _insert 메서드를 value와 self.root를 매개변수로 하여 실행한다. 밑의 실행코드를 예시로 들어 value는 3, self.root는 5

    def _insert(self, value, current_node): # 매개변수로 value와 current_node
        if value < current_node.value: # value(3)이 current_node.value(5)보다 작다면 (위의 예시로는 참인 상황이니까 실행된다.)
            if not current_node.left: # current_node.left가 비어있다면
                current_node.left = TreeNode(value) # TreeNode(3)을 current_node_left에 넣는다.
            else: # current_node.left가 비어있지 않다면
                self._insert(value, current_node.left) # _insert 메서드를 value와 current_node.left를 매개변수로 하여 실행한다. 이런식으로 함수를 반복하여 왼쪽을 채우는 느낌인것 같다.
        elif value > current_node.value: # 이번엔 insert인수를 7로 받았을때로 가정한다. value(7)가 current_node.value(5)보다 크다면
            if not current_node.right: # current_node.right가 비어있다면
                current_node.right = TreeNode(value) # TreeNode(7)을 current_node.right에 넣어라.
            else: # currend_node.right가 비어있지 않다면
                self._insert(value, current_node.right) # _insert 메서드를 value, current_node.right를 매개변수로 하여 실행한다. 이런식으로 함수를 반복하여 오른쪽을 채우는 느낌인것 같다.
        else: # value와 current_node가 같다면
            print("이미 존재하는 값입니다.") # 이미 값이 존재한다고 출력하기
        
    # traversal : 순회
    # 트리 순회 정의 : Tree의 Node들을 지정된 순서대로 “방문”하는 것
    
    # preorder traversal(전위 순회)은 루트 노드에서부터 다음과 같은 방법으로 노드들을 방문한다.

    # 노드를 방문한다.
    # 왼쪽 서브트리를 전위 순회한다.
    # 오른쪽 서브트리를 전위 순회한다.
    
    def preorder_traversal(self, start, traversal): # start에 bt.root인 5가 들어가고, traversal에 ""이 들어간다.
        if start: # start값이 존재할 때
            traversal = traversal + (str(start.value) + ' ') # traversal에 start.value, 즉 5를 문자열로 넣고 공백을 결합해서 누적한다.
            traversal = self.preorder_traversal(start.left, traversal)
            '''
            bt객체를 인수 start.left 즉 bt.root.left와 traversal을 사용하여 preorder_traversal 메서드를 실행하고, traversal에 넣는다.
            메서드가 계속 반복되며 start값이 존재하지 않을 때 까지, 즉 bt의 왼쪽의 값을 전부 불러올 때 까지 스택에 쌓이고, 스택에 쌓인 역순으로 메서드를 실행한다.
            '''
            traversal = self.preorder_traversal(start.right, traversal) # 위와 마찬가지로 right값을 전부 불러올 때 까지 반복한다.
        return traversal # traversal에 누적된 데이터를 반환한다.

    # inorder traversal (중위순회)

    # 왼쪽 서브트리를 중위순회한다.
    # 노드를 방문한다.
    # 오른쪽 서브트리를 중위순회한다.
    
    def inorder_traversal(self, start, traversal):
        if start:
            traversal = self.inorder_traversal(start.left, traversal)
            traversal += (str(start.value) + ' ')
            traversal = self.inorder_traversal(start.right, traversal)
        return traversal

    # postorder traversal (후위순회)

    # 왼쪽 서브트리를 후위순회한다.  
    # 오른쪽 서브트리를 후위 순회한다.
    # 노드를 방문한다.

    def postorder_traversal(self, start, traversal):
        if start:
            traversal = self.postorder_traversal(start.left, traversal)
            traversal = self.postorder_traversal(start.right, traversal)
            traversal += (str(start.value) + ' ')
        return traversal

    # 탐색 : 검색한 데이터가 트리 안에 존재하는지의 여부를 탐색한다. 존재한다면 True, 아니라면 False를 반환한다.

    def search(self, value):
        return self._search(value, self.root) # bt객체에 인수로 받은 value와 self.root를 인수로 하여 _search 메서드의 결과를 반환. 밑에 코드를 예시로 들면 value는 4, self.root는 5다.

    def _search(self, value, current_node): # 매개변수로 value와 current_node를 사용한다. value에는 4, current_node에는 5가 들어간다.
        if not current_node: # current_node가 없다면
            return False # False를 반환
        elif current_node.value == value: # current_node의 value값, 즉 self.root가 인수로 받은 value값과 같다면
            return True # True를 반환
        elif value < current_node.value: # 인수로 받은 value값이 current_node.value 즉 self.root보다 작다면
            return self._search(value, current_node.left) # _search 메서드를 value, current_node.left를 인수로 하여 실행한 결과를 반환한다. 왼쪽 트리의 값을 탐색하는 과정인것 같다.
        else: # 인수로 받은 value값이 current_node.value 즉 self.root보다 크다면
            return self._search(value, current_node.right) # _search 메서드를 value, current_node.right를 인수로 하여 실행한 결과를 반환한다. 오른쪽 트리의 값을 탐색하는 과정인것 같다.

    # 삭제

    def delete(self, value):
        if not self.root: # 트리에 아무것도 없다면
            return # 끝낸다.
        else: # 트리에 뭐라도 있다면
            self.root = self._delete(value, self.root) 
            '''
            _delete메서드를 인수로 받은 value와 bt객체의 root값을 인수로 하여 실행하고 bt객체의 root에 넣는다.
            밑에 코드로 보자면 value에는 3, self.root에는 5가 들어간다.
            '''
    def _delete(self, value, current_node): # 매개변수로 value와 current_node를 사용한다.
        if not current_node: # current_node가 없다면, 즉 트리에 아무것도 없다면
            return current_node # current_node 반환. 아무것도 없으니 반환할게 없다.

        elif value < current_node.value: # value가 current_node의 value값보다 작다면, 즉 지우고자 하는 값이 bt객체의 root보다 작다면
            current_node.left = self._delete(value, current_node.left) # bt객체의 _delete메서드를 value, current_node.left를 인수로 사용하여 실행한 값을 current_node.left에 넣는다.

        elif value > current_node.value:
            current_node.right = self._delete(value, current_node.right)

        else: # value값과 current_node.value가 같다면, 즉 지우고자 하는 값과 현재 탐색한 값이 같을 때
            if not current_node.left and not current_node.right: # 현재 노드의 왼쪽과 오른쪽 값이 둘다 없을 때
                current_node = None # currnet_node에 None을 넣는다. 삭제하는 메서드이기 때문에 값을 비우는 것이다.

            elif not current_node.left: # current_node.left가 없다면
                current_node = current_node.right # current_node.right을 current_node에 넣는다.

            elif not current_node.right: # current_node.right가 없다면
                current_node = current_node.left # current_node.left를 current_node에 넣는다.

            else: # current_node.left와 current_node.right가 존재할 때
                min_node = self._find_min(current_node.right) # bt객체의 _find_min메서드를 current_node.right를 인수로 사용하여 실행한 결과값을 min_node에 넣는다.
                current_node.value = min_node.value # min_node.value의 값을 current_node.value에 넣는다. min_node.value는 밑의 코드로 보자면 2가 되겠다.
                current_node.right = self._delete(min_node.value, current_node.right)
                '''
                bt객체의 _delete메서드를 min_node.value와 current_node.right을 인수로 하여 실행한 결과값을 current_node.right에 넣는다.
                여기선 min_node.value가 2이고
                '''

        return current_node # current_node를 반환한다.

    def _find_min(self, current_node): # current_node는 4이다. 위에서 쭉쭉 타고 내려와서 여기까지 왔다.
        while current_node.left: # current_node.left값이 존재할 때 무한루프
            current_node = current_node.left # current_node.left값을 current_node에 넣는다.
        return current_node # 위의 무한루프가 끝난 후 current_node를 반환한다. 맨 왼쪽을 탐색하는 과정인 것 같다. 맨 왼쪽의 값을 위의 min_node에 넣게 되는 것이다.

# 아 딜리트 모르겠다. 주석 써놓긴 했는데 갑자기 실행 구조가 머리속에서 꼬이기 시작했다. 중간부터 이상한거같아.

# 실행코드
# 이진 트리 객체를 생성합니다. 루트 노드의 값은 5입니다.
bt = BinaryTree(5)

# 값을 삽입합니다.
bt.insert(3)
bt.insert(7)
bt.insert(2)
bt.insert(4)
bt.insert(6)
bt.insert(8)

# 이진 트리를 전위 순회한 결과를 출력합니다.
print("전위 순회: ", bt.preorder_traversal(bt.root, ""))

# 이진 트리를 중위 순회한 결과를 출력합니다.
print("중위 순회: ", bt.inorder_traversal(bt.root, ""))

# 이진 트리를 후위 순회한 결과를 출력합니다.
print("후위 순회: ", bt.postorder_traversal(bt.root, ""))

# 값을 검색합니다.
print("값 4가 트리에 존재하는가? ", bt.search(4))
print("값 9가 트리에 존재하는가? ", bt.search(9))

# 값을 삭제합니다.
bt.delete(3)
print("값 3을 삭제한 후 중위 순회: ", bt.inorder_traversal(bt.root, ""))

# 값을 삭제합니다.
bt.delete(7)
print("값 7을 삭제한 후 중위 순회: ", bt.inorder_traversal(bt.root, ""))

# 값을 삭제합니다.
bt.delete(5)
print("값 5을 삭제한 후 중위 순회: ", bt.inorder_traversal(bt.root, ""))


