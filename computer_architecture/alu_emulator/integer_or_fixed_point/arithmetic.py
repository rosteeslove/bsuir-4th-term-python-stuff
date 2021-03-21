"""
Summary:
This module contains methods facilitating addition, subtraction,
multiplication and division for 2s-complement binary strings.
"""


import basic_operations as basic
import binary_string_io as bsio


def _align(a, b):
    """
    Return a tuple of a-arg and b-arg binary strings but
    changed so that their size equals to the size of the bigger one.
    """
    if len(a) < len(b):
        a = basic.expand_to_len(a, len(b))
    elif len(a) > len(b):
        b = basic.expand_to_len(b, len(a))

    return a, b


def sum(a, b, rus_output=False):
    """
    Return sum of 2 two's complement binary strings
    and the error bool*.

    * - True if there's an error.
    """
    bigger_len = len(a) if len(a) > len(b) else len(b)
    a = basic.expand_to_len(a, bigger_len)
    b = basic.expand_to_len(b, bigger_len)

    if rus_output:
        print(('Считаем сумму следующих чисел в дополнительном коде:\n'
               '{0}(2) = {1}(10)\n'
               '{2}(2) = {3}(10)\n'
               ).format(a, bsio.twos_comp_binary_string_to_int(a),
                        b, bsio.twos_comp_binary_string_to_int(b)))
        print('Она соответствует сумме в прямом коде, поэтому...\n')

    a_sign = a[0]
    b_sign = b[0]

    error_bool = False
    c = basic.sum(a, b, rus_output)[0]
    if a_sign == b_sign and c[0] != a_sign:
        error_bool = True

    if rus_output:
        print(('\n'
               'Результат суммы в дополнительном коде:\n'
               'a + b = c\n'
               'a = {0}(2) = {1}(10)\n'
               'b = {2}(2) = {3}(10)\n'
               'c = {4}(2) = {5}(10)\n'
               'Переполнение для дополнительного кода '
               + ('есть' if error_bool else 'отсутствует') + '.'
              ).format(a, bsio.twos_comp_binary_string_to_int(a),
                       b, bsio.twos_comp_binary_string_to_int(b),
                       c, bsio.twos_comp_binary_string_to_int(c)))
    
    return c, error_bool


def dif(a, b, rus_output=False):
    """
    Return the difference between a-arg and b-arg 2s-complement
    binary strings.
    """
    a, b = _align(a, b)
    nb = basic.neg(b)

    if rus_output:
        print(('Считаем разность следующих чисел в дополнительном коде:\n'
               '{0}(2) = {1}(10)\n'
               '{2}(2) = {3}(10)\n'
               ).format(a, bsio.twos_comp_binary_string_to_int(a),
                        b, bsio.twos_comp_binary_string_to_int(b)))
        print('Она соответствует сумме первого '
              'и отрицания второго, поэтому...')
        print(('Отрицание второго числа:\n{0}, ошибка {1}.\n'
              ).format(nb[0], 'есть' if nb[1] else 'отсутствует'))

    c = sum(a, nb[0], rus_output)

    if rus_output:
        print('Результат разности соответствует '
              'результату суммы в дополнительном коде.')

    return c


def mul(a, b):
    """
    Return the unsigned product
    of a-arg and b-arg unsigned binary strings.

    Remark: the product is of the same bit number
    as the bigger argument so this method is to be used
    with small numbers to avoid overflows.
    """
    p = '0'
    a, b = _align(a, b)

    for bit in reversed(a):
        if bit == '1':
            p = basic.sum(p, b)
        b = basic.shift_left(b)

    return p


def full_mul(a, b):
    """
    Returns the unsigned product of a-arg and b-arg unsigned 
    binary strings.
    """
    p = '0'

    for bit in reversed(a):
        if bit == '1':
            p = basic.sum(p, b)
        b += '0'

    return p


