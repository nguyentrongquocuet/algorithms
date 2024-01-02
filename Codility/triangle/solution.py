def solution(A):
  N = len(A)

  if N < 3:
    return 0

  A.sort()

  i = N - 1

  while i > 1:
    if A[i - 1] + A[i - 2] > A[i]:
      return 1

    i -= 1

  return 0
