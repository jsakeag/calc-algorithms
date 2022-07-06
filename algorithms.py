from multiprocessing.connection import wait
from tracemalloc import stop
import numpy as np
import sys
import time


def trapezoid_rule():
    a = 0
    b = np.pi
    n = 2
    N = 11

    while(n <= N):
        h = (b - a) / (n - 1)
        x = np.linspace(a, b, n)
        f = np.sin(x)

        I_trap = (h/2)*(f[0] + 2 * sum(f[1:n-1])
                        + f[n-1])
        err_trap = 2 - I_trap

        print(chr(27) + "[2J")
        print("Trapezoid rule estimation with " +
              str(n) + " points: " + str(I_trap))
        print("Error: " + str(err_trap))

        n += 1
        time.sleep(0.25)


def simpsons_rule():
    a = 0
    b = np.pi
    n = 2
    N = 11

    while(n <= N):
        h = (b - a) / (n - 1)
        x = np.linspace(a, b, n)
        f = np.sin(x)

        I_simp = (h/3) * (f[0] + 2*sum(f[:n-2:2])
                          + 4*sum(f[1:n-1:2]) + f[n-1])
        err_simp = 2 - I_simp

        print(chr(27) + "[2J")
        print("Simpson's rule estimation with " +
              str(n) + " points: " + str(I_simp))
        print("Error: " + str(err_simp))

        n += 1
        time.sleep(0.25)


simpsons_rule()