def imul(m, r, rus_output=False):
    """
    Return the product of m-arg and r-arg
    interpreting them as 2s-complement binary strings.

    Remark: the Booth's algorithm is used 
    (https://en.wikipedia.org/wiki/Booth%27s_multiplication_algorithm).
    """
    if rus_output:
        print('Перемножим следующие числа в дополнительном коде '
              'по алгоритму Бута:')
        print('m = {0}(2) = {1}(10)'.format(m,
               bsio.twos_comp_binary_string_to_int(m)))
        print('r = {0}(2) = {1}(10)\n'.format(r,
               bsio.twos_comp_binary_string_to_int(r)))

    x = len(m)
    y = len(r)
      
    m = m[0] + m

    A = m + (y+1)*'0'
    S = basic.neg(m)[0] + (y+1)*'0'
    P = '0' + x*'0' + r + '0'

    if rus_output:
        print('Установим значения регистров A, S и P:\n'
              + 'A = {0} {1} {2} {3}\n'.format(A[0], A[1:(x+1)],
                                               A[(x+1):(x+y+1)], A[-1])
              + 'S = {0} {1} {2} {3}\n'.format(S[0], S[1:(x+1)],
                                               S[(x+1):(x+y+1)], S[-1])
              + 'P = {0} {1} {2} {3}\n'.format(P[0], P[1:(x+1)],
                                               P[(x+1):(x+y+1)], P[-1]))
    if rus_output:
        print('P:')
    for _ in range(y):
        two_last_bits_of_p = P[-2:]

        if two_last_bits_of_p == '01':
            P = basic.sum(A, P)[0]
        elif two_last_bits_of_p == '10':
            P = basic.sum(S, P)[0]

        P = basic.arithmetic_shift_right(P)
        if rus_output:
            print('{0} {1} {2} {3}'.format(P[0], P[1:(x+1)],
                                           P[(x+1):(x+y+1)], P[-1]))

    if rus_output:
        print('\nОтбрасываем крайние биты. Результат умножения:\n'
              + 'm * r = {0}(2) = {1}(10)'.format(P[1:-1],
                  bsio.twos_comp_binary_string_to_int(P[1:-1])))

    return P[1:-1]


def idiv(a, b, rus_output=False):
    """
    Return tuple of quotient and remainder of a-arg / b-arg
    as well as boolean indicating whether an error has occured.

    Remark: a-arg and b-arg are 2s-complement binary strings.

    Another remark:
    (here I am using python int variables and binary string variables
    interchangeably since any one of the former type corresponds to
    the one of the latter)

    Let's say q, r = idiv(a, b).

    Well, while a is indeed equal to q*b + r,
    q is not necessary a // b and r is not necessary a % b.
    """
    if rus_output:
        print('Поделим следующие числа в дополнительном коде:')
        print('a = {0}(2) = {1}(10)'.format(a,
            bsio.twos_comp_binary_string_to_int(a)))
        print('b = {0}(2) = {1}(10)\n'.format(b,
            bsio.twos_comp_binary_string_to_int(b)))

    if bsio.twos_comp_binary_string_to_int(b) == 0:
        print('Ошибка: деление на ноль.')
        raise ZeroDivisionError

    a, b = _align(a, b)
    M = b
    AQ = basic.expand_to_len(a, len(a)*2)
    A, Q = AQ[:len(a)], AQ[-len(a):]

    if rus_output:
        print('Установим значения регистров A, Q и M:')
        print('A: {0}'.format(A))
        print('Q: {0}'.format(Q))
        print('M: {0}\n'.format(M))

        print('A:' + ' '*(len(A) - 2) + ' Q:\n')

    for _ in range(len(a)):
        AQ = basic.shift_left(A + Q)
        A, Q = AQ[:len(a)], AQ[-len(a):]

        old_A = A
        if M[0] == A[0]:
            A = dif(A, M)[0]
        else:
            A = basic.sum(A, M)[0]

        if old_A[0] == A[0] or A == Q == basic.expand_to_len('0', len(A)):
            Q = Q[:-1] + '1'
        else:
            Q = Q[:-1] + '0'
            A = old_A

        if rus_output:
            print('{0} {1}'.format(A, Q))

    r = A
    q = Q if a[0] == b[0] else basic.neg(Q)[0]

    if rus_output:
        print('')
    error_bool = False
    if basic.neg(Q)[1]:
        error_bool = True
        if rus_output:
            print('Произошло переполнение.')

    if rus_output:
        print('Результат деления:\n'
              + 'q = {0}(2) = {1}(10)\n'.format(q,
                  bsio.twos_comp_binary_string_to_int(q))
              + 'r = {0}(2) = {1}(10)'.format(r,
                  bsio.twos_comp_binary_string_to_int(r)))
                  
    return q, r, error_bool
