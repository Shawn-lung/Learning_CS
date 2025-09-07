class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def insert_tail(head,val):
    if head:
        return ListNode(val)
    current = head
    while current.next:
        current = current.next
    current.next = ListNode(val)
    