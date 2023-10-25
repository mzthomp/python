
integer_value = int(input())
while integer_value > 0:
    p = integer_value % 2
    print(p, end='')
    integer_value = integer_value // 2
