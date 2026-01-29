"""write a program to find the reverse of the given number"""

def reverse(num):
    rev = 0
    while num > 0:
        rev = rev * 10 + num % 10
        num = num // 10
    return rev

def ispalindrome(num):
    return num == reverse(num)


print(reverse(123789))        # 321

print(reverse(123456))        # 321

print(ispalindrome(123))  # False
print(reverse(121))        # 121
print(ispalindrome(121))  # True
