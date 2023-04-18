# DFS 깊이우선 탐색 문제
# https://leetcode.com/problems/keys-and-rooms/

# 1. 문제 이해하기

# 문제 : 0번방부터 n-1 번방까지(배열을 사용하라는 의미,인덱스를 사용해라) 총 n개의 방이 있다. 0번 방을 제외한 모든 방을 잠겨있다. 우리의 목표는 모든 방에 visit하는 것이다. 하지만 잠겨져 있는 방은 key가 없으면 visit할 수 없다. 각 방에 방문할 때, 별개의 열쇠뭉치를 찾을 수도있다.
# 각각의 열쇠에는 number가 쓰여져 있고, 해당 번호에 해당하는 방을 잠금 해제할 수 있다. 열쇠뭉치는 모두 가져갈 수 있고, 언제든 방문을 열기 위해 사용할 수 있다.
# 문제에서 rooms 배열이 주어지고, rooms[i]는 해당 방에서 얻을 수 있는 열쇠뭉치 목록을 표현한다. 모든 방을 visit할 수 있으면 True, 그렇지 않으면 False를 반환하라.
# 0번방은 무조건 오픈됨

# 제약조건 : n == rooms.length : 방의 개수, n : inputsize
# 2 <= n <= 1000 이므로 n^2으로도 시간 복잡도 사용 가능 

# 2. 접근 방법
# 그래프적으로 서로 연결되어있는 것끼리 구성되어있는 그래프로 추상화
# DFS 사용 -> 시간 복잡도 : O(V + E) Vertex + Edge -> 완전탐색이므로 모든 vertex와 edge를 다 가기 때문에
# -> v = 방의 개수, e = 열쇠의 개수 총합 => 1000, 3000 -> O(4000) -> BFS든, DFS든 둘 다 사용가능

# 3. 코드 설계 
# DFS 템플릿 기본 사용

# 4. 코드 구현(DFS)

def canVisitAllRooms(rooms):
    visited = [False] * len(rooms) # False로 채우기

    # v에 연결되어잇는 모든 vertex 방문할거라는 코드
    def dfs(cur_v):
        visited[cur_v] = True # 방문하면 True로 저장
        for next_v in rooms[cur_v]:
            if visited[next_v] == False:  #next_v 가 방문 했었는지 확인, 인덱스로 접근하기 때문에 시간 복잡도는 O(1)
                dfs(next_v)
                  

    dfs(0) # 시작 위치
    
    if visited == len(rooms):
        return True
    else:
        return False
    # return visited # 0 - 1 - 2- 4 - 3

rooms = [[1,3], [2, 4], [0], [4], [], [3,4]]
print(canVisitAllRooms(rooms))

# 4. 코드 구현(BFS)
# from collections import deque

# def canVisitAllRooms(rooms):
#     visited = [False] * len(rooms) # False로 채우기

#     def bfs(v):
#         queue = deque()
#         queue.append(v)
#         visited[v] = True
#         while queue:
#             cur_v = queue.popleft() # 방문할 현재v를 큐에서 뽑고
#             for next_v in rooms[cur_v]: # 현재 v의 인접 v들에서
#                 if visited[next_v] == False: # 다음 v가 False이면(방문하지 않았으면)
#                     queue.append(next_v) # 예약 목록에 넣고
#                     visited[next_v] = True # 방문한 v는 True 처리해서 visited에 저장

#     bfs(0)

#     return all(visited)

# rooms = [[1,3], [2, 4], [0], [4], [], [3,4]]
# print(canVisitAllRooms(rooms))
