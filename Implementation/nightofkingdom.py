# 왕실의 나이트
# p. 115
# 시뮬레이션

# 현재 나이트 위치 입력 받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1 # 열은 문자이므로 ord로 아스키코드 변환

# 나이트가 이동할 수 있는 8가지 방향 정의, L 자 움직임
steps = [(-2, -1),(-1, -2),(1, -2),(2, -1),(2, 1),(1, 2),(-1, 2),(-2, 1)]

result = 0

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)