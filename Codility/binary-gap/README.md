
# Binary gap
https://app.codility.com/programmers/lessons/1-iterations/binary_gap/

# Problem Overview
Given number N, returns the maximum gap between two 1s in N's binary representation

# Solution Strategy
Divide N by 2 until we find the first 1-bit. Keep dividing; if N is dividable by 2, increase the count by 1; otherwise compare the count to the current result and reset the count to 0. Stop when N < 1
