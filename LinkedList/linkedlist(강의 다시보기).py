class Node:
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next

first = Node(1)
second = Node(2)
third = Node(3)
first.next = second
second.next = third
first.value = 6 

class LinkedList(object):
    def __init__(self):
        self.head = None # head가 none값을 가리킴
    def append(self, value): # 시간 복잡도 : O(n)
        new_node = Node(value)
        if self.head is None: # head가 옮겨가며 뒤에 new_node를 가리키면 안되기 때문에, 마지막 노드는 none값을 가져야함
            self.head = new_node
        # 맨 뒤의 node가 new_node를 가리켜야 한다.
        else:
            current = self.head 
            while(current.next): # 타고타고 마지막 노드를 가야하기 때문에 current.next가 none이 될때까지 실행, current_next를 new_node 전까지 갈 수 있도록 구현 
                current = current.next
            current.next = new_node
        self.head = new_node # head가 new_node를 가리키게함
    def get(self, idx): # 특정 인덱스에 있는 값을 가져오는 메서드, 시간 복잡도 : O(n)
        # head에 접근(linkedlist에 접근)
        current = self.head
        # 원하는 index로 이동
        for _ in range(idx): # 인덱스 만큼 반복(원하는 인덱스까지 가기 위해서)
            current = current.next
        # value 반환
        return current.value
    def insert(self, idx, value): # 중간 인덱스에 노드를 추가하는 메소드
        new_node = Node(value)
        if idx == 0:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            current = self.head
            for _ in range(idx):
                current = current.next
            new_node.next = current
            current.prev.next = new_node
            new_node.prev = current.prev
            current.prev = new_node
    def remove(self, idx):
        if idx == 0:
            self.head.prev = None
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(idx):
                current = current.next
            if current.next is None:
                current.prev.next = None
            else:
                current.prev.next = current.next
                current.next.prev = current.prev
    def insert_back(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else: # 시간 복잡도 : O(1)
            self.tail.next = new_node
            self.tail = self.tail.next


ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.get(0)
ll.get(1)
ll.get(3)
ll.insert(idx = 2, value= 9)
ll.remove(3)
