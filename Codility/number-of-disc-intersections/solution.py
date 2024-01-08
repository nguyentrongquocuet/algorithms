def solution(A):
  # Implement your solution here
  l = len(A)
  start = [0] * l
  end = [0] * l

  for i in range(l):
    start[i] = i - A[i]
    end[i] = i + A[i]

  start.sort()
  end.sort()

  started = 0
  result = 0

  i = j = 0

  while i < l and j < l:
    # loop until we cannot end the disc any more
    if start[i] > end[j]:
      started = max(started - 1, 0)
      j += 1
      continue
    else:
      # it intersects with all disc before it, so we update result BEFORE increasing started
      result += started
      started += 1
      i += 1

  return result if result < 10000001 else -1
