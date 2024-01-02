---
tags:
  - sort
---
# Triangle
https://app.codility.com/programmers/lessons/6-sorting/triangle/

# Problem Overview
Determine whether a triangle can be built from a given set of edges.

# Solution Strategy
3 edges are a, b, c where:
a + b > c
c + b > a
a + c > b

We can have 3 for-loop for each of them and just check. However that's not the point of making this an algorithm question.

Say c is the largest edge in the triangle: a < c and b < c, the conditions become a + b < c only, b/c the other 2 are always true.
Say a and b are the largest numbers that are smaller than c in the set, if a + b <= c then there's no triangle we could form from the set with c as largest edge, b/c anything else is smaller than a and b. but if a + b > c we have at least a-b-c as a triangle.
That is, we just need to sort the list, check from right to left if there's a triplet that A[i-1] + A[i-2] > A[i]
