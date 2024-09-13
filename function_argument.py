# '''Variable-length arguments'''
# # their are two tyes of variable-length arguments
# # 1. Arbitrary Arguments (tuple)
# # 2. Keyword Arbitrary Arguments (dictionary)

def average (*numbers):
    sum=0
    for i in numbers:
      sum=sum+i
    print("average is: ",sum/len(numbers))
average(12,8,10,5,4)

#Keyword Arbitrary Arguments
def name(**name):
    print("Hello,", name["fname"], name["mname"], name["lname"])
name(mname = "Buchanan", lname = "Barnes", fname = "James")

"""default argument"""

# When you create a function in Python, you can define default values for some or all of the parameters. 
# These default values are used by the function if no value is provided for those parameters during the function call

def addition(a=0,b=9):  #a and b is consider as a default value
    c=a+b
    print(c)
addition()  #this the actual value.. if this value is not given then the function consider a default value as a actual value
#and when the actual value is given and default also then function consider a actual value it overide the default value 
#default is considered when actual value is not given
def addition(a=0,b=9): 
    c=a+b
    print(c)
addition(2,3)


# '''keyword argument'''
def addition(a=3,b=4):
    c=a+b
    print(c)
addition(b=1,a=2)

# """required argument"""
def addition(a=9,b=9,c=9): #parameter
    d=a+b+c
    print(d)
addition()  #argument  
#argument utna hi hona chahiye jitna parameter hai agar argument ki value parameter se jayada hue tb error hoga

# '''return Statement
# The return statement is used to return the value of the expression back to the calling function'''

def average (*numbers):
    sum=0
    for i in numbers:
      sum=sum+i
    #print("average is: ",sum/len(numbers))
    return sum/len(numbers)
c= average(12,8,10,5,4)
print(c)

"""required argument"""
def addition(a=9,b=9,c=9):
    return (a+b+c)
print(addition(3,5))