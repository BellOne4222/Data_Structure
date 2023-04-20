# https://leetcode.com/problems/climbing-stairs/
# climing upstairs
# 문제 : 계단을 올라가고있다. 이 계단의 꼭대기에 도착하려면 n개의 steps 만큼 올라가야 한다. 한 번 올라갈 때 마다 1 step 또는 2 steps 올라갈 수 있다. 꼭대기에 도달하는 방법의 개수는 총 몇 가지 일까?
# 제약사항 : 1 <= n <= 45

# 1. 문제 이해하기
# n = 5 라고 할때, n = 3 + n = 4 같은 하위 문제로 나눠서 해결

# 완전 탐색 방법
def cs(n):
    if n == 1: # base case : 탈출 조건
        return 1
    if n == 2:
        return 2
    
    return cs(n-1) + cs(n-2) # 하위 문제로 나누기

# 하위 문제로 나누어서 구할때, 중복 되는 계산이 있으므로, DP 사용
# Top-down 방식 사용(재귀 이용), memoization
memo = {}
def cs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n not in memo: # memo에 값이 없으면 계산해서 memo에 저장
        memo[n] =  cs(n-1) + cs(n-2) 
    return memo[n] # 계산 결과를 memo에 저장

# Bottom-up 방식(반복문 사용), tabulation
memo = {1:1, 2:2} # memo에 넣어놨기 때문에 basecase x
def cs(n):
    for i in range(3, n+1): # 반복문을 통해서 아래에서 위로, memo에 저장
        memo[i] = memo[i-1] + memo[i-2] # 저장한 값을 통해 계산, 계산한 값을 memo에 저장
    return memo[n]
    