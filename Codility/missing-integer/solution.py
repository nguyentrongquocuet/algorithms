def solution1(A):
  l = len(A)
  flags = [False] * l

  for n in A:
    n -= 1

    if n < l and n >= 0:
      flags[n] = True

  for i in range(l):
    if not flags[i]:
      return i + 1

  return l + 1


def solution2(A):
  l = len(A)

  for i in range(l):
    if A[i] <= 0:
      A[i] = l + 1

  # now A contains only positive
  for i in range(l):
    n = abs(A[i])

    if n > l:
      continue

    n -= 1

    A[n] = -abs(A[n])

  for i in range(l):
    if A[i] > 0:
      return i + 1

  return l + 1
