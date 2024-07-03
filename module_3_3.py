def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)
# print_params()
# print_params(b = 25)
# print_params(c = [1,2,3])
values_list = [5, 'fefe', False]
values_dict = {'a' : 5 , 'b' : 'fefe', 'c' : False }
values_list_2 = [4 , 'gui']
print_params(*values_list_2, 44)
# print_params(*values_list)
# print_params(**values_dict)