# https://leetcode.com/problems/daily-temperatures/
# 문제 : 매일의 온도를 나타내는 int형 배열 temperatures가 주어진다. answer 배열의 원소 answer[i]는 i번째 날의 온도보다 더 따뜻해지기 까지
# 며칠을 기다려야 하는지 나타낸다. 만약 더 따뜻해지는 날이 없다면 answer[i] == 0 이다. answer 배열을 반환하는 함수를 구현하라.

# 1. 문제 이해하기
# 시간 복잡도 : 10^5 까지 이므로 10^8을 넘으면 안되기 때문에 n^2은 불가 -> nlogn, n, logn 중 하나로 풀어야한다.

# 2. 접근 방법
# (1) 직관적으로 생각 -> 완전 탐색 
# (2) 자료구조와 알고리즘 활용
# 완전 탐색 : 비교하려는 값을 기준으로 뒤의 숫자들을 쭉 훑으면서 기도하다가 더 큰 값이 나오면 그 값의 인덱스 - 비교하려는 값의 인덱스
# 인덱스 뺀값을 answer 배열에 저장 -> 완전탐색은 n^2이므로 불가 -> 다른 방법 고안
# 특정 조건을 만족하는 데이터가 들어올 때 까지 스택에 push (온도가 더 높은 데이터가 들어올때 까지 push), 더 높은 데이터가 들어오면 그 데이터 보다 낮은 데이터들은 pop
# 높은 데이터는 남기고, 다시 남은 데이터보다 높은 데이터가 들어올때까지 push
# 더 높은 데이터가 들어오면 방금 들어온 데이터에 가까운 남은 데이터 pop
# 들어온 순서 - 스택에 있는 날짜 반환
# 마지막 남은 데이터 pop
# stack을 사용하면 한번만 훑으면서 pop, push를 진행하면 O(n)으로 문제 풀이 가능

# 3. 코드 설계
# (1)반복문으로 input t 배열 훑으면서 push, pop 과정 진행완료되게 설계
# (2) 스택선언 후 반복문 구현
# (3) while문으로 현재 t보다 낮은 온도를 pop을 하고, 며칠 기다렸는지 계산
# (4) answer 배열에 며칠 기다렸는지를 업데이트
# (5) 낮은 온도가 없으면 stack에 t push

# 4. 코드 구현

def dailyTemperatures(temperatures):
    answer = [0] * len(temperatures) # answer 배열 초기화 (temperature 배열 길이 만큼 0을 넣어서 초기화)
    stack = []
    for cur_day, cur_temp in enumerate(temperatures): # O(n), 인덱스와 원소의 쌍을 튜플형태로, (현재 날짜와 온도를 쌍으로 반복문을 돌리기 위해 enumerate 사용)
        while stack and stack[-1][1] < cur_temp: # 현재 온도보다 낮은 온도가 있다면 pop, stack[-1] : top에 있는 데이터, [-1][1] -> top에 있는 데이터에서 (날짜(0번째 인덱스), 온도(1번째 인덱스))로 저장되있는 것중 온도를 나타냄
            prev_day , _ = stack.pop() # 날짜만 나오고(기다린 날짜를 계산하기 위해 prev_day 저장) 뒤에 온도는 _로 없앰
            answer[prev_day] = cur_day - prev_day # 기다린 날짜 업데이트 prev_day 업데이트
        stack.append((cur_day, cur_temp)) # 스택에 데이터가 없거나 현재 온도보다 높은 온도가 있다면 while문 빠져 나와서, 날짜와 온도 스택에 저장 
    return answer

dailyTemperatures([73,74,75,71,69,72,76,73])

# 5. 디스코드 week1 stack(LIFO) 문제 보기