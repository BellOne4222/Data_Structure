# 완전 탐색으로 모든 노드를 방문하는 방식(깊이 우선 방식)

# 후위 순회 방식으로 leafnode에 가면 1을 반환하고, left와 right가 둘다 1이면 +1을 하는 방식으로 올라온다.
# 마지막 루트 노드를 가기전에 left의 최대 깊이와 right의 최대깊이 중에 가장 큰 값에 +1 을 하여 최종 max_depth를 반환

# 재귀 방식으로 코드 설계 : maxdepth() 함수 설계 -> basecase 설계 -> l = maxdepth(l)(왼쪽 childnode), r = maxdepth(r) -> 정보 취합 후 가장 깊은 depth 값에 +1
# -> return(l or r 중에 큰값) + 1
# postorder도 순회방식이기 때문에 n개의 node를 순회 하므로 시간 복잡도는 O(n)

from collections import deque

def maxDepth(root):
    max_depth = 0
    if root is None: # 루트 노드가 None이면 0
        return 0
    left_depth = maxDepth(root.left) # 왼쪽 노드의 깊이를 left_depth에 저장, 재귀 방식으로 leafnode 까지 반복
    right_depth = maxDepth(root.right)
    return max(left_depth, right_depth)+1 # 둘중에 하나 큰거에 +1, 재귀 방식으로 leafnode(left,right 둘다 None)에 갈때마다 값을 반환

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