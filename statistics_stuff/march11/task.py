import math
from random import seed
from random import random
import matplotlib.pyplot as plt

seed(69)
n = 0
k = 0

while True:
    m = 0
    for i in range(100):
        if random() < 0.8:
            m += 1

    if m >= 75 and m <= 90:
        k += 1

    n += 1

    if n % 1000000 == 0:
        print(k / n)
