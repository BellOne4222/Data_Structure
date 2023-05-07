# 문자열 뒤집기
# p. 313

# nums = list(map(int, input().split()))
nums = '0001100'
reverse0 = 0 # 전부 0으로 바꾸는 경우
reverse1 = 0 # 전부 1로 바꾸는 경우

if nums[0] == 0: # 첫째자리 판별
    reverse1 += 1 
else:
    reverse0 += 1

for i in range(len(nums)-1): # 두번째자리부터 끝까지
    if nums[i] != nums[i+1]: 
        if nums[i+1] == 1: # 다음 수에서 1로 바뀌는 경우
            reverse0 += 1
        else: # 다음수에서 0으로 바뀌는경우
            reverse1 += 1

print(min(reverse0, reverse1))

