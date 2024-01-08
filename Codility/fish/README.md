---
tags:
  - stack
---

# Fish

https://app.codility.com/programmers/lessons/7-stacks_and_queues/fish/

# Problem Overview

Array A and B both of length N, B contains 1s and 0s, fish i has size A[i] and direction B[i], Fish swim from i to 0 if B[i] = 0, otherwise swim from i onwards. Two fish swim opposite could meat each other and eat eachother, the larger fish will win, the other will die. Count how many fish alive, given the speed is the same.

# Solution Strategy

Let's simplify it so we only consider if the upstream fish meets downstream fish. Upstream fish will eat the downstream fish until it is eaten.
Create a stack to store downstream fish, enumerate thru the fish list, if the fish going upstream, let it try to eat the downstream fish until it can't. Each time 2 fish meets, obviously 1 fish will die, we decrease the alive number from len(A) by 1 each time they encounter.
