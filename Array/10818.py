# 백준 10818 최소, 최대 

# N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.
# 첫째 줄에 정수의 개수 N (1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄에는 N개의 정수를 공백으로 구분해서 주어진다. 모든 정수는 -1,000,000보다 크거나 같고, 1,000,000보다 작거나 같은 정수이다.
# 첫째 줄에 주어진 정수 N개의 최솟값과 최댓값을 공백으로 구분해 출력한다.

N = int(input())
nums = list(map(int, input().split())) #map(적용할 함수, 반복 가능한 자료형), split은 한 문자열을 나누어 리스트로 구분
print(min(nums),max(nums))

# input 한번에 여러개의 값을 받으려면 input에서 split을 하여 변수 여러개에 저장 가능하다
# N에 정수의 개수를 입력 받고, nums에 정수를 입력 받고 split을 이용하여 공백으로 구분