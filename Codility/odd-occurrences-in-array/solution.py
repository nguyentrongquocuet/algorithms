def solution(A):
  r = 0

  for i in A:
    r = r ^ i

  return r
