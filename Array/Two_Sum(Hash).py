# 문제 :  정수가 저장된 배열 nums가 주어졌을 때, nums의 원소 중 두 숫자를 더해서 target이 될 수 있으면 True, 불가능하면 Fasle를 반환하세요. 같은 원소를 두 번 사용할 수 없습니다.

# https://leetcode.com/problems/two-sum/ 
# 해설 : https://deftkang.tistory.com/167

# 원소의 개수 = nums
# 시간 복잡도 : O(N제곱), O(NlogN), O(N) 이하의 시간 복잡도를 사용해야함(제약 조건 확인), N제곱을 사용하면 10의 8 제곱이 되므로 왠만하면 로그나 N 사용
# Hash 사용

# Hash로 푸는 방법은 target을 nums의 값과 빼서 Dictionary에서 찾고 없으면 추가한다.

def twoSum(self, nums, target):
    # target - nums 값을 seen에서 찾고 없으면 seen에 추가        
    seen = {}
 
    for idx, val in enumerate(nums):
        another = target - val
 
        if another in seen:
            # seen에 넣었던 값이 먼저 return 돼야 한다.
            return [seen[another], idx]
        else:
            seen[val] = idx
 
    return [-1, 1]   