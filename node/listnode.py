# linked_list.py
# Utilities and operations for singly linked lists

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ---------- Day 1 Basics ----------
def from_list(values):
    """Build a linked list from a Python list."""
    head = None
    for v in reversed(values):
        head = ListNode(v, head)
    return head

def to_list(head):
    """Convert a linked list back into a Python list."""
    out, current = [], head
    while current:
        out.append(current.val)
        current = current.next
    return out

def print_list(head):
    """Print all values in a linked list."""
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "")
        current = current.next
    print()


# ---------- Day 2 Operations ----------
def insert_head(head, val):
    """Insert a new node at the beginning."""
    return ListNode(val, head)

def insert_tail(head, val):
    """Insert a new node at the end."""
    if not head:
        return ListNode(val)
    current = head
    while current.next:
        current = current.next
    current.next = ListNode(val)
    return head

def delete_node(head, target):
    """Delete the first node with the given value."""
    dummy = ListNode(0, head)
    prev, current = dummy, head
    while current:
        if current.val == target:
            prev.next = current.next
            break
        prev, current = current, current.next
    return dummy.next

def reverse_list(head):
    """Reverse the linked list."""
    prev, current = None, head
    while current:
        nxt = current.next      # save next
        current.next = prev     # reverse link
        prev, current = current, nxt
    return prev


# ---------- Day 3 Operations ----------
def length(head):
    count, current = 0, head
    while current:
        count+=1
        current = current.next
    return count

def find_kth(head, k):
    current, idx = head, 0
    while current and idx < k:
        current = current.next
        idx += 1
    return current

def has_cycle(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False