def function(n):
    if n<=1:
        return n
    print(n)
    return function(n-1)
def printName(s,n):
    if n<=0:
        return 
    print(s)
    printName(s,n-1)
        


if __name__ == "__main__":
   print(function(5))  
   n=int(input("Enter the number of times to print your name: "))
   printName("sathya",n)
