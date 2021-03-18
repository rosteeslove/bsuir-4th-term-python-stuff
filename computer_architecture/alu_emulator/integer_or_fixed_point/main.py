import binary_string_io as bin_str_io
import basic_operations as basic
import arithmetic as arithm


def main():
    """
    # tests:
    for i in range(-128, 128):
        for j in range(-128, 128):
            i_str = bin_str_io.int_to_twos_comp_binary_string(i)
            j_str = bin_str_io.int_to_twos_comp_binary_string(j)

            # imul:
            prod_str = arithm.imul(i_str, j_str)
            prod = bin_str_io.twos_comp_binary_string_to_int(prod_str)

            if prod != i*j:
                print('error: {0}*{1} = {2}'.format(i, j, prod))

            # idiv:
            if j == 0:
                continue

            q_str, r_str = arithm.idiv(i_str, j_str)
            q = bin_str_io.twos_comp_binary_string_to_int(q_str)
            r = bin_str_io.twos_comp_binary_string_to_int(r_str)

            if i != q*j + r:
                print('error: {0}/{1} = {2} ({3})'.format(i, j, q, r))
    """

    # operations test:
    print('Sum:\n')

    a = int(input('\tFirst arg: '))
    b = int(input('\tSecond arg: '))

    a_str = bin_str_io.int_to_twos_comp_binary_string(a)
    b_str = bin_str_io.int_to_twos_comp_binary_string(b)

    print('First arg + second arg = {0}'.format(
        bin_str_io.twos_comp_binary_string_to_int(basic.sum(a_str, 
                                                            b_str, 
                                                            True))))


    print('Difference:\n')

    a = int(input('\tFirst arg: '))
    b = int(input('\tSecond arg: '))

    a_str = bin_str_io.int_to_twos_comp_binary_string(a)
    b_str = bin_str_io.int_to_twos_comp_binary_string(b)

    print('First arg - second arg = {0}'.format(
        bin_str_io.twos_comp_binary_string_to_int(arithm.dif(a_str, 
                                                           b_str, 
                                                           True))))


    print('Multiplication:\n')

    a = int(input('\tFirst arg: '))
    b = int(input('\tSecond arg: '))

    a_str = bin_str_io.int_to_twos_comp_binary_string(a)
    b_str = bin_str_io.int_to_twos_comp_binary_string(b)

    print('First arg * second arg = {0}'.format(
        bin_str_io.twos_comp_binary_string_to_int(arithm.imul(a_str, 
                                                            b_str, 
                                                            True))))


    print('Division:\n')

    a = int(input('\tFirst arg: '))
    b = int(input('\tSecond arg: '))

    a_str = bin_str_io.int_to_twos_comp_binary_string(a)
    b_str = bin_str_io.int_to_twos_comp_binary_string(b)

    div_res = arithm.idiv(a_str, b_str, True)
    print(('First arg / second arg = {0}\n'
           r'First arg % second = {1}').format(
               bin_str_io.twos_comp_binary_string_to_int(div_res[0]),
               bin_str_io.twos_comp_binary_string_to_int(div_res[1])))
  

if __name__ == "__main__":
    main()
