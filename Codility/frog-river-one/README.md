---
tags:
  - bitwise
  - set
  - bitmasking
---
# Frog River One
https://app.codility.com/programmers/lessons/4-counting_elements/frog_river_one/
# Problem Overview
Given X and array A, find the first index that the numbers from 0 - that index fill up the range from 1 - X. If no such index, return -1

# Solution Strategy
## 1. Using Set
* Using an array(or a set), count how many numbers are filled at each index. If we fill in enough X numbers, return that index. At the end return -1

## 2. Bitwise
* The solution using Set involves O(n) space. We can eliminate that using a technique called bit-masking
* We have a number that acts like a Set, that is, at each index, we set the respective bit to 1, and when all bits are set to 1, we return that index. At the end, return -1
* To set n'th bit of K to 1, we do K = K | (1 << n)
* To get n bits integer where all bits are 1, we do I = (1 << n) - 1
