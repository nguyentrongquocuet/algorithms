---
tags:
  - stack
---

# Nesting

https://app.codility.com/programmers/lessons/7-stacks_and_queues/

# Problem Overview

Given string S consists of `(` and `)`, check if S is properly nested

# Solution Strategy

It's the same as the Brackets problem, except this time we have only 1 type of bracket.
Stack S to store the open bracket, each time encouter a close bracket, pop if S is not empty, otherwise return 0. In the end, if S is not empty that means the number of opens and close are not equal, return 0 if its the case otherwise return 1
