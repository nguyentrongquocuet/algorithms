def makePrefixSum(A):
  suffix = [0] * (len(A) + 1)

  for i in range(len(A)):
    suffix[i + 1] = A[i] + suffix[i]

  return suffix


def solution1Verbose(S, P, Q):
  N = len(S)
  M = len(P)

  A = [0] * N
  C = [0] * N
  G = [0] * N
  T = [0] * N

  for i in range(N):
    g = S[i]

    if g == "A":
      A[i] = 1
    if g == "C":
      C[i] = 1
    if g == "G":
      G[i] = 1
    if g == "T":
      T[i] = 1

  pA = makePrefixSum(A)
  pC = makePrefixSum(C)
  pG = makePrefixSum(G)
  pT = makePrefixSum(T)

  result = [0] * M

  for k in range(M):
    l = P[k]
    r = Q[k]

    if l < 0:
      l = 0

    if r >= N:
      r = N - 1

    if pA[r + 1] - pA[l] > 0:
      result[k] = 1
    elif pC[r + 1] - pC[l] > 0:
      result[k] = 2
    elif pG[r + 1] - pG[l] > 0:
      result[k] = 3
    elif pT[r + 1] - pT[l] > 0:
      result[k] = 4

  return result


def solution1(S, P, Q):
  N = len(S)
  M = len(P)

  A = [0] * (N + 1)
  C = [0] * (N + 1)
  G = [0] * (N + 1)
  T = [0] * (N + 1)

  for i in range(N):
    g = S[i]

    if g == "A":
      A[i + 1] = A[i] + 1
    else:
      A[i + 1] = A[i]
    if g == "C":
      C[i + 1] = C[i] + 1
    else:
      C[i + 1] = C[i]
    if g == "G":
      G[i + 1] = G[i] + 1
    else:
      G[i + 1] = G[i]
    if g == "T":
      T[i + 1] = T[i] + 1
    else:
      T[i + 1] = T[i]

  result = [0] * M

  for k in range(M):
    l = P[k]
    r = Q[k]

    if l < 0:
      l = 0

    if r >= N:
      r = N - 1

    if A[r + 1] - A[l] > 0:
      result[k] = 1
    elif C[r + 1] - C[l] > 0:
      result[k] = 2
    elif G[r + 1] - G[l] > 0:
      result[k] = 3
    elif T[r + 1] - T[l] > 0:
      result[k] = 4

  return result

from collections import deque

VALUES = {
    "A": 1,
    "C": 2,
    "G": 3,
    "T": 4,
}

def solution2(S, P, Q):
    N = len(S)
    M = len(P)

    I = [-1] * N

    queue = deque()

    for i in range(N):
        while len(queue) > 0:
            idx = queue.pop()

            if S[idx] > S[i]:
                I[idx] = i
            else:
                queue.append(idx)
                break

        queue.append(i)

    result = [0] * M

    for i in range(M):
        l = P[i]
        r = Q[i]

        if l < 0:
            l = 0

        if r >= N:
            r = N-1

        while True:
            nextSmallerIdx = I[l]

            if nextSmallerIdx == -1 or nextSmallerIdx > r:
                result[i] = VALUES[S[l]]
                break

            l = nextSmallerIdx

    return result
