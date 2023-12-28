def solution(X, A):
    filled = 0
    flag = [False] * X

    for idx, i in enumerate(A):
        i -= 1
        if not flag[i]:
            filled += 1
            flag[i] = True

        if filled == X:
            return idx

    return - 1


def solution2(X, A):
    result = (1 << X) - 1
    curResult = 0

    for idx, v in enumerate(A):
        # indices are 0-based but v was 1-based so we need to minus 1
        v -= 1
        curResult = curResult | (1 << v)

        if curResult == result:
            return idx

    return -1
