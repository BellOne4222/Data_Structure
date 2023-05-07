# 볼링공 고르기
# p.315

# 조합을 이용, 무게에 따라 분류하고, 무게가 1인 경우에 B가 선택하는 경우의 수를 구해서 result 업데이트

N, M = map(int, input().split())
weight = list(map(int, input().split()))

array = [0] * 11 # 1부터 10까지 무게를 담을수 있는 리스트, 무게는 1~10까지 있으므로

for i in weight: # 각무게에 해당하는 볼링공의 개수 카운트
    array[i] += 1

result = 0

for j in range(1,M+1): # 1부터 m까지의 각 무게에 대하여 처리
    N -= array[j] # 무게가 j인 볼링공의 개수(A가 선택할 수 있는 경우의수) 제외
    result = array[j] * N # B의 선택하는 경우의 수와 곱하기

print(result)