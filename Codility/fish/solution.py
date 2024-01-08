from collections import deque


def solution(A, B):
  downstream = deque()

  l = len(A)

  alive = l

  for i in range(l):
    # if this fish going downstream
    if B[i] == 1:
      downstream.append(i)
      continue

    # eat until be eaten
    while len(downstream):
      lastDownstream = downstream.pop()

      if A[lastDownstream] < A[i]:
        alive -= 1
        continue
      else:
        downstream.append(lastDownstream)
        alive -= 1
        break

  return alive
