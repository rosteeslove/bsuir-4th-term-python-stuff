"""
This module is for demo and testing purposes.
"""


import lagranges
import divdiffs_interpolation as ddi
import ls_bestapprox as lsb


xs = [0.1*i for i in range(11)]
ps = [0.0, 0.41, 0.79, 1.13, 1.46, 1.76, 2.04, 2.3, 2.55, 2.79, 3.01]

m = 1.96
ys = [p + 1.96*((-1)**k) for k, p in enumerate(ps)]

nodes = [(x, y) for x, y in zip(xs, ys)]

print(f'xs = {[round(x, 2) for x in xs]}')
print(f'ys = {[round(y, 2) for y in ys]}')

lagr_poly = lagranges.interpoly(nodes)
ddi_poly = ddi.interpoly(nodes)
lsb_poly_n1 = lsb.bestapprox_alpha(nodes, 10)
lsb_poly_n2 = lsb.bestapprox_beta(nodes, 10)

print(lagr_poly)
print(ddi_poly)
print(lsb_poly_n1)
print(lsb_poly_n2)
