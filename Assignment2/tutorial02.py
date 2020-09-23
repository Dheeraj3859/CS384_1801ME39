# All decimal 3 places
import math
# Function to compute mean
# Function to compute sum. You cant use Python functions
def summation(first_list):
    # sum Logic
    for val in first_list:
    	if isinstance(val,int)==False and isinstance(val,float)==False:
    		return 0
    sum=0
    for val in first_list:
        sum+=val

    return round(sum,3)
def mean(first_list):
    # mean Logic
    for val in first_list:
    	if isinstance(val,int)==False and isinstance(val,float)==False:
    		return 0
    sum=summation(first_list)    		
    n=len(first_list)
    return round(sum/n,6)

def sorting(first_list):
    # Sorting Logic
    temp = first_list
    n=len(first_list)
    for i in range(n-1):
        for j in range(n-i-1):
            if temp[j]>temp[j+1]:
                temp[j],temp[j+1]=temp[j+1],temp[j]

    return temp
# Function to compute median. You cant use Python functions
def median(first_list):
    # median Logic
    for val in first_list:
    	if isinstance(val,int)==False and isinstance(val,float)==False:
    		return 0
    n=len(first_list)
    new_list=sorting(first_list)
    if n%2==0:
    	ind1=(n-1)//2
    	ind2=n//2
    	return round((new_list[ind1]+new_list[ind2])/2,2)
    else:
    	return round(new_list[n//2],6)



# Function to compute variance. You cant use Python functions
def variance(first_list):
    # variance Logic
    for val in first_list:
    	if isinstance(val,int)==False and isinstance(val,float)==False:
    		return 0
    Mean=mean(first_list)
    num=0
    n=len(first_list)
    for val in first_list:
    	num+=(val-Mean)*(val-Mean)
        

    return round(num/n,6)

# Function to compute Standard deviation. You cant use Python functions
def standard_deviation(first_list):
    # Standard deviation Logic
    for val in first_list:
    	if isinstance(val,int)==False and isinstance(val,float)==False:
    		return 0
    val=variance(first_list)
    ans=math.sqrt(val)
    return round(ans,6)

# Function to compute mse. You cant use Python functions
def mse(first_list, second_list):
    # mse Logic
    n1=len(first_list)
    n2=len(second_list)
    if n1!=n2:
    	return 0
    for v1 in first_list:
    	if isinstance(v1,int)==False and isinstance(v1,float)==False:
    		return 0
    for v2 in second_list:
    	if isinstance(v2,int)==False and isinstance(v2,float)==False:
    		return 0
    num=0
    for i in range(n1):
    	num+=(first_list[i]-second_list[i])*(first_list[i]-second_list[i])

    return round(num/n1,6)

# Function to compute RMSE. You cant use Python functions
def rmse(first_list, second_list):
    # RMSE Logic
    n1=len(first_list)
    n2=len(second_list)
    if n1!=n2:
    	return 0
    for v1 in first_list:
    	if isinstance(v1,int)==False and isinstance(v1,float)==False:
    		return 0
    for v2 in second_list:
    	if isinstance(v2,int)==False and isinstance(v2,float)==False:
    		return 0
    Mse=mse(first_list,second_list)

    return round(math.sqrt(Mse),6)





# Function to compute mae. You cant use Python functions
def mae(first_list, second_list):
    # mae Logic
    n1=len(first_list)
    n2=len(second_list)
    if n1!=n2:
    	return 0
    for v1 in first_list:
    	if isinstance(v1,int)==False and isinstance(v1,float)==False:
    		return 0
    for v2 in second_list:
    	if isinstance(v2,int)==False and isinstance(v2,float)==False:
    		return 0
    num=0
    for i in range(n1):
    	num+=abs(first_list[i]-second_list[i])

    return round(num/n1,6)


# Function to compute NSE. You cant use Python functions
def nse(first_list, second_list):
    # nse Logic
    n1=len(first_list)
    n2=len(second_list)
    if n1!=n2:
    	return 0
    for v1 in first_list:
    	if isinstance(v1,int)==False and isinstance(v1,float)==False:
    		return 0
    for v2 in second_list:
    	if isinstance(v2,int)==False and isinstance(v2,float)==False:
    		return 0
    var=variance(first_list)
    Mse=mse(first_list,second_list)
    return round(1-(Mse/var),6)


# Function to compute Pearson correlation coefficient. You cant use Python functions
def pcc(first_list, second_list):
    # nse Logic
    n1=len(first_list)
    n2=len(second_list)
    if n1!=n2:
    	return 0
    for v1 in first_list:
    	if isinstance(v1,int)==False and isinstance(v1,float)==False:
    		return 0
    for v2 in second_list:
    	if isinstance(v2,int)==False and isinstance(v2,float)==False:
    		return 0
    num=0
    mean_x=mean(first_list)
    mean_y=mean(second_list)
    for i in range(n1):
    	num+=(first_list[i]-mean_x)*(second_list[i]-mean_y)
    den1=0
    for i in range(n1):
    	den1+=(first_list[i]-mean_x)*(first_list[i]-mean_x)
    den1=math.sqrt(den1)
    den2=0
    for i in range(n2):
    	den2+=(second_list[i]-mean_y)*(second_list[i]-mean_y)
    den2=math.sqrt(den2)
    den=den1*den2

    return round(num/den,6)


# Function to compute Skewness. You cant use Python functions
def skewness(first_list):
    # Skewness Logic
    for val in first_list:
    	if isinstance(val,int)==False and isinstance(val,float)==False:
    		return 0
    var=standard_deviation(first_list)
    Mean=mean(first_list)
    num=0
    n=len(first_list)
    for val in first_list:
    	tem=(val-Mean)/var
    	num+=tem*tem*tem
    return round(num/n,6)
    


# Function to compute Kurtosis. You cant use Python functions
def kurtosis(first_list):
    # Kurtosis Logic
    for val in first_list:
    	if isinstance(val,int)==False and isinstance(val,float)==False:
    		return 0
    var=standard_deviation(first_list)
    Mean=mean(first_list)
    num=0
    n=len(first_list)
    for val in first_list:
    	tem=(val-Mean)/var
    	num+=tem*tem*tem*tem

    return round(num/n,6)



