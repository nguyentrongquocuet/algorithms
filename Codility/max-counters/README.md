---
---
# Max Counters
https://app.codility.com/programmers/lessons/4-counting_elements/max_counters/
# Problem Overview
Given an array of N counters, each starts with 0, and a command array A.
Possible commands are:
* Increase i'th index of N by 1
* Set all indices of N by max(N)

# Solution Strategy
The obvious solution is to do exactly what the command tells us: increase the counter, keep track of maxCounter, and set it to N when needed. However, the approach proved so slow that it didn't pass the performance test.

The catch is that when setting maxCounter to N, we actually just set a min value for N. After setting the min value of N, if we increase index i, we get the latest value by comparing it with the min value before increasing. In the end, after all the commands are done, we check the last time if there's any element in N that is still smaller than the min, that means those elements weren't updated since the last time we set the maxCounter to N
