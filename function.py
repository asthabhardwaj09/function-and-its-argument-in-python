'''We use FUNCTION because when we have to write the same line of code than instead of using the same line number
of time we use a function and simply call that function
'''
def calculateaddition(a,b):
    c=a+b
    print(c)
def isgreater(a,b):
    if(a>b):
        print("a is greater")
    else:
        print("b is greater")
def issmaller(a,b):
    pass             #we use pass if for a certain time we do not want to use or write that code ,so we pass it
    
    
a=int(input("enter the a value: "))
b=int(input("enter the b value: "))
calculateaddition(a,b)
isgreater(a,b)

def name(fname, lname):
    print("Hello,", fname, lname)

name("Sam", "Wilson")


