class Solution1:
  def distinctSubseqII(self, S):
    l = len(S)
    dp = [0] * (l + 1)
    # last occurrences of a letter
    dup = {}

    for i in range(l):
      dp[i + 1] = dp[i] * 2 + 1

      if S[i] in dup:
        j = dup[S[i]]
        dp[i + 1] -= dp[j - 1 + 1] + 1  # + 1 for the letter itself

      dup[S[i]] = i

    return dp[l] % (10**9 + 7)


class Solution2:
  def distinctSubseqII(self, S):
    # we store the whole alphabet but its OK to just store what's in S
    end = [0] * 26

    for c in S:
      end[ord(c) - ord('a')] = sum(end) + 1

    return sum(end) % (10**9 + 7)
