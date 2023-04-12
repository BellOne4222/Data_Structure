# https://leetcode.com/problems/longest-consecutive-sequence/

# 문제 : 정렬되어 있지 않은 정수형 배열 nums가 주어졌다. nums 원소를 가지고 만들 수 잇는 가장 긴 연속된 수의 갯수는 몇 개인지 반환하시오.

# 1. 문제 이해하기 : output을 보면 중복된 숫자는 빼고 개수 세기, input size는 N이고, 시간 복잡도는 제약조건에 따라, O(n^2) 미만의 시간복잡도로 풀어야한다.
# nums 배열의 최소길이가 0이므로 nums 배열이 비어있는 경우도 고려해야한다.
# 제약 조건의 nums[i]의 범위를 보면 int 자료형이라는 것을 알 수 있다.

# 2. 접근 방법 : 다음의 숫자가 있는지 없는지 체크 하면서 다음수가 있다면 다음수를 찾고 없으면 다음 숫자를 기준으로 탐색
# 중복 제거 -> if 시작점일때만, while문 실행, 시작점은 기준 숫자의 앞에 숫자가 없을 때
# 다른 접근 방법: 정렬 후 (O(n)) 비교를 하면, O(nlogn)이 된다.

def longestConsecutive(nums):
    longest = 0 # 연속된 개수를 저장하는 곳 초기화
    num_dict = {} # 딕셔너리 선언
    for num in nums: # 딕셔너리에 넣기
        num_dict[num] = True # value값 True로 선언
    # num_set = set(nums)를 이용해 value값을 설정하는 과정을 없앨수 있다.
    for num in num_dict: # 연속된 수 있는지 확인
        if num -1 not in num_dict: # 시작점을 알기위해 num의 앞에 있는 숫자가 딕셔너리에 있는지 없는지 판별
            cnt = 1
            target = num + 1
            while target in num_dict: # 타겟이 있는지 없는지 바로 확인 O(1), while은 특정 조건을 만족해야 돌아가기 때문에 n번 반복이 아닌, 타켓에 접근하는건 1번이기 때문에 n이 아니다.
                target += 1 # 다음수를 확인하기 위해 +1을 해줌
                cnt += 1
            longest = max(longest, cnt)
    return longest

print(longestConsecutive([6, 7, 100, 5, 4, 4]))

# 참고할만한 코드
# class Solution:
#     def longestConsecutive(self, nums: list[int]) -> int:
#         result = 0
#         if not len(nums):
#             return result

#         num_dict = {x(key): x + 1(value) for x in nums} # 파이썬의 comprehension 방식, 반복문으로 딕셔너리 초기화
#         for n in nums:
#             target = n
#             cnt = 0
#             if n - 1 not in num_dict:
#                 while target in num_dict:
#                     target = num_dict[target] # key에 target을 넣고 value에 true대신 next target값을 넣어서 기존의 +1 해주는 방식 대신 value값을 target값 저장하는 용도로 사용
#                     cnt += 1
#                     if result < cnt:
#                         result = cnt

#         return result