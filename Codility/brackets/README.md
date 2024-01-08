---
tags:
  - stack
---

# Brackets

https://app.codility.com/programmers/lessons/7-stacks_and_queues/brackets/

# Problem Overview

Given string S, check if string S is properly nested by `()[]{}`

# Solution Strategy

This is surely a legendary question in the Stack topic.
When a string S is properly nested?

- Every close bracket properly closes one open bracket
- If we remove a pair that one close each other, the string must be empty

We have a stack that store the open bracket, we loop through string, if we encouter a close bracket, check if it closes the lastest open bracket, if it does, remove that open bracket from the stack, otherwise return False. In the end, if the open stack is empty, that means the string is properly nested.
