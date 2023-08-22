def checkPalindrome(x):
    conv_number = str(x)
    reverse_number = conv_number[::-1]
    if conv_number == reverse_number :
        return True
    else:
        return False
#print (checkPalindrome(123546))

big_palindrome = 0
a = 0
b = 0
for i in range (100,1000):
    for j in range(100,1000):
        if checkPalindrome (i*j) and i*j > big_palindrome:
            big_palindrome = i*j
            a = i
            b = j

print(big_palindrome, a, b)