# 📘 Day 2 – Linked List Operations & Arrays vs Linked Lists

**Date:** Sept 7, 2025  

---

## ✅ Key Learnings

### Linked List Operations
- **Insert at head:** Create a new node, point `.next` to the old head, return the new node.  
- **Insert at tail:** Walk to the end of the list, attach the new node, and return the head.  
  - Edge case: if the list is empty (`head=None`), simply return a new node.  
- **Delete a node (by value):** Use a **dummy node** to simplify deletion logic, especially when the target node is the head.  
- **Reverse a linked list:** Maintain three pointers (`prev`, `current`, `nxt`) and flip links step by step until the list is reversed.

### Arrays vs Linked Lists (Complexity)
| Operation             | Array (Python list) | Linked List |
|-----------------------|----------------------|-------------|
| Access k-th element   | `O(1)`               | `O(k)`      |
| Insert at head        | `O(n)`               | `O(1)`      |
| Insert at tail        | `O(1)` amortized     | `O(n)` (unless tail pointer is kept) |
| Delete at head        | `O(n)`               | `O(1)`      |
| Delete in middle      | `O(n)`               | `O(k)`      |

- Arrays: contiguous memory → fast random access, but costly insertions/deletions.  
- Linked lists: scattered memory → slower access, but more flexible for head operations.  

---

## ❓ Questions I Asked Today
1. Why do we check `if not head:` in the `insert_tail` function?  
   → Because if the list is empty, we need to handle it by creating and returning a new single-node list.  

2. Can you explain how the `delete_node` function works when it uses a dummy node?  
   → Answer: the dummy node ensures there is always a `prev` pointer, so even if the head is deleted, the list remains connected.  

3. I’m still unclear about Big-O notation. What exactly does `O(n)` mean, and why don’t we write `O(n-k)` for deletions in arrays?  
   → Answer: Big-O describes worst-case growth with input size. While exact steps for deleting at index `k` are `n-k`, worst case is still proportional to `n`.  

---

## 🧪 Mini Test Results
- **Q1:** Explained correctly why arrays provide `O(1)` access and linked lists require `O(k)` traversal.  
- **Q2:** Wrote `insert_tail`; initial version missed the empty-list case and return value, but corrected after review.  
- **Q3:** Correctly reasoned why saving `nxt=current.next` is necessary before reversing.  

**Score:** 3/3 after minor fix 🎯  

---

## 📝 Reflection
- The dummy node technique is a powerful way to simplify edge cases.  
- Big-O makes more sense when viewed as “growth trend” rather than exact steps.  
- I need to be more mindful of edge cases (like an empty list) when writing functions.  
