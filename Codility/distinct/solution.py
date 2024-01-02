def solution1(A):
  if not len(A):
    return 0

  A.sort()

  distinct = 1

  i = 1

  while i < len(A):
    if A[i] != A[i - 1]:
      distinct += 1

    i += 1

  return distinct

def solution2(A):
  m = {}

  for n in A:
    m[n] = True

  return len(m)
