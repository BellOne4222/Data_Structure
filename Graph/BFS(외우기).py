# 너비 우선 탐색(BFS), 큐(FIFO) 사용

graph = { # 인접 리스트 방식으로 그래프 구현
    'A': ['B', 'D', 'E'], 
    'B': ['A', 'C', 'D'],
    'C': ['B'],
    'D': ['A', 'B'],
    'E': ['A'],
}

# BFS 외워야함
from collections import deque

def bfs(graph, start_v):
    visited = [start_v] # start_v에 방문
    queue = deque(start_v) # deque에 start_v를 넣음 : while문을 돌리기 위한 사전 세팅
    while queue: # 큐가 있는지 없는지 확인, 한 사이클 돌면 FIFO 이므로 A -> B로 이동 : B에 예약을 했으므로
        cur_v = queue.popleft()
        for v in graph[cur_v]: # dequeue한 cur_v로 가까운 모든 노드부터 방문
            if v not in visited: # 방문을 하지 않은 노드이면 visited에 추가함(방문을 한다.)
                visited.append(v)
                queue.append(v) # 그 노드를 방문 예약을 건다.(start_v로 온게 아니라 인접 노드 방문으로 온것이므로)
    return visited # 큐에 값이 없으면(다 방문을 했으면) 종료, 가까운 곳부터 방문

print(bfs(graph, 'A'))

# 시작 노드 기준 근처 노드를 다 방문을 하고 예약을 걸어놓은 노드를 다 갔을때 큐에 값이 없으면 다시 가까운 곳에 방문
# A - B - D - E - C