# 팩토리얼
def factorial(n):
    if n == 1: # base case : 더이상 재귀호출을 하지 않아도 계산값을 반환할 수 있는 상황(조건)
        return 1
    return n * factorial(n-1) 

factorial(4) # n=4 일 때, 4,3,2,1 까지 자기 자신을 호출 -> 4*3*2*1