def swap_with_variable(n1,n2):
    print(f'Initially n1 is {n1} and n2 is {n2}')
    v=n1
    n1=n2
    n2=v
    return f'After swapping n1 is {n1} and n2 is {n2}'
print(swap_with_variable(100,200))


def swap_without_variable(n1,n2):
    print(f'Initially n1 is {n1} and n2 is {n2}')
    n1,n2=n2,n1
    return f'After swapping n1 is {n1} and n2 is {n2}'
print(swap_without_variable(223,224))
