from collections import deque

BRACKET = {
    '(': ')',
    '{': '}',
    '[': ']'
}

def solution(S):
  openQ = deque()

  for bracket in S:
    # open
    if bracket in BRACKET:
      openQ.append(bracket)
    else:
      # close bracket but hasn't open yet
      if len(openQ) == 0:
        return 0

      lastOpen = openQ.pop()

      # if this bracket doesn't close the last open braket
      if bracket != BRACKET[lastOpen]:
        return 0

  return 1 if len(openQ) == 0 else 0
