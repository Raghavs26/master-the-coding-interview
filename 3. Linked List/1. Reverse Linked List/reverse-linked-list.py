class node:
    def __init__(self, val):
        self.data = val
        self.next = None


# 1 -> 2 -> 3
# null -> 1 -> 2 -> 3
# null <- 1 <- 2 <- 3
class Solution:
    def reverseList(self, head: node):
        current, prev:node = head, None
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev