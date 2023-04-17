# 깊이 우선 탐색(DFS), 재귀 함수 사용
# DFS 템플릿 외우기

graph = { # 인접 리스트 방식으로 그래프 구현
    'A': ['B', 'D', 'E'], 
    'B': ['A', 'C', 'D'],
    'C': ['B'],
    'D': ['A', 'B'],
    'E': ['A'],
}

# def dfs(graph, cur_v, visited=[]):
#     visited.append(cur_v)
#     for v in graph[cur_v]:
#         if v not in visited:
#             visited = dfs(graph, v, visited)
#     return visited

# print(dfs(graph, 'A'))

# 위 코드를 단순화한 코드
graph = { ... }
visited = [] # 언제는 visited에 접근할 수있도록 전역변수 느낌으로 선언
def dfs(cur_v): # 시작 cur_v는 A
    visited.append(cur_v)
    for v in graph[cur_v]: # A와 연결된 모든 노드 방문
        if v not in visited: 
            dfs(v) #dfs 함수를 재귀적으로 사용하여 반복문으로 방문하는 구조, 함수를 다시 호출 했으므로 그다음인 B가 알아서 근처 노드를 탐방
            # 재귀 함수 호출을 해서 방문을 하는 것을 위임하는 구조, cur_v도 다음 노드로 바뀌면서 실행
            # dfs를 안했으면 그 안한 노드에서 다른 노드를 방문하는 구조

print(dfs('A'))


# 방문을 안한 노드에 갔을때, 그 노드에서 함수를 또 호출해 다음 노드로 이동
# A - B - C - D - E