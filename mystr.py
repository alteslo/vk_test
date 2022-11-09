def mystr(int_str=None):

    def str_proc(int_str):
        int_map = {
            1: '1',
            2: '2',
            3: '3',
            4: '4',
            5: '5',
            6: '6',
            7: '7',
            8: '8',
            9: '9',
            0: '0'
        }

        summa = 0
        input_str = int_str
        output_str = ''
        if input_str < 0:
            input_str *= -1
            int_str *= -1
            output_str = '-'
        while int_str:
            summa += 1
            int_str = int_str // 10
        for i in range((summa - 1), 0, -1):
            num = input_str // 10 ** i
            output_str += int_map.get(num)
            input_str = input_str % 10 ** i
        return output_str + int_map.get(input_str % 10)

    if int_str is None:
        return ''
    elif isinstance(int_str, int):
        return str_proc(int_str)
    elif isinstance(int_str, float):
        a = str_proc(int(int_str))
        b = round(int_str % 1, 10)
        while b % 1 != 0:
            b *= 10
        return a + '.' + str_proc(b)
    elif isinstance(int_str, str):
        return int_str
    else:
        return int_str.__str__()

# print(type(str(5)))

class A:
    pass

b = A()


print(mystr(3, 4))

# print(str(543, 3))
