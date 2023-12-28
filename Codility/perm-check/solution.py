def solution(A):
    flag = [False] * len(A)
    filled = 0

    for n in A:
        n -= 1

        if n >= len(A) or flag[n]:
            return 0

        filled += 1
        flag[n] = True

    return 1 if filled == len(A) else 0
