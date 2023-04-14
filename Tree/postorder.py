# 후위 순회

def postorder(cur_node):
    if cur_node is None:
        return
    
    
    postorder(cur_node.left) # leftchild 먼저 방문
    postorder(cur_node.right) # rightchild 방문
    print(cur_node.value) # 자기 자신 방문
    
# postorder(root)
# visited : B - C - A