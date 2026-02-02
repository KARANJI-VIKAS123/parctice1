"""write a program to find the reverse of the given number"""
num=int(input("enter a number"))
rev=0
while(num>0):
    rev=rev*10+num%10
    num=num//10
print("reverse number is:",rev)

"""story-19"""
x=10
y=30
z=x+y