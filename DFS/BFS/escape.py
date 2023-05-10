# 미로 탈출
# p.152
# BFS, 시작 지점에서 가까운 노드 부터 차례대로 그래프의 모든 노드를 탐색
# (1,1) 지점에서 부터 BFS를 수행하여 모든 노드의 값을 거리 정보로 넣는다.
# 특정 노드를 방문 하면 그 이전 노드의 거리에 1을 더한 값을 리스트에 넣는 방식

from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 이동할 네 방향 정의(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x,y):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x,y))
    # 큐가 빌때까지 반복
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 미로 찾기 공간을 벗어나면 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 벽(괴물) 칸 인경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 ㅂ아문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n-1][m-1]

print(bfs(0,0))

