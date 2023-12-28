from collections import defaultdict
from typing import List


def solve(P: str, Q: str, idxList: List[int]):
  if len(idxList) == 0:
    return 0

  countMap = defaultdict(lambda: 0)

  for i in idxList:
    countMap[P[i]] += 1
    countMap[Q[i]] += 1

  chars = list(countMap.keys())

  # Highest frequency char
  hFC = chars[0]

  for c in chars:
    if countMap[c] > countMap[hFC]:
      hFC = c

  withHFCIdx = []
  withoutHFCIdx = []
  withoutHFCCharMap = {}

  for i in idxList:
    if P[i] == hFC:
      withoutHFCCharMap[Q[i]] = 1
    elif Q[i] == hFC:
      withoutHFCCharMap[P[i]] = 1
    else:
      withHFCIdx.append(i)

  for i in idxList:
    if P[i] not in withoutHFCCharMap and Q[i] not in withoutHFCCharMap:
      withoutHFCIdx.append(i)

  return min(solve(P, Q, withHFCIdx) + 1, solve(P, Q, withoutHFCIdx) + sum(withoutHFCCharMap.values()))


def solution(P: str, Q: str):
  l = len(P)
  dupChar = {}

  for i in range(l):
    if P[i] == Q[i]:
      dupChar[P[i]] = 1

  dIdx = []

  for i in range(l):
    if P[i] in dupChar or Q[i] in dupChar:
      continue

    dIdx.append(i)

  return sum(list(dupChar.values())) + solve(P, Q, dIdx)


if __name__ == "__main__":
  P = "fdddddabcih"
  Q = "cgbahfdaagg"

  print(solution(P, Q))
