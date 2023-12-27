# Minimum distinct letters

https://app.codility.com/programmers/custom_challenge/pi_challenge_2023/

# Problem Overview
The task involves constructing a string S of length N using two given strings, P and Q, also of length N. The construction rule for S is such that each character in S is either taken from P or Q at the respective index. The aim is to determine the minimum count of distinct letters in S.

# Solution Strategy
1. Initial Considerations:
* If both P and Q have the same character at an index, that character must be included in the distinct set as it's the only available choice.

2. Identifying Unique Letters:
* Extract unique characters from P and Q (P1 and Q1) where they differ at every index.

3. Reduced Problem:
* Solve the reduced problem for P1 and Q1 to find the count of distinct letters.
4. Optimization for Efficiency:

* Optimize by selecting the most frequently occurring letter (H) in P1 and Q1.
* Two choices:
    * Choose H: Exclude H from P1 and Q1.
    * Don't choose H: Retain H in P1 and Q1, excluding the selected replacement characters.
5. Comparative Analysis:

* Compare the counts obtained from the above two choices for the reduced problem.
* If not choosing H introduces new letters, exclude these entirely from P1 and Q1.
* Adjust the count accordingly if new letters are introduced.
6. Recursive Approach:
* Recursively apply the above steps for the chosen path to minimize the count.
* Evaluate the minimum count between the two paths.
* This strategy aims to minimize the count of distinct letters by efficiently selecting letters and recursively solving the reduced problems to determine the optimal choice at each step.
## The Award

https://app.codility.com/cert/view/certTUWZBG-E7Q9979SWGA4UEUZ/
