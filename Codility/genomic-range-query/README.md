---
tags:
  - prefix sum
  - array
---

# Genomic Range Query

https://app.codility.com/programmers/lessons/5-prefix_sums/genomic_range_query/

# Problem Overview

The given string S of length N contains only the letters ACGT, where the weight goes from 1 to 4, respectively. Array P and Q of length M contain pair l-r, find the minimum factor in range [l,r] of S

# Solution Strategy

1. Use prefix sum

We have a limited set of character, which are ACGT. At each range we can check if A exist, if exist then return 1, if not check for CGT in the ascending order of weight.

We construct a counter array of A, set 1 to the index that A appears on S and construct a prefix-sum array from it.
S = ACGTAATGA
A = [1, 0, 0, 0, 1, 1, 0, 0, 1]
P = [0, 1, 1, 1, 1, 2, 3, 3, 3, 4]
To get the number of A in range [l,r], we do P[r + 1] - P[l].
If the number is not 0 that means A is in range.

That is, we construct 4 array for each ACTG and using the above way to check.

2. Use monotonic queue

The idea is that, from l, keep finding the next index that <= r where weight is smaller than at i. Because we have only 4 weights, we need to jump at most 4 times

For the kind of problem where one needs to find the next smaller/larger value in an array, we use monotonic queue. In this case it is a non-strictly decreasing queue, that the queue always keeps the value decreasing(non-strictly) from left to right.

S = ACGTAATGA

At index i of array I holds the index j in S such that j > i where S[i] > S[j] or j = -1(in case nothing is smaller than S[i])

I = [-1, 4, 3, 4, -1, -1, 8, 8, -1]

**How the monotonic queue works?**

To add new value to the right of the queue, we need to pop right until the value >= the right most value in the queue. After that add new value to the queue. If new value i pops j out, that mean j > i.

**How to use monotonic queue to form I?**
We don't store value directly, instead we store index, that is, if index i pops index j out, S[j] > S[i], I[j] = i
