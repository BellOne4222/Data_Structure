def dfs(cur_node):
    if cur_node is None: # basecase, none값을 만나면 재귀 종료
        return 0
    dfs(cur_node.left) # 다음 노드에 위임 및 함수 호출,left 먼저 수행 후 right
    dfs(cur_node.right)


# dfs(root) : root만 있으면 root가 가리키는 tree에 속한 모든 노드에 접근할 수 있게 해주는 함수