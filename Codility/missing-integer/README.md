---
tags:
  - array
---

# Missing Integer

https://app.codility.com/programmers/lessons/4-counting_elements/missing_integer/

# Problem Overview

Given integer array A consists of N numbers, find the first positive integer that is not in A

# Solution Strategy

1. Use 1 counter array

- At first glance, the result must be somewhere in 1 -> N + 1. N + 1 happens when A consists of all numbers from 1 - N. Knowing that, we can make a counter array for just numbers from 1 -> N to mark numbers in A. Ultimately, we return the first number that is not in counters. If no such number is found, then return N + 1.

2. Use the input array as a flag array

- We need to modify the input array to 'mark' the existence of number, the goal is:
  - Ignore what needs to be ignored: 0 and negative numbers; another case is if the number is greater than N
  - Preserve the value of other numbers
- Set negative indices and 0 indices to N + 1  so they would be ignored. Now the set contains only positive integer
- If we know the integer is originally positive, we can get the original value from the positive or negative form
- Now we use the input array of length N to mark the existence of a number in A, idx 0 marks number 1, idx i marks number i+1.
- As we enumerate through the array, if the original number of that index say original(n) is in range (1 - N) we set the A[original(n)-1] to negative.
- In the end, those indices that still have positive value are those that aren't present in the list
