# 후위 순회 문제

# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/

# 문제 : Lowest Common Ancestor of a Binary Tree : 문제에서 Binary 트리 하나와 해당 트리에 속한 두 개의 노드가 주어진다. 이 때, 두 노드의 공통 조상 중 가장 낮은 node 즉, LCA를 찾아라.

# 시간 복잡도 : 모든 노드 순회 한번 -> O(n), Node.val -> 정수 범위, Node.val은 unique 하다 -> p,q 값 혼동 방지

# 2. 접근 방법 : p와 q의 노드 부터 위로 쭉 올라가 보는 방법 생각, 왼쪽 오른쪽에서 오는 정보로 내가 공통조상인지 판별하는 메커니즘

# 3. 코드 설계 : 트리 -> 재귀 -> 작게 구현을 해서 전체에 적용하는 방식으로 구현

# 1. leftchild, rightchild 둘 다 값이 없을때, root 자기 자신 반환
# 2. 자기 자신이 p 또는 q는 아닌데 왼쪽 오른쪽 둘 다 return 값이 없을 때, 아무것도 반환하지 않는다.
# 3. 왼쪽 오른쪽 둘다 return 값이 있을 때, 자기 자신이 공통 조상
# 4. 한 쪽에서만 들어올때는 한쪽에서 들어 온 것을 통과 시켜주면 됨

# 어떤 값을 리턴할지 알기 위해서는 왼쪽 오른쪽 에서 리턴값을 받아야 한다.
# -> 왼쪽 오른쪽 둘다 lca 함수 돌려보고 리턴값 결정
# lca는 가장 낮은 조상 리턴하는 함수

def LCA(root, p, q): # 가장 낮은 조상의 노드 값을 반환하는 함수, 왼쪽 오른쪽에서 값이 들어와야하고 정보를 취합해 리턴
    if root == None: # basecase
        return None
    
    # left right에서 어떤 값이 들어오는지 알기 위한 부분
    left = LCA(root.left, p, q)
    right = LCA(root.right, p, q)
    if root == p or root == q: # 나 자신이 p이거나 q이면 자기 자신 반환
        return root
    elif left and right: # left와 right 둘 다 리턴값이 주어질때(None 제외)
        return root
    return left or right # left, right가 둘다 none이면 None 반환, None과 값 하나가 들어오면 그 값 하나를 return

LCA([3,5,1,6,2,0,8,None,None,7,4],6,4) # p = 6, q = 4

# 트리 순회 문제 -> left right 값을 알아야 하기 때문에 left먼저,  right를 그 다음 방문을 하고 자기 자신을 방문하는 방식이므로 -> postorder 후위 순회

