# 상하좌우
# p.110
# 시뮬레이션

N = int(input())
x, y = 1, 1 # 초기 좌표 설정
plans = input().split()

# LRUD에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_direction = ['L', 'R', 'U', 'D']

# 이동 계획 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_direction)):
        if plan == move_direction[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > N or ny > N:
        continue
    # 이동 수행
    x,y = nx, ny

print(x,y)
