# 전위 순회 : 자식들에게 가기전에 먼저 자신에게 방문하는 방식

def preorder(cur_node):
    if cur_node is None:
        return
    
    print(cur_node.value) # 자기 자신 먼저 방문
    preorder(cur_node.left) # leftchild 방문
    preorder(cur_node.right) # rightchild 방문

# preorder(root)
# visted : A - B - C