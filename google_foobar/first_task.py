"""
A quickly compiled script to compare algorithm variations for the
first task of google foobar challenge.


The task is:

input: integer number n between 1 and 1_000_000. 
output: the list of [square numbers]* such that their sum equals n.


* https://math.wikia.org/wiki/Square_number#:~:text=In%20mathematics%2C%20a%20square%20number,written%20as%203%20%C3%97%203.
"""


import math
import time

from matplotlib import pyplot as plt


def solution1(n):
    """
    The solution I submitted.
    """
    res = []
    while n > 0:
        m = int(math.floor(math.sqrt(n))**2)
        res.append(m)
        n -= m
    return res


def solution2(n):
    """
    The same as above but recursive hence slower a bit.
    """
    if n == 0:
        return []
    m = int(math.floor(math.sqrt(n))**2)
    return [m] + solution2(n - m)


def solution3(n):
    """
    The second thought solution I came up with after the submission.
    """
    res = []
    while n > 0:
        m = int(math.sqrt(n))**2
        res.append(m)
        n -= m
    return res


def main():
    ran = range(1, 100000002, 100)
    sols1 = []
    sols2 = []
    sols3 = []

    time1 = time.time()
    for i in ran:
        solution1(i)
        time2 = time.time()
        sols1.append(time2-time1)

    time1 = time.time()
    for i in ran:
        solution2(i)
        time2 = time.time()
        sols2.append(time2-time1)

    time1 = time.time()
    for i in ran:
        solution3(i)
        time2 = time.time()
        sols3.append(time2-time1)

    print(solution1(12))
    print(solution2(12))
    print(solution3(12))

    plt.plot(ran, sols1, label='The submitted one')
    plt.plot(ran, sols2, label='The submitted one but recursive')
    plt.plot(ran, sols3, label='The second thought solution')

    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
