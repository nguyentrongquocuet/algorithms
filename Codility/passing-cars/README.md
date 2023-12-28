---
tags:
  - sum
---
# Passing cars
https://app.codility.com/programmers/lessons/5-prefix_sums/passing_cars/
# Problem Overview
Given array A of length N contains only 0 and 1, if P <= Q < N, we say P is passing Q, count how many pairs of P and Q are passing.

# Solution Strategy
At index P, we need to count the numbers of 1s after P because there are only 0 and 1, and the number of 1s after P is the sum of all the elements after P.

