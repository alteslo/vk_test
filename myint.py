def myint(str_int=None):

    def int_proc(str_int):
        int_map = {
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            '0': 0
        }
        razryad = (len(str_int) - 1)
        a = 0
        minus_balanser = 1
        if str_int[0] == '-':
            str_int = str_int[1:]
            minus_balanser = -1
            razryad -= 1
        for i in str_int:
            a += int_map.get(i) * 10 ** razryad
            razryad -= 1
        return a * minus_balanser

    if str_int is None:
        return 0
    elif isinstance(str_int, int):
        return str_int
    elif isinstance(str_int, float):
        num = str(str_int)
        num = num[:num.find('.')]
        return int_proc(num)
    elif isinstance(str_int, str):
        try:
            num = int_proc(str_int)
        except TypeError:
            raise ValueError(f'invalid literal for int() with base 10: {str_int}')
        return num
    else:
        raise TypeError(f'int() argument must be a string, a bytes-like object or a number, not {type(str_int).__name__}')


class A:
    pass

b = A()

print(myint('-549.889'))


# b = A()

a = int('-549.89')
print(a)
