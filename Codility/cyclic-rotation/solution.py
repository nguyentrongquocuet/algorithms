def solution1(A, K):
  l = len(A)

  if l < 2:
    return A

  K = K % l

  if K == 0:
    return A

  left = A[0: l - K]
  right = A[l - K:]

  return [*right, *left]


def solution2(A, K):
  l = len(A)

  if l < 2:
    return A

  K = K % l

  while K > 0:
    K -= 1
    lastV = A[0]

    for i in range(1, l):
      A[i], lastV = lastV, A[i]

    A[0] = lastV

  return A
