score = {
    'math' : 97, # 값은 중복될 수 있지만 key 값은 중복 불가
    'eng' : 49,
    'kor' : 89
} # 중괄호로 딕셔너리 선언

score['math']

score['math'] = 45 # 초기화
print(score['math'])
score['sci'] = 100 # 딕셔너리에 추가
print(score['sci'])

print('music' in score) # music이라는 key 가 딕셔너리 안에 있는지 확인

if 'music' in score: # key in dictionary명 = 찾는 과정 => O(1)
    print(score['music'])
else:
    score['music'] = 0