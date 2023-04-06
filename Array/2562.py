# 백준 2562 최댓값

nums = [] # 빈 리스트 생성
for i in range(9): # 9개 이므로 9번 돌려서 입력값 리스트에 넣기
    nums.append(int(input()))

print(max(nums))
print(nums.index(max(nums))+1)  # 최댓값의 인덱스의 자리 번호 이므로 0번부터 시작하기 때문에 1을 더해야 자릿값이 나옴
