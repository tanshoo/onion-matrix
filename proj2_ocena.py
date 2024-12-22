import numpy as np
import time


class OnionMatrix:
    # tu wklejona będzie implementacja z rozwiązania
    pass

##############################################################################
# test m=n=3
##############################################################################
def test3x3():
    A1 = np.random.rand(3,3)
    A2 = np.random.rand(3,3)
    A3 = np.random.rand(3,3)
    A = np.vstack((
        np.hstack((A1, A1, A1)),
        np.hstack((A1, A2, A2)),
        np.hstack((A1, A2, A3))
    ))
    A_onion = OnionMatrix([A1, A2, A3])
    b = np.random.rand(9)
    return all( np.isclose(A@b, A_onion.multiply(b))) and \
        all( np.isclose(np.linalg.solve(A,b), A_onion.solve(b)))

##############################################################################
# czas mnożenia
##############################################################################
def test_multiply_time(n, m, N):
    times = np.empty(N)
    for i in range(N):
        v = np.random.rand(m*n)
        blocks = [np.random.rand(m,m) for _ in range(n)]

        # czas start!
        start = time.time()
        A = OnionMatrix(blocks)
        res = A.multiply(v)
        # mierzymy czas
        times[i] = time.time() - start

        # tu następuje ponadto sprawdzenie poprawności
        # wyniku i jeśli jest on niepoprawny, zwracane jest np.Inf

    return np.max(times)

##############################################################################
# czas rozwiązywania
##############################################################################
def test_solve_time(n, m, N):
    times = np.empty(N)
    for i in range(N):
        b = np.random.rand(m*n)
        blocks = [np.random.rand(m,m) for _ in range(n)]

        # czas start!
        start = time.time()
        A = OnionMatrix(blocks)
        res = A.solve(b)
        # mierzymy czas
        times[i] = time.time() - start

        # tu następuje ponadto sprawdzenie poprawności
        # wyniku i jeśli jest on niepoprawny, zwracane jest np.Inf

    return np.max(times)

##############################################################################
# jaki wynik?
##############################################################################
if test3x3():
    mark = 1
    print("Test 3x3 zdany. +1 do oceny.")
    mtime = test_multiply_time(1000,10,10)
    stime = test_solve_time(1000,10,10)

    mtime_treshA, mtime_treshB, stime_treshA, stime_treshB = .01, .05, .01, .05
    if mtime < mtime_treshA:
        mark += 3
        print(f"Czas mnożenia {mtime:.5f}s poniżej {mtime_treshA}s. +3 do oceny.")
    elif mtime < mtime_treshB:
        mark += 1
        print(f"Czas mnożenia {mtime:.5f}s od {mtime_treshA}s do {mtime_treshB}s. +1 do oceny.")
    elif mtime < np.Inf:
        print(f"Czas mnożenia {mtime:.5f}s powyżej {mtime_treshB}s. +0 do oceny.")
    else:
        print(f"Błędne wyniki mnożenia. +0 do oceny.")


    if stime < stime_treshA:
        mark += 4
        print(f"Czas rozwiązywania {stime:.5f}s poniżej {stime_treshA}s. +4 do oceny.")
    elif stime < 0.5:
        mark += 2
        print(f"Czas rozwiązywania {stime:.5f}s od {stime_treshA}s do:{stime_treshB}s. +2 do oceny.")
    elif stime < np.Inf:
        print(f"Czas rozwiązywania {stime:.5f}s powyżej {stime_treshB}s. +0 do oceny.")
    else:
        print(f"Błędne wyniki rozwiązywania. +0 do oceny.")


    print(f"Ocena = {mark}pkt")

else:
    print("Oblany test 3x3.\n Ocena 0 punktow.")

