# 📘 Day 3 – Linked List Utilities, Cycle Detection & Big-O Basics

**Date:** Sept 8, 2025  

---

## ✅ Key Learnings

### Linked List Utilities
- **`length(head)`**: counts the number of nodes by walking through the list. → `O(n)` time, `O(1)` space.  
- **`find_kth(head, k)`**: walks node-by-node until reaching the k-th node. → `O(k)` time, `O(1)` space.  
- **`has_cycle(head)` (Floyd’s Algorithm):** uses two pointers (slow = 1 step, fast = 2 steps).  
  - If no cycle → `fast` hits `None`.  
  - If cycle exists → `fast` eventually laps `slow` inside the cycle.  
  - Complexity: `O(n)` time, `O(1)` space.

### Big-O Refresher
- **O(1):** constant extra work (or memory), independent of input size.  
- **O(n):** linear growth with number of nodes.  
- Important: often we highlight space complexity only when two approaches differ significantly (e.g., HashSet = `O(n)` space vs Floyd’s = `O(1)` space).  

---

## ❓ Questions I Asked Today
1. *Why doesn’t Floyd’s algorithm need many loops to catch up?*  
   → Because the fast pointer gains 1 step on the slow pointer per iteration. Within one cycle length, they must meet.  

2. *What exactly does `O(1) space` mean?*  
   → It means the algorithm only uses a fixed number of extra variables, no matter how big the input is.  

3. *Why do we sometimes emphasize space complexity and sometimes not?*  
   → Because in many basic linked list operations, extra memory is always constant. But in cycle detection, comparing HashSet (`O(n) space`) vs Floyd’s (`O(1) space`) highlights the advantage.  

---

## 🧪 Mini Test Results
- **Q1 (concept):** Correctly explained why fast and slow must meet in a cycle.  
- **Q2 (code):** Wrote `length(head)` function correctly, with proper traversal and counting.  
- **Q3 (logic MCQ):** Correctly chose option A (the invariant of Floyd’s algorithm).  

**Score:** 3/3 🎯  

---

## 📝 Reflection
- I understand better why Big-O space complexity is important when comparing different strategies.  
- The Floyd’s cycle detection algorithm is clever because it achieves `O(n)` time *and* `O(1)` space, unlike HashSet.  
- Writing utility functions like `length` helps me see linked lists as flexible but slower to access compared to arrays.  
