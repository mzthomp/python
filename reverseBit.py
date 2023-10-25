def int_to_reverse_binary(integer_value):
    input_string = ''
    while integer_value > 0:
       p = integer_value % 2
       input_string = input_string + str(p)
       integer_value = integer_value // 2
    return input_string


def string_reverse(input_string):
    reverse_string = input_string[::-1]
    return reverse_string

integer_value = int(input())

a = int_to_reverse_binary(integer_value)
b = string_reverse(a)
print(a)
print(b)


