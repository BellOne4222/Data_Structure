# 중위 순회 : 중간에 자기 자신을 방문해야한다.

def inorder(cur_node):
    if cur_node is None:
        return
    
    
    inorder(cur_node.left) # leftchild 먼저 방문
    print(cur_node.value) # 자기 자신 방문
    inorder(cur_node.right) # rightchild 방문

# inorder(root)
# visited : B - A - C