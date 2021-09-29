def prime_checker():
    n=int(input('Enter the Number to check: '))
    if n==1:
        return 'Not a Prime'
    return 'Not a Prime Number' if any([n%i==0 for i in range(2,n)])==True else 'Prime Number'
print(prime_checker())

