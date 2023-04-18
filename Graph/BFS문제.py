# BFS(너비 우선 탐색 문제)
# 미로 찾기/ 최단거리 구하는 문제는 BFS 자주사용
# https://leetcode.com/problems/shortest-path-in-binary-matrix/description/

# 1. 문제 이해하기

# 문제 : n*n binary matrix인 grid가 주어졌을 때, 출발지에서 목적지 까지 도착하는 가장 빠른 경로의 길이를 반환하라. 만약 경로가 없다면 -1을 반환
# 출발지 : top-left cell, 목적지 : bottom- right cell
# 값이 0 인 cell 만 지나갈 수 있다, cell끼리는 8가지 방향으로 연결되어있다.(edge와 corner 방향으로 총 8가지이다.)
# 연결된 cell을 통해서만 지나갈 수 있다.

# 제약조건 : n == grid.length(리스트 길이, row, 세로) == grid[i].length(column, 가로)
# 시간 복잡도 : 100까지 이므로 n^2까지 괜찮으므로 bfs 사용

# 2. 접근 방법
# BFS 사용
# BFS의 시간 복잡도 : cell의 개수 , v 만큼 방문 하므로, 시간복잡도는 O(v) = O(n^2)
# 자료구조와 알고리즘 사용 : graph(암시적 그래프 표현)

# 3. 코드 설계
# 최단 거리 구하는 문제 -> BFS 사용 -> queue 사용

# 4. 코드 구현

from collections import deque

def shortestPathBinaryMatrix(grid):
    shortest_path_len = -1 # 도착할 수 없으면 -1이므로 그냥 -1로 초기화
    row = len(grid)
    col = len(grid[0])
    
    if grid[0][0] != 0 or grid[row-1, col-1] != 0:
        return -1 # 시작가 없으면 -1
    visited = [[False] * col for _ in range(row)] # False로 아직 방문하지 않은 곳들을 채워줌

    delta = [[(1,0), (-1,0), (0,1), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1),]] # 상하좌우, 대각선 좌표들 저장(8가지 방향)
    queue = deque() # 시작점에서 큐선언
    queue.append((0, 0, 1))
    visited[0][0] = True
    
    while queue:
        cur_r, cur_c, cur_len = queue.popleft()

        # 목적지에 도착했을 때 그때의 cur_len를 shortest_path_len에 저장하면 된다. (도착지 좌표: col -1, row -1)
        if cur_r == row - 1 and cur_c == col -1: #목적지에 도착했을 때  
            shortest_path_len = cur_len
            break # 목적지 도착하고 break


        # 연결되어있는 노드들 확인하기
        for dr, dc in delta: # 8가지 방향
            next_r = cur_r + dr
            next_c = cur_c + dc
            if next_r >=0 and next_r < row and next_c >=0 and next_c < col:
                if grid[next_r][next_c] == 0 and visited[next_r][next_c]:
                    queue.append((next_r, next_c, cur_len + 1)) # 다 방문하고 한칸씩 옮기면서 늘어나므로 cur_len에 +1, cur_len = 도착 경로
                    visited[next_r][next_c] = True # 방문했으면 그 좌표는 True 처리

    return shortest_path_len
