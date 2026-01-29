n=int(input("enter a number:"))
def isAdam(n):
  return square(n)==reverse(square(reverse(n)))

print(isAdam(n))
