---
tags:
  - tag1
  - tag2
---

# Count div

https://app.codility.com/programmers/lessons/5-prefix_sums/count_div/

# Problem Overview

Count how many number in range [A, B] that is dividable by K

# Solution Strategy

The minimum number dividable by K is ceil(A / K), we need to ceil because if not the number >= A
The maximum number dividable by K is floor(B / K), we need to floor because if not the number <= B
return floor(B / K) - ceil(A / K).
