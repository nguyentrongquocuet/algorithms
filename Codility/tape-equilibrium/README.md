---
tags:
  - sum
---
# TapeEquilibrium
https://app.codility.com/programmers/lessons/3-time_complexity/tape_equilibrium/
# Problem Overview
Given array A, index 0 < P < len(A) splits the array by 2 halves, find the minimum abs of the difference of two halves's sum
# Solution Strategy
sum(left) = sum(A) - sum(right)

Enumerate through the array and keep track of the sum up to that index. Check if the difference is the smallest
