LIMIT = 10e8

def solution(A):
  sumRight = sum(A)

  result = 0

  for i in A:
    sumRight -= i

    if i == 0:
      result += sumRight

    if result > LIMIT:
      return -1

  return result
