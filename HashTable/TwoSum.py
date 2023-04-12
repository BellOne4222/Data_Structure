# https://leetcode.com/problems/two-sum/

# 문제 : 정수가 저장된 배열 nums이 주어졌을 때, nums의 원소중 두 숫자를 더해서 target이 될 수 있으면 True, 불가능 하면 False를 반환하시오. 같은 원소를 두 번 사용할 수 없다.

# 2. 접근 방법 : 메모리 사용 -> 시간 복잡도를 줄이기 위해 메모리를 사용(해시 테이블)
# 딕셔너리에 input 값인 4를 key에 저장하고, value에 True를 저장 그리고 nums에 있는 값들을 같은 방식으로 저장
# 메모리를 사용하여 시간 복잡도를 낮추는 방법 사용

# 3. 코드 설계 : 반복문을 돌면서, nums의 value 값을 key에 저장, value에는 True 저장 
# nums의 값들에 반복문으로 돌면서, target 값 - i = n을 해서 n이 딕셔너리에 있는지 없는지 확인 하고, return True로 처리(O(1))
# 반복문이 돌아도 True 리턴이 안되면, return False로 반환 -> 둘이 더해도 Target 값이 안되는 경우
# 찾는 과정 O(1)을 반복문으로 n번 돌았으므로, 시간 복잡도는 O(n)

# 4. 코드 구현

def two_sum(nums, target): # nums, target이 two_sum으로 들어옴
    memo = {} #딕셔너리 선언
    for v in nums: # 딕셔너리의 키값에 밸류를 하나하나 저장 -> 딕셔너리에 있는지 없는지 판별하기 위해서 v:1 식으로 저장
        memo[v] = 1
    
    for v in nums: # 타겟이 될수 있는지 없는지 판별
        needed_number = target - v # 동일한 원소는 안된다고 하였으므로, 
        if needed_number in memo and needed_number != v : # O(1) hashfunction 사용, nums에서 찾으면 시간복잡도가 O(n^2)이 되므로 딕셔너리에서 찾는 방법을 사용해서 시간 복잡도를 줄일 수 있다.
            return True # 있으면 True 반환
    return False # 없으면 False 반환

print(two_sum(nums = [4,1,9,7,8,2], target= 14))
print(two_sum(nums = [7], target= 14))
# 딕셔너리를 쓰는 이유 : in을 사용해서 key 값이 내가 원하는 값이 있는지 없는지를 확인하기 위해 사용
