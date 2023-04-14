# Maximum Depth of Binary Tree(level order)
# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# 문제 : 문제에서 binary tree 하나가 주어진다. 주어진 binary tree의 최대 깊이를 반환해라.

# 1. 문제 이해하기 : 제약 조건의 극한 상황도 생각해보기
# 시간 복잡도 : n^2 은 10^8이 되므로 이하의 시간 복잡도로 고려

# 2. 접근 방법 
# (1) 직관적 : 위에서 부터 내려오면서 레벨별로 depth를 하나씩 늘려가면서 세기 (level order)
# level order -> BFS와 비슷한 방식(deque 사용) -> FIFO 방식으로 root에 방문을 하고 다음 갈 노드에 예약을 걸어 놓고 예약한 노드를 큐에 넣어놓고 depth 정보도 같이 넣어놓는다.
# 방문한 노드들은  popleft로 빼고 예약하고 안간 노드는 냅두고 다음 예약할 노드를 넣는다. 그리고 마지막으로 방문하는 노드가 max depth 라는 방식
# child node가 있으면 예약을 큐에 저장을 한다. 저장을 할때 해당 노드의 depth 값을 같이 저장하여 마지막 노드에서 depth 값을 반환한다.

# 3. 코드 설계
# level order -> 큐 선언 -> enque -> while문으로 트리 순회 -> 큐에 popleft로 방문한 노드들 deque -> 예약 한 노드들을 큐에 enque -> enque를 할 때 depth 정보도 기입 -> max_depth 최신화 하면서 마지막 max_depth 반환
# 노드의 개수만큼 반복을 할 것이므로 시간복잡도는 O(N)

# 4. 코드 구현
from collections import deque

def maxDepth(root):
    max_depth = 0
    if root is None:
        return max_depth
    q = deque()
    q.append((root,1)) #enque, 방문할 노드에 예약, depth 정보도 같이 기입해야하기 때문에 현재 depth는 1이므로 1로 저장
    while q: # q가 소진될때 까지, popleft(dequeue) 되는 노드에 방문
        cur_node, cur_depth = q.popleft() # cur_node 뿐만 아니라 depth 값도 같이 dequeue 됨 
        max_depth = max(max_depth, cur_depth) # cur_depth가 증가하므로 마지막 cur_depth가 max_depth이다.
        if cur_node.left:
            q.append((cur_node.left, cur_depth + 1)) # left에 방문 예약 걸기, 현재 depth보다 아래의 레벨에 가는것이므로 depth에 +1
        if cur_node.right:
            q.append((cur_node.left, cur_depth + 1))
    return max_depth



class TreeNode: # root가 리스트로 주어져서 트리 구성
    def __init__(self, l=None, r=None, v=0):
        self.left = l
        self.right = r
        self.value = v

root = TreeNode(v=3)
root.left = TreeNode(v=9)
root.right = TreeNode(v=20)
root.right.left = TreeNode(v=15)
root.right.right = TreeNode(v=7)
print(maxDepth(root))

# tree가 나오면 구현이나 순회 떠올리기
# postorder, levelorder 방식
# 기본 템플릿 외우기