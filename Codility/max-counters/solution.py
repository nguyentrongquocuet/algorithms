def solution(N, A):
    counters = [0] * N
    minCounter = 0
    maxCounter = 0

    for n in A:
        n -= 1

        if 0 <= n < N:
            # if counters[n] < minCounter, it wasn't updated since last time set maxCounter to N
            counters[n] = max(minCounter, counters[n]) + 1

            if counters[n] > maxCounter:
                maxCounter = counters[n]

        if n == N:
            minCounter = maxCounter

    for i in range(N):
        # if counters[n] < minCounter, it wasn't updated since last time set maxCounter to N
        counters[i] = max(counters[i], minCounter)

    return counters
