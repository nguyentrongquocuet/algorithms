---
tags:
  - set
---
# Perm Check
https://app.codility.com/programmers/lessons/4-counting_elements/perm_check/
# Problem Overview
Given array A has N number, check if A contains all numbers from 1 - N(A is a permutation)

# Solution Strategy
Count the occurrence of each number
* If A has a number that occurs twice, A is not a permutation
* If A has a number that exceeds N, A is not a permutation
* If we don't fill enough N numbers, A is not a permutation
* If none of the above is true, A is a permutation
