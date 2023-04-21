# unique paths
# https://leetcode.com/problems/unique-paths/description/

# 1. 문제 이해하기
# 문제 : 이 로봇은 m * n grid 위에 있다. 로봇은 처음에 좌측 상단 모서리(grid[0][0])에 위치해있다. 로봇은 우측 하단 모서리(grid[m-1][n-1])로 이동하려고 한다. 로봇은 한 번에 오른쪽이나 아래쪽으로만 움직일 수 있다.
# 두 정수 m과 n이 주어졌을 때, 로봇이 우측 하단 모서리에 도달할 수 있는 가능한 unique paths의 수를 반환하세요.
# 테스트 케이스는 답이 2 * 10^9 이하가 되도록 생성한다. : int 자료형으로 output 값을 도출해내도 된다, 완전탐색으로 하면 2*10^9 이므로 완전탐색은 사용하지 마라 라는 의미

# 제약 조건: 1 <= m,n <= 100
# m = row , n = column

# 2. 접근 방법
# (1) 완전 탐색(DFS)
# 격자 이므로 그래프 문제이다.
# unique path의 수 : 8C2 = (m-1)+(n-1)C(m-1)or(n-2) = 8! / (2!6!) = 28 
# 갈수 있는 수 : m-1, n-1 이므로 결국 m+n-2Cm-1 or n-1 이다.
# DFS 문제(number of islands)와 차이점 똑같은 격자이지만, DFS문제는 갔던곳은 visited에 저장하고 다시 가지는 않았고 unique path 문제는 갔던 격자를 또 갈 수 있기 때문에 차이점이 있다.

# 3. 코드 설계
# (1) 완전탐색
# 출발 지점 부터 도착 지점 까지 경로 계산
def dfs(r, c):
    if r == 2 and c == 6: # basecase : r=2, c=6 일때 unique path는 1이므로(도착점에 도착할때)
        return 1
    unique_paths = 0
    if r+1 < 3: # 아래로 3칸 이상 내려가면 범위 밖으로 벗어나므로
        unique_paths += dfs(r+1, c) 
    if c+1 < 7: # 오른쪽으로 7칸 이상 가면 범위 밖으로 벗어나므로
        unique_paths += dfs(r, c+1)
    unique_paths += dfs(r+1, c) # 아래
    unique_paths += dfs(r, c+1) # 오른쪽
    return unique_paths

# 도착지점에서 출발 지점까지 경로 계산
def dfs(r, c):
    if r == 0 and c == 0: # basecase : 출발점에 도착할때)
        return 1
    unique_paths = 0
    if r-1 >= 0: # 맨 윗줄을 넘어가면 안되므로
        unique_paths += dfs(r-1, c) 
    if c-1 >= 0: # 맨 왼쪽 줄을 넘어가면 안되므로
        unique_paths += dfs(r, c-1)
    return unique_paths

# (2) top-down 방식 시간 복잡도 : O(m * n) = O(10^4) : 시간 복잡도가 엄청 줄었고 사용가능
# 딕셔너리 사용
memo = {}
def dfs(r,c):
    if r == 0 and c == 0: # basecase 
        memo[(r,c)] = 1
        return memo[(r,c)]
    
    unique_paths = 0
    
    if (r,c) not in memo:
        if r-1 >= 0: # 맨 윗줄을 넘어가면 안되므로
            unique_paths += dfs(r-1, c) 
        if c-1 >= 0: # 맨 왼쪽 줄을 넘어가면 안되므로
            unique_paths += dfs(r, c-1)
        memo[(r,c)] = unique_paths 
    return memo[(r,c)]

# 이중 리스트 사용
def uniquePaths(m,n):
    memo = [[-1]*n for _ in range(m)] # -1로 초기화
    def dfs(r,c):
        if r == 0 and c == 0: # basecase : 출발점 도착
            memo[r][c] = 1
            return memo[r][c]
        unique_paths = 0
        if memo[r][c] == -1: #격자를 할때는 범위 설정 중요
            if r-1 >= 0: # 맨 윗줄을 넘어가면 안되므로(범위)
                unique_paths += dfs(r-1, c) # 위쪽으로 이동
            if c-1 >= 0: # 맨 왼쪽 줄을 넘어가면 안되므로(범위)
                unique_paths += dfs(r, c-1) # 왼쪽으로 이동
            memo[r][c] = unique_paths 
        return memo[r][c]
    return dfs(m-1, n-1) # 도착점 좌표가 m-1, n-1 이므로
uniquePaths(3,7)

# (3) bottom-up 방식 dp table 채워가는 방식
def uniquePaths(m,n):
    memo = [[-1]*n for _ in range(m)] # dp table
    for r in range(m): # 맨 왼쪽 세로 한줄 0으로 초기화
        memo[r][0] = 1
    for c in range(n): # 맨 위쪽 가로 한줄 0으로 초기화
        memo[0][c] = 1
    for r in range(1, m): # 초기화를 해줬으므로 1부터 시작
        for c in range(1, n):
            memo[r][c] = memo[r-1][c] + memo[r][c-1] # 점화식
    return memo[m-1][n-1]
uniquePaths(3, 7)

# ccccccccc
#r
#r
#r
#r


