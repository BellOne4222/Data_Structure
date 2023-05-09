# 시각
# p. 113
# 완전 탐색(brute force)
# 가능한 경우의 수를 모두 검사해 보는 탐색 방법
# 86400가지

H = int(input())
# H = 5
count = 0

# 시
for h in range(H+1):
    # 분
    for m in range(60):
        # 초
        for s in range(60):
            # 매 시각 안에 3이 포함되어 있다면 카운트 증가, 문자열로 처리해 더해서 이어준 다음에 처리
            if '3' in str(h)+str(m)+str(s):
                count += 1

print(count)
