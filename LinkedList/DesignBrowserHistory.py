# 인터넷 브라우저에서 방문기록과 동일한 작동을 하는 BrowserHistory class를 구현할 것이다. 구현할 브라우저는 homepage에서 시작하고,
# 이후에는 다른 url에 방문할 수 있다. 또, 뒤로가기와 앞으로 가기가 작동되도록 구현해라

# https://leetcode.com/problems/design-browser-history/

# 1. 문제 이해하기
# 제약 조건 확인 -> 시간 복잡도 관련 확인 -> visit을 할때마다 노드 추가 -> O(1), back은 doubling linkedlist로 구현해야함 -> 시간 복잡도는 O(n)
# worst case 생각 -> back(100), forward(100) -> step이 100까지 제한이므로, 100 * 4900 = 49000번이 worst
# worst case를 봤을때 49000이 10^8 보다 작으므로 시간 복잡도 고민을 안해도된다.
# 2. 접근 방법
# (1) input, output 먼저 보기 -> 순서가 있는 자료구조를 사용(뒤로도 가고 앞으로도 가기 때문에 선형 자료구조가 필요)
# (2) input에서 visit 부분에서 새로운 url에 방문하면 기록을 삭제하라는 부분에서 array에서는 지우기 힘든 부분이 많을것 같으므로 linkedlist 사용 -> 중간에 삽입이 가능하므로

# 3. 코드 설계
# head, tail, current 사용 염두
# homepage를 입력 받으면, 노드를 생성하고 head, tail, current가 node를 가리키게 구현, 
# doubly linkedlist로 구현, previous, next를 각각 가리킴, return 값으로 homepage 주소값
# visit은 tail이나 current가 next로 넘어갈수 있게 구현
# back은 step수로 반복문을 돌면서 current가 앞으로 갈 수 있게 구현
# forward는 step수 만큼 반복문을 돌면서 current가 뒤로 갈수 있게 구현
# current가 특정 노드를 가리키고 있을때 visit을 하면 그 뒤의 node를 삭제하고 새로운 노드에 연결하고 current가새로운 노드로 이동

# 4. 코드 구현

# doubly linkedlist로 구현
class ListNode(object): 
    def __init__(self, val = 0, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev

class BrowserHistory(object):
    def __init__(self, homepage):
        self.head = self.current = ListNode(val=homepage) #노드 생성, current와 head가 새로운 노드를 가리키게 설정
    def visit(self, url):
        self.current.next = ListNode(val=url, prev=self.current) # 새로운 사이트에 가기 위해서 새로운 노드 생성, value는 url, prev는 현재 current, currnet.next가 새로운 노드를 가리키게 설정
        self.current = self.current.next # current를 새로 생성된 노드로 한칸 옮김
        return None # visit 메소드가 끝나고 none 리턴(뒤의 정보는 삭제하라고 했으므로)
    def back(self, steps):
        while steps > 0 and self.current.prev != None: #step을 하나씩 줄이면서 0이 될때까지 반복, step이 0이 되지 않더라도(step이 남더라도) current.prev가 none이 되지 않을때 까지( 맨 앞 노드에 올때까지 계속 감)
            steps -= 1
            self.current = self.current.prev # current 한칸 앞으로 이동
        return self.current.val #step이 0이 되면 빠져 나와서 val값인 url 리턴
    def forward(self, steps):
        while steps > 0 and self.current.next != None:
            steps -= 1
            self.current = self.current.next #step을 하나 깎고 다음 노드로 current 이동
        return self.current.val # 빠져나오면 val 값 반환
