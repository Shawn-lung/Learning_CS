class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

values = [1,2,3,4]
head = None
for i in reversed(values):
    head = ListNode(i, next=head)

current = head
while current is not None:
    print(current.val)
    current = current.next