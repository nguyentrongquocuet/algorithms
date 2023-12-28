def solution(A):
    S = sum(A)

    cs = 0
    cd = None

    for i in range(0, len(A)):
        if i > 0:
            right = S - cs

            if cd is None or abs(cs - right) < cd:
                cd = abs(cs - right)

        cs += A[i]

    return cd
