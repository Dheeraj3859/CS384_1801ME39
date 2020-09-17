# Function to add two numbers 
def add(num1, num2): 
	addition = num1 + num2
	return addition

# Function to subtract two numbers 
def subtract(num1, num2): 
	subtraction = num1 - num2
	return subtraction

# Function to multiply two numbers 
def multiply(num1, num2): 
	#Multiplication Logic 
	return num1*num2

# Function to divide two numbers 
def divide(num1, num2): 
	#DivisionLogic
        if num2==0:
            return 0
        else:
            return num1/num2
# Function to add power function
#You cant use the inbuilt python function x ** y . Write your own function
def power(num1, num2): #num1 ^ num2
	#DivisionLogic
        flag=0
        if num2<0:
            flag=1
            num2=num2*-1
        num2 = int(num2)
        if num1==0:
            return 0
        ans=1
        for i in range(num2):
            ans = ans*num1
        if flag==1:
            return 1/ans
        else:
            return ans

def printGP(a,r,n):
    gp=[]
    if isinstance(n,float):
        n = int(n)
    for i in range(n):
        gp.append(a*power(r,i))
    return gp

def printAP(a,d,n):
    ap = []
    if isinstance(n,float):
        n = int(n)
    for i in range(n):
        ap.append(a+i*d)
    return ap

def printHP(a,d,n):
    hp = []
    if isinstance(n,float):
        n = int(n)
    for i in range(n):
        den = a+i*d;
        if den==0:
            return 0
        
        hp.append(round(1/den,3))
    return hp

print(power(5,-2))
