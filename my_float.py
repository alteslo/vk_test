def my_float(str_float=0.0):

    def float_proc(str_float):
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
        razryad = (len(str_float) - 1)
        a = 0
        minus_balanser = 1
        if str_float[0] == '-':
            str_float = str_float[1:]
            minus_balanser = -1
            razryad -= 1
        elif not str_float[0].isdigit():
            raise ValueError(f"could not convert string to float: {str_float}")
        for i in str_float:
            a += int_map.get(i) * 10 ** razryad
            razryad -= 1
        return a * minus_balanser

    if str_float is None:
        raise TypeError("float() argument must be a string or a number, not 'NoneType'")
    elif isinstance(str_float, int):
        return str_float * 1.0
    elif isinstance(str_float, float):
        return str_float
    elif isinstance(str_float, str):
        if str_float.count('.') == 1:
            first_num = str_float[:str_float.find('.')]
            second_num = str_float[str_float.find('.') + 1:]
            if first_num[0] == '-':
                return round(float_proc(first_num) * 1.0 - (float_proc(second_num) / 10 ** len(second_num)), 10)
            return round(float_proc(first_num) * 1.0 + (float_proc(second_num) / 10 ** len(second_num)), 10)
        elif str_float[1:].isdigit():
            return float_proc(str_float) * 1.0
        else:
            raise ValueError(f'could not convert string to float: {str_float}')
    else:
        raise ValueError(f'could not convert to float: {str_float}')


print(float(None))

a = '1234'
print(my_float(a))

# a = 'авпавыпв'
# print(my_float(a))

# a = '-598'
# print(my_float(a))


# a = '5.5'
# print(my_float(a))

# a = 'd5.5'
# print(my_float(a))

# a = []
# print(my_float(a))
 
