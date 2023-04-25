'''
파이썬은 데이터마다 주소값(메모리의 주소)을 전부 가지고 있다.

mutable - 메모리에서 값을 변경할 수 있는 객체
    리스트(list), 세트(set), 딕셔너리(dict), 클래스(class) 등

immutable - 메모리에서 값을 변경할 수 없는 객체
    정수(int), 실수(float), 문자열(str), 튜플(tuple)
    
'''

me = 10
print(id(me))
me += 1
print(id(me))
you = 10
print(id(you))

list1 = [1, 2, 3]
print(id(list1))
list1.append(4)
print(id(list1))