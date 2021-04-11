"""
This module contains interpoly function to produce Lagrange's
interpolation polynomial for a list of interpolation nodes.
"""


from polynomial import Polynomial


def interpoly(nodes) -> Polynomial:
    """
    Return interpolation polynomial for a list of
    interpolation nodes.
    """
    omega = Polynomial(1)

    for node in nodes:
        omega *= Polynomial(1, -node[0])

    omegajs = [(omega/Polynomial(1, -node[0]))[0] for node in nodes]
    small_ls = [(oj/oj(node[0]))[0] for (oj, node) in zip(omegajs, nodes)]

    interpolynomial = Polynomial(0)
    for small_l, node in zip(small_ls, nodes):
        interpolynomial += small_l*node[1]

    return interpolynomial
