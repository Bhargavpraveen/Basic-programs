def fibonacci():
    n=int(input('How many fibonacci terms do you want to display ? '))
    a,b,lst=0,1,[]
    for _ in range(n):
        lst.append(a)
        a,b=b,a+b
    return lst
print(fibonacci())
