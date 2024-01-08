from collections import deque

OPEN = "("
CLOSE = ")"


def solution(S):
  opens = deque()

  for c in S:
    if c == OPEN:
      opens.append(c)
      continue

    if len(opens) == 0:
      return 0

    opens.pop()

  return 1 if len(opens) == 0 else 0
