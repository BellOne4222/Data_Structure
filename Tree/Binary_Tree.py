# 노드
class Node: 
    def __init__(self):
        self.value = 0
        self.left_child = None
        self.right_child = None

class BinaryTree:
    def __init__(self):
        self.root = None # 링크드리스트의 head역할, 트리는 root가 있어야한다.

bt = BinaryTree()
bt.root = Node(value = 1)
bt.root.left = Node(value = 2)
bt.root.right = Node(value = 3)
bt.root.left.left = Node(value = 4)
bt.root.left.right = Node(value = 5)
bt.root.right.right = Node(value = 6)

