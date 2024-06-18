def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()

print_params(1, 25, )
print_params(1, 'строка', c=[123])

values_list = [1, 'не цифра', True]
values_dict = {'a': 1, 'b': 'строка', 'c': True}
print()

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [69.21, 'не число']
print_params(*values_list_2)