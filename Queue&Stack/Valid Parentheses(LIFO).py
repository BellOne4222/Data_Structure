# https://leetcode.com/problems/valid-parentheses/
# 괄호 유효성 문제(LIFO 문제)
# Valid Parentheses : () {} [] 를 포함하고 있는 문자열 s가 주어졌을 때 괄호가 유효한지 아닌지 판별하시오.
# -> 괄호가 잘 닫혔는지 확인하는 문제 잘 닫혔으면 True 반환, 아니면 False 반환

# 1. 문제 이해
# 시간 복잡도 : 제약 조건이 10^4 까지 이므로 n^2은 안된다. -> nlogn or n

# 2. 접근 방법
# (1) 여는게 있으면 닫는게 있어야 하므로 -> 짝수 -> 반복문 돌려서 여는걸 +1, 닫는걸 -1로 하여 더해서 0이 되면 True
# (2) 여는게 먼저 와야한다. -> 반복문 돌리면서 중간에 음수가 나오면 닫는게 먼저 인걸로 판별하는 방식
# (1) , (2)는 소괄호만 놓고 접근 방법 설정 -> 이제 중괄호랑 대괄호 포함 접근 방법 설정

# 소괄호 중괄호 대괄호 따로 분류하여 각각 계산
# 종류 별로 숫자를 매겨야 하고, 다른 괄호를 닫기 전에 다른 괄호로 닫으면 안되므로 순서도 중요
# 마지막에 온 여는 괄호를 먼저 처리해야 하므로 -> LIFO(stack) 사용 -> top에 있는 괄호 확인
# 짝이 맞는 괄호는 pop을 하다가 여는 괄호와 닫는 괄호가 안맞으면 False 처리

# 짝이 맞아서 나 pop한 경우 stack이 비면 합계가 0이 되게 설계

# 3. 코드 설계
# (1) 입력 문자열 S에서 반복문 돌려서 만약 '( { [' 이면, stack에 push()
# (2) 만약 ') } ]'가 들어오면, 스택의 괄호랑 짝이 되면 stack.pop(), 짝이 맞지 않다면, return False
# (3) 반복문을 다 돌고 나왔을 때,  stack에 데이터가 남아있으면 return False, 스택이 비어있으면 return True
# (4) listStack -> 시간 복잡도 계산 : push, pop -> O(1), 반복문은 문자열의 길이가 n일때 이므로, O(n) 즉, O(n)

# 4. 코드 구현

def isValid(s):
    stack = []
    for i in s:
        if i == "(":
            stack.append(")")
        elif i == "{":
            stack.append("}")
        elif i == "[":
            stack.append("]")
        elif not stack or stack.pop() != i: # 문자열 s 반복문 돌리다가 닫는 괄호가 나오면, 스택이 비어있지 않으므로, pop을 해서 i와 같지 않은지 판별 -> top에 있는 괄호와 짝이면 pop 
            return False
    return not stack