def solution(N):
  while N % 2 == 0:
    N = N // 2

  # now we go passed the first 1

  # result
  r = 0
  # current count
  c = 0
  while N > 0:
    if N % 2 == 0:
      c += 1
    else:
      if c > r:
        r = c

      c = 0

    N = N // 2

  return r
