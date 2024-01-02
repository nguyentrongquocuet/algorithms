---
tags:
  - dp
  - strings
---
# 940. Distinct Subsequences II
https://leetcode.com/problems/distinct-subsequences-ii
# Problem Overview
Given a string s, return the number of distinct non-empty subsequences of s. Since the answer may be very large, return it modulo 10e8 + 7.

# Solution Strategy

## Solution 1, how many subsequences up to index `i` if we already knew the result up to index `i-1`
Given string `abcb` as an example.
* There's only 1 subsequence of `a`.
* Subsequence of `ab` includes subsequence of `a`, subsequence of `a` with `b` attached to the end, and `b` itself: `a, ab, b`
* Same as above, subsequence of `abc` includes subsequence of `a`, `ab`, `a` attached with `c`, `ab` attached with `c` and `c` itself, but `ab` already includes subsequence of `a` so we dont count twice: `a, ab, b, ac, abc, bc, c`
* Here comes the catch, we have another `b`, lets use the theory above, the result would be `a, ab, b, ac, abc, bc, c, ab, abb, bb, acb, abcb, bcb, cb, b`, we have duplicate `ab, b`, the letter itself and the subsequence of `a` attached to `b`

Say we have total `k` subsequences at index `i`, we also have the same letter at index `j` < `i`, `S[i] == S[j]` so the part of `j-1` attached to `S[i]` and `j-1` attached to `S[j]` plus `S[i]` itself will be the duplication.

The final formula: dp[i] = dp[i-1] * 2 + 1 or dp[i-1] * 2 - dp[j-1]
We only count the `j` which closest to `i` because as we described, `dp` contains the distinct subsequence so even if there's multiple indices that has the same letter, the duplication is already excluded.

## Solution 2, how many subsequences that ends with `S[i]` if we already knew subsequences that ends with `S[j < i]`

Again let's take `abcb` as an example:
Initially the number of subsequences(NOS) is as follows:
```
dp = {
  a: 0,
  b: 0,
  c: 0
}
```

To get the NOS of `S[i]` we simply add `S[i]` to the end of every prev NOS, plus the letter itself so `dp[S[i]] = sum(dp) + 1`. Note that as we calculating `S[i]`, we explicitely concat `S[i]` to the end of prev NOS, even if theres `S[i]` in `dp`, after concat it becomes `S[i]S[i]`, so we do need to plus 1

We start with `S[0]` which is `a`
```
dp = {
  a: 0 + 1, # a
  b: 0,
  c: 0
}
```

Same with `S[1]` (`b`)

```
dp = {
  a: 1, # a
  b: 1 + 1, # ab, b
  c: 0
}
```

With `S[2]`(`c`)

```
dp = {
  a: 1, # a
  b: 2, # ab, b
  c: 1 + 2 + 1, # ac, abc, bc, c
}
```

With `S[3]`, which is also `b`

```
dp = {
  a: 1, # a
  b: 1 + 2 + 4 + 1, # ab, abb, bb, acb, abcb, bcb, cb, b
  c: 4, # ac, abc, bc, c
}
```

At the end, the result is the total of all subsequences that end with the letter in `S`
