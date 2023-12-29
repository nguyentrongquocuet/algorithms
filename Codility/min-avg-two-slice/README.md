---
tags:
  - math
  - array
  - prefix sum
---
# Min Avg Two Slice
https://app.codility.com/programmers/lessons/5-prefix_sums/min_avg_two_slice/
# Problem Overview
Given array A of length N > 1, find the first index of the slice that has the smallest average.

# Solution Strategy

Mathematically speaking, in any array of length N > 3, there's always a sub-array of smaller size that has a smaller average compared to the array.

So now from 0 -> N-2, we compare average of set 3 and set 2. In the end, the only pair thats left unchecked is the set 2 [N-2, N-1]

## Solution proof
We prove that in any array A length N > 3, always lie a sub-array of size 2 or 3 that has smaller average; (I)
We dont prove it directly, we prove the other side is not true;

```
Say we divide A by m subarray of size 2 and n sub arrays of size 3. Denoted sub2i, sub3j
N = m * 2 + n * 3

avgA = average(A)
avgA = (avg21 * 2 + avg22 * 2 +... + avg2m * 2) + (avg31 * 3 + avg32 * 3 + ... + abg3n * 3) / (2m + 3n) (*)

avg2i = min(average(sub2)) (1)
avg3j = min(average(sub3)) (2)

From (1), (2) and (*) we have:
avgA >= (2 * avg2 * m + 3 * avg3 * n) / (2m + 3n). (**)

Assume that (I) is wrong (J), then:
avg2 > avgA (3)
avg3 > avgA (4)

Then from (3), (4) and (**) we have:
(2 * avg2 * m + 3 * avg3 * n) / (2m + 3n) > (2 * avgA * m + 3 * avgA * n) / (2m + 3n) = avgA * (2m + 3n)  / N = avgA * N / N = avgA (***)

From (**) and (***) we have:
avgA >= (2 * avg2 * m + 3 * avg3 * n) / (2m + 3n) > avgA. (****)

Statement (****) is always false, so the assumption (J) is wrong, so the assumption (I) is right.
```
