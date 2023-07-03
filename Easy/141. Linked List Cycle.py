# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x,y):
#         self.val = x
#         self.next = y

# Два флага X и Y
# X.speed =1 Y.speed =2
# Если X и Y находятся в одной и той же точке на конец своего движения то существует цикл
# Если Y достигает Null node, то цикла нет


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
