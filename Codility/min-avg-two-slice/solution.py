def solution(A):
  l = len(A)
  minAverage = None
  minIdx = 0
  pA = [0] * (l + 1)

  for i in range(l):
    pA[i + 1] = pA[i] + A[i]

  i = 0

  while i < l - 2:
    a2 = (pA[i + 2] - pA[i]) / 2
    a3 = (pA[i + 3] - pA[i]) / 3

    if minAverage is None or a2 < minAverage or a3 < minAverage:
      minIdx = i
      minAverage = min(a3, a2)

    i += 1

  # i is now l - 2
  # the last slice that we havent checked is [l-2, l-1]
  a2 = (pA[i + 2] - pA[i]) / 2

  if minAverage is None or a2 < minAverage:
    minIdx = i

  return minIdx
