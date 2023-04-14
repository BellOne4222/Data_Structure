# 피보나치 수열
def fibo(n):
    if n == 1 or 2: 
        return 1
    return fibo(n-2) + fibo(n-1) # fibo 함수 자기 자신을 호출

fibo(5)