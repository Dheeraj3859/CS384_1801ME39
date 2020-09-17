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
        ans=1
        for i in range(num2):
            ans = ans*num1
        return ans

def printGP(a,r,n):
    gp=[]
    for i in range(n):
        gp.append(a*power(r,i))
    return gp

def printAP(a,d,n):
    ap = []
    for i in range(n):
        ap.append(a+i*d)
    return ap

def printHP(a,d,n):
    hp = []
    for i in range(n):
        den = a+i*d;
        if den==0:
            return 0
        
        hp.append(round(1/den,3))
    return hp
