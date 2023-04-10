# queue 선언
q = []

# enqueue O(1) -> rear에 데이터 추가
q.append(1)
q.append(2)
q.append(3)
q.append(4)

# dequeue O(n) -> front 에서 데이터 추출
q.pop(0) # pop을 하면 데이터 추출 후 한 칸씩 앞으로 데이터 이동 -> O(n)
q.pop(0)
q.pop(0)