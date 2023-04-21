# Min Cost Climbing stairs
# https://leetcode.com/problems/unique-paths/description/

# 1. 문제 이해하기
# 문제 : 계단을 올라가고 있다. 한 번 올라갈 때 마다 1 step 또는 2steps 올라갈 수 있다. 문제에서 정수형 배열 cost가 주어지는데, cost[i]는 i번째 계단을 지불해야 하는 비용이다.
# 처음 시작은 index 0 또는 index 1 중 한 곳에서 시작할 수 있다.
# 이 계단의 꼭대기에 도착하기 위해 지불해야하는 비용의 최소값을 반환하라.

# 제약 조건 : 2 <= cost.length <= 1000 : 시간 복잡도는 O(N^2)이하 
# 0 <= cost.[i] <= 999 : cost 가 0이면 그 자리를 밟는 거기 때문에 고려해야한다.

# 2. 접근 방법
# (1) 완전 탐색 (재귀를 이용)'
cost = [10, 15, 20, 17, 1]
def dfs(n): # 시간 복잡도 : O(2^n) -> 2^1000이므로 2^8이 넘어서 불가
    if n == 0 and n == 1: # basecase
        return 0 
    return min(dfs(n-1)+cost[n-1], dfs(n-2)+cost[n-2]) # n-1층에서 올라오는거 vs n-2층에서 올라오는거 비교, cost는 밟고 올라올 칸의 값

# 중복되는 계산이 있으므로 memoization을 사용하여 해결
# (2) Top-down 방식 : 중복되는 계산 값을 메모리에 저장(memoization) 
# 시간 복잡도 : O(n) : 2n 번 호출 된다.
cost = [10, 15, 20, 17, 1]
memo = {}
def dp(n): # 시간 복잡도 : O(2^n) -> 2^1000이므로 2^8이 넘어서 불가
    if n == 0 and n == 1: # basecase
        return 0 
    if n not in memo: # memo에 값이 없는 것은 딱 한번 계산을 해준다.
        memo[n] = min(dp(n-1)+cost[n-1], dp(n-2)+cost[n-2]) # 계산값을 memo에 저장 # 1+ dp(4), 17 + dp(3) , 각 계산값 중 최소값 반환(각 2n 번), 1+ dp(4) 부터 수행하고 쭉쭉 계산하고 계산값을 메모리에 저장 후 밑에 dp(3) 계산은 메모리에서 가져와서 실행
    return memo[n]

# (3) Bottom-up : memo[0] = 0, memo[1] = 0 => 문제에서 index 0, 1에서 시작 가능하다고 했으므로 basecase 설정 가능
cost = [10, 15, 20, 17, 1]
# memo = {0 : 0, 1: 0} or
def dp(n):
    # memo = {0 : 0, 1: 0} or
    memo = [-1]*n # -1로 배열 초기화 (-1, -1, -1, -1, -1, -1)
    memo[0] = 0
    memo[1] = 0
    # bottom-up은 반복문 사용
    for i in range(2, n+1): # 2~ n까지
        memo[i] = min(memo[i-1]+cost[i-1], memo[i-2]+cost[i-2])
    return memo[n]
