---
tags:
  - binary
  - bitwise
  - XOR
---

# OddOccurrencesInArray

https://app.codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/

# Problem Overview

Array A contains an odd number of elements, knowing that only one element occurs at an odd time. Find that element

# Solution Strategy

Naive solution is to count each element and find the answer, but we have more efficient if we leverage the bitwise XOR(exclusive OR) operator.

The operator XOR, when applied to 2 numbers: At each bit, XOR returns 0 if two bits are the same; otherwise, it returns 1.

a ^ b = b ^ a, a ^ a = 0;

Given that, the answer to this problem is accumulatively xor every number together
