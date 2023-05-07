# 1. 문제 이해하기
# 문제 : grid는 "1"(land)와 "0"(water)으로 이루어진 지도를 표현하는 m x n 이차원 배열이다. 이 지도에 표시된 섬들의 총 갯수를 반환해라.
# 섬이란 수평과 수직으로 땅이 연결되어 있고, 주변은 물로 둘러싸여있는 것을 말한다. 또한, grid의 네개의 가장자리는 모두 물로 둘러 싸여 있다고 가정
# 섬은 수평과 수직으로 연결
# input 에서 m == grid.length : row의 개수, n == grid[i].length : column의 개수
# 시간 복잡도 : 1 <= m,n <= 300 이므로 최대 300* 300 = 90000이므로 n^2은 불가

# 2. 접근 방법
# (1) 직관적으로 보기 : 수평과 수직으로만 연결된 1들을 색칠하며 이어가서 섬 개수 파악, 단순화와 극한화 해보기
# - 붙어있는 애들을 색칠하고 count를 1씩 증가하는 방식, 문제를 보고 DFS, BFS 떠올리기, 암시적 그래프 방식(직관적으로 어느 노드끼리 연결이 되어있는지 알 수 있기때문에) 문제
# 2차원 배열에 지도문제 - BFS, DFS문제로 접근

# 3. 코드 설계
# (1) BFS : 첫번째 리스트 부터 bfs 실행 -> 이중 반복문으로 grid[i][j]에 탐방하면서 bfs 실행 -> if grid[i][j] == 1 and not in visited
# -> for i for j if grid[i][j] == 1 and not visited -> bfs 실행, dfs도 똑같은 방식으로 실행


# 4. 코드 구현
# (1) BFS (deque 사용)

from collections import deque

def numIslands(grid):
    number_of_islands = 0
    m = len(grid) # 그리드 길이, row의 개수
    n = len(grid[0]) # 그리드의 0번째 리스트(가로), column의 개수
    visited = [[False] * n for _ in range(m)] # 모든 칸은 False로 설정, n * m -> 전체 칸

    def bfs(x,y): # 메모리 아끼기 위해서 위에 작성
        # 노드의 동서남북을 다 방문 하는 코드
        dx = [-1, 1, 0, 0] # 상 하 좌 우 에 해당하는 위치에 가기 위해서 x와 y의 좌표값에 dx dy 연산을 해주어 상하좌우 정보를 기입
        dy = [0, 0, -1, 1] # 기준 좌표에서 상하좌우에 대한 좌표 증감값을 넣어서 좌표값 return 하는 방식



        visited[x][y] = True # 방문했으면 True로 변경
        queue = deque()
        queue.append((x, y))
        while queue: # 큐가 다 소진될때 까지
            cur_x, cur_y = queue.popleft() 
            
            # 상하좌우의 좌표를 알기 위한 코드
            
            for i in range(4):
                next_x = cur_x + dx[i]
                next_y = cur_y + dy[i]
                # if 방문하면 안되는 좌표: grid의 범위를 넘어서는 것, 섬만 방문해야하는데 물도 방문하는 경우, 방문했던 곳 방문하면 안되는 3가지 경우
                if next_x >=0 and next_x < m and next_y >=0 and next_y < n: # grid 범위를 넘어서는 경우
                    if grid[next_x][next_y] == "1" and not visited[next_x][next_y]: # 섬이 아니라 물을 방문하는 경우 and 방문했던 곳을 방문하는 경우
                        visited[next_x][next_y] = True
                        queue.append((next_x, next_y))
            


    # 이 부분 구현이 중요 윗부분은 dfs, bfs 기본 템플릿이기 때문에

    for i in range(m):
        for j in range(n):
            if grid[i][j] == "1" and not visited[i][j]: # 땅이면서, 방문 안했을 때(True)
                bfs(i, j)
                number_of_islands += 1 # 방문 start를 할때마다 count up
                # dfs()
    return number_of_islands



print(numIslands(grid=[
    ["1","1","0","0","0"], 
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
    ]))

