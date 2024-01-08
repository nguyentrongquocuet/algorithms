---
tags:
  - sorting
---
# NumberOfDiscIntersections
https://app.codility.com/programmers/lessons/6-sorting/number_of_disc_intersections/
# Problem Overview
Given array A of length N contains integers, disc i expand from i - A[i] to i + A[i], how many discs are intersecting?

# Solution Strategy

## When two disc intersect?

They intersect when one started but the other hasn't ended.
Say disc [-1, 1] and [0, 10], disc 2 starts at 0 but disc 1 only ends at 1.
Say disc [-1, 1] and [1, 3], disc 2 starts at 1, disc 1 also ends at 1 but b/c the discs contain their border, so we count them as intersected.

## Pick the one that starts earliest first
Say A [1, 5, 2, 1, 4, 0], they starts and ends at [-1, -4, 0, 2, 0, 5] and [1, 6, 4, 4, 8, 5] respectively

Now we pick the one that starts earliest first. So we sort `starts`
-1: did any disc ends before -1, no
-4: did any disc ends before -4, no. -1 hasn't ended yet, so we have 1 intersect
0: ...., -1 and -4 hasn't ended yet, so we have 2 more intersections with -1, -4
0: ...., -1 and -4 and the other 0 hasn't ended yet, so we have 3 more intersections with -4, -1, 0
2: -1 is ended, so we remove -1, we have -4, 0, 0 hasn't ended, so we have 3 more intersections with -4, 0, 0
5: the first 0 was ended, so we have 2 more intersections with the other 0 and -4

We checked all discs, there are some discs that haven't ended yet, but we don't care.

Totally we have 1 + 2 + 3 + 3 + 2 = 11

We don't need to know which one is ended, we only cares about the number of them, and to make it even easier to compare, we can sort the `ends`.

## Summary
So in simple term, we have `i`, `j` and `started` go from 0, we increase `j` until `end[j] > start[i]`, along with decreasing `started` by one each time, after `start[i] <= end[j]`, we know that the new disc just starts, so it will intersect with all the disc that started before it, `result = result + started`, after that we increase `started` by 1
