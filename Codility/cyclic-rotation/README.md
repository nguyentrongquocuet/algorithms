# Cyclic rotation

https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation/

# Problem Overview

Given array A, number K, rotate the array A K times, in each time, shift each index to the right, the rightmost index to the first index

# Solution Strategy
## 1. Return a new array

- If we shift by the length of A, it becomes itself. So the first thing to do is to get the modulo of K by len(A)
- Now we know that in the result, K latest elements of A will be on the left, and len(A) - K elements will be on the right. We need to connect those 2 parts

## 2. Modify the input array
- In each rotation, our job is to move each index to the next while saving the previous value of the following index for the next loop. In the end, the saved value becomes the latest element; we just need to set it to the first element
