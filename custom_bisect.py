from bisect import bisect_left
from random import choices, choice
 

def bisect_left_custom(lst: list, target) -> int:
    if target <= lst[0]:
        return 0
    s, e = 0, len(lst)
    while(e-s>1):
        if target <= (val := lst[(mid:=s + (e-s)//2)]):
            e = mid
        else:
            s = mid
    return e

a = [1, 2, 4, 4, 4]
tar = 4




# print(bisect_left(a, tar))
# print(bisect_left_custom(a, tar))


def bisect_test(bisect_func_cust: callable, bisect_func_lib: callable,  tests_count = 100):
    for i in range(tests_count):
        lst = sorted(choices(range(1,10), k=15))
        tar = choice(lst)
        if not (cust_bis := bisect_func_cust(lst, tar)) == (lib_bis := bisect_func_lib(lst, tar)):
            print('='*120 + '\n' + f'Ошибка {i}: {lst} \n<<>> tar = {tar}')
            print(f'custom -> {cust_bis}   lib_bis -> {lib_bis}')


bisect_test(bisect_left_custom, bisect_left)
print('sadfsadfad')













