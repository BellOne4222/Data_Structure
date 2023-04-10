from collections import deque # doubly ended queue -> front, rear 두 곳에서 dequeue를 양방향으로 가능하다.

queue = deque() # deque은 linkedlist로 구현되어있다.

# enqueue() O(1)
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)

# dequeue() O(1) -> front를 뒤로 한칸만 옮겨주면 되기때문에 O(1)
queue.popleft()
queue.popleft()
queue.popleft()