import math


def solution(A, B, K):
  x = math.ceil(A / K)
  y = math.floor(B / K)

  return y - x + 1
