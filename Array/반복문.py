# 1. 문제 이해하기
# 문제 :  정수가 저장된 배열 nums가 주어졌을 때, nums의 원소 중 두 숫자를 더해서 target이 될 수 있으면 True, 불가능하면 Fasle를 반환하세요. 같은 원소를 두 번 사용할 수 없습니다.
# 제약 조건 -> 시간 복잡도 먼저 파악

# 2. 접근 방법
# (1) nums 안에 있는 값들을 하나하나 다 더해서 target 값을 도출해본다. -> nums[i] + nums[j] = target(14)가 되면 되겠다 생각
# (2) 2중 반복문 생각(바깥에서 i, 안에서 j 돌리기) -> 바깥에서 O(n), 안에서 O(n)이므로 시간 복잡도는 O(n^2)

# 3. 코드 구현, 디버깅 해보면서 디테일 잡기 -> i,j 가 같은 원소인경우

def twoSum(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i+1,n): # i+1로 시작함으로써, i = 0, j=1 인 경우에서 부터 시작
            if nums[i] + nums[j] == target: #i,j = 0일때도 포함되기 때문에 같은 원소 사용은 불가한다고 했으므로, 
                return True
    return False

print(twoSum(nums=[4,1,9,7,5,3,16], target=14))

# https://leetcode.com/problems/two-sum/