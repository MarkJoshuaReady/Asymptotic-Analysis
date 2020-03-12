# Mark Joshua Omandam
# BSCS - II
# 2018-1607

import math
import numpy as np
import matplotlib.pyplot as plt

log = []
supLin = []
linear = []
quad = []
poly = []
expo = []


inputVal= []


def algs():
    n = 1
    x = int(input("This aims to get the answer of these algorithms in a given nth values of 'n':\n"
                  "Logarithmic algorithm – O(logn)\n"
                  "Linear algorithm – O(n)\n"
                  "Superlinear algorithm – O(nlogn)\n"
                  "Polynomial algorithm – O(n^c)\n"
                  "Exponential algorithm – O(c^n)\n\n"
                  "Enter the value of 'n': "))

    while n < x:
        inputVal.append(n)


        log.append(math.log(n, 10))
        print(math.log(n) , "O(logn)")
        print(log, 'qweqweqeqwe')

        supLin.append(n * math.log(n, 10))
        print(n * math.log(n, 10), "O(nlogn)")
        print(n * math.log(n), "O(nlogn)")

        linear.append(n)
        print(n, "O(n)")

        quad.append(n ** 2)
        print(n ** 2, "O(n^c)")

        poly.append(n ** 3)
        print(n ** 3, "O(n^c)")

        expo.append(2 ** n)
        print(2 ** n, "O(c^n")
        n += 1


algs()

fig, ax = plt.subplots()
index = np.arange(4)


plt.plot(inputVal, log, color = 'r', label='Logarithmic')
plt.plot(inputVal, supLin, color = 'g', label='Superlinear')
plt.plot(inputVal, linear, color = 'b', label='Linear')
plt.plot(inputVal, quad, color = 'y', label='Quadratic')
plt.plot(inputVal, poly, color = 'violet', label='Polynomial')
plt.plot(inputVal, expo, color = 'black', label='Exponential')
plt.xlabel('Values of n')
plt.ylabel('Result of the nth Value')
plt.title('Algorithms')
plt.legend()


plt.tight_layout()
plt.show()