# 정렬이 안된 리스트를 정렬 할 때의 시간 복잡도는 O(nlogn)
# two-pointer : 두 개의 포인터를 가지고 움직이면서 해결하는 방법
# 접근방법 : 반복문 방법에서는 시간 복잡도가 O(n^2) 인데 더 줄이기 위해서 정렬을 사용하여 시간 복잡도는 O(nlogn)
# 리스트를 정렬 후, 각 숫자를 더한 것과 target 값을 비교하는 방식 -> 타겟 값으로 이동하면서 생각
# 양 끝 숫자를 더한 후 타겟값보다 크면 오른쪽 숫자를 왼쪽으로 한칸 옮기고 타겟 보다 작으면 왼쪽 숫자를 오른쪽으로 움직이는 방식으로 비교

# 코드 설계
# nums 정렬 -> nums.sort()
# 가장 왼쪽 숫자 = left, 가장 오른쪽 숫자 = right
# l = 0, r = n-1 개
# nums[l] + nums[r] = target 인지 확인
# nums[l] + nums[r]이 > target r을 r-1(r을 왼쪽으로 한칸 이동), nums[l] + nums[r] < target이면, l을 l+1(l을 오른쪽으로 한칸 이동) -> 계속 반복
# 정렬은 nlogn, 반복문은 l과 r이 만날 때이므로, n개이므로 n번 실행 -> O(n)
# 전체 코드는 시간복잡도가 더 큰 O(nlogn)
def twoSum(nums, target):
    nums.sort() # 정렬, O(nlogn)
    l, r = 0, len(nums)-1
    while l<r: # 이 조건을 만족하면서 반복을 돌릴 것이므로 while 사용, O(n)
        if nums[l] + nums[r] > target:
            r -= 1 # 타겟 값보다 크면 r을 한칸 왼쪽으로 이동
        elif nums[l] + nums[r] < target:
            l += 1 # 타켓 값 보다 작으면 l을 한칸 오른쪽으로 이동
        elif nums[l] + nums[r] == target:
            return True
    return False

print(twoSum(nums=[2,1,5,7], target=4))
print(twoSum(nums=[4,1,9,7,5,3,16], target=14))

# https://leetcode.com/problems/two-sum/