def second_smallest_largest(arr):
    arr=sorted(set(arr))
    return f'Second small is {arr[1]} and Second largest is {arr[-2]}'
print(second_smallest_largest([3,5,1,6,7,2,2,1,7,6]))
