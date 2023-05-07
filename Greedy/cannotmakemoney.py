# 만들 수 없는 금액
# p.314

# N = int(input())
# money = list(map(int, input().split()))

N = 5
money = [3,2,1,1,9]
money.sort()

target = 1 # target 값 업데이트 하는 방식, 1이면 최소는 1이므로 target을 1로설정
for i in money:
    if target < i: # target이 i 보다 작으면 탈출, 만들 수 없는 금액을 만나면 탈출
        break
    target += i # else: target에 i를 더하며 target 갱신

print(target)