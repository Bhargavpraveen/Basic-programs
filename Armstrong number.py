def armstrong_number():
    n=input('Enter any number to check: ')
    add=sum([int(i)**3 for i in n])
    return 'Armstrong Number' if str(add)==n else 'Not an Armstrong Number'
print(armstrong_number())
