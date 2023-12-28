---
tags:
  - sum
---
# PermMissingElm
https://app.codility.com/programmers/lessons/3-time_complexity/perm_missing_elem/

# Problem Overview
Given array A contains N distinct numbers in the range [1 -> N + 1], find the missing element.

# Solution Strategy
Say we add the missing element to A, a becomes a set of 1 -> N + 1, so the sum will be (N + 1) * (N + 2) / 2.
To find the missing element, we just need to subtract that amount by the sum of A
