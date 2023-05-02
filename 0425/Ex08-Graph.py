'''
파일명 : Ex08-Graph.py

그래프(Graph)
  노드(vertice)와 간선(정점/edge/arcs)로 이루어진 자료구조
  
 A
/ \
B  C
\ /
 D
 |
 E
 
'''
class Graph:
  '''
  self.vertices = ['A', 'B', 'C', 'D', 'E']
  
  self.adj_list = {
  'A' : [],
  'B' : [],
  'C' : [],
  'D' : [],
  'E' : []
  }
  '''
  def __init__(self, vertices):
    self.vertices = vertices
    self.adj_list = {} # 빈 딕셔너리
    for vertex in vertices:
      self.adj_list[vertex] = []
  
  '''
  graph.add_edge('A', 'B')
  graph.add_edge('A', 'C')
  graph.add_edge('B', 'D')
  graph.add_edge('C', 'E')
  '''
  
  def add_edge(self, u, v):
    self.adj_list[u].append(v)
    self.adj_list[v].append(u)
    
    '''
      self.adj_list = {
      'A' : [B, C],
      'B' : [A, D],
      'C' : [A, E],
      'D' : [B],
      'E' : [E]
      }
    '''
    
  def remove_edge(self, u, v):
    self.adj_list[u].remove(v)
    self.adj_list[v].remove(u)
  
  '''
  'A' : [B, C],
  'B' : [A, D],
  'C' : [A, E],
  'D' : [B],
  'E' : [E]
  '''
  
  def print_graph(self):
    for vertex in self.vertices:
      print(vertex, end=' -> ')
      print(' -> '.join([str(node) for node in self.adj_list[vertex]]))

# 실행 코드
vertices = ['A', 'B', 'C', 'D', 'E']

print(' -> '.join(vertices)) # .join() : 리스트 요소 출력 시 쉼표 대신 앞에 작성한 문자열을 대신 출력함

graph = Graph(vertices)
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('B', 'D')
graph.add_edge('C', 'E')

graph.print_graph()

'''
A -> B -> C
B -> A -> D
C -> A -> E
D -> B
E -> C
'''
