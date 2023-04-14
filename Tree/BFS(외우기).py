from collections import deque

def bfs(root):
    visited = [] # 방명록 느낌
    if root is None:
        return 0
    q = deque() # 큐를 구현하기 위해서 deque 사용, bfs를 사용하기 위해서 큐를 사용
    q.append(root)
    while q: # 큐는 갈것이라는 예약록 느낌
        cur_node = q.popleft() # cur_node를 통해 접근을 하고, visited에 저장이 되면 q에서 예약한 곳은 popleft처리
        visited.append(cur_node.value) # 방명록 느낌으로 value값을 넣어줌

        if cur_node.left: # leftchild가 있다면
            q.append(cur_node.left) # 큐에 예약하는 느낌으로 갈 예정을 나타내는 정보를 q에 저장
        if cur_node.right: # rightchild가 있다면
            q.append(cur_node.right) # FIFO라는 큐에 성질을 이용해서 예약하는 방식
    return visited

# bfs(root)