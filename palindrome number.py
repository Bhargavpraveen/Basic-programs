def palindrome():
    n=input('Enter any number: ')
    return 'Palindrome' if n[::-1]==n else 'Not a palindrome'
print(palindrome())
