# All decimal 3 places

# Function to compute mean
def mean(first_list):
    # mean Logic
    sum=0
    for i in first_list:
    	if isinstance(i,int)==False and isinstance(i,float)==False:
    		return 0
    	else:
    		sum=sum+i
    n=len(first_list)
    return round(sum/n,3)


# Function to compute median. You cant use Python functions
def median(first_list):
    # median Logic
    for val in first_list:
    	if isinstance(val,int)==False and isinstance(val,float)==False:
    		return 0
    n=len(first_list)
    for i in range(n-1):
        for j in range(n-i-1):
            if first_list[j]>first_list[j+1]:
                first_list[j],first_list[j+1]=first_list[j+1],first_list[j]


    return round(first_list[n/2],3)



# Function to compute variance. You cant use Python functions
def variance(first_list):
    # variance Logic
    Mean=mean(first_list)
    num=0
    n=len(first_list)
    for val in first_list:
    	if isinstance(val,int) or isinstance(val,float):
    		num=num+(val-Mean)*(val-Mean)
    	else:
    		return 0
        

    return round(num/n,3)

# Function to compute Standard deviation. You cant use Python functions
def standard_deviation(first_list):
    # Standard deviation Logic
    for val in first_list:
    	if isinstance(val,int)==False and isinstance(val,float)==False:
    		return 0
    val=variance(first_list)
    ans=sqrt(val)
    return round(ans,3)


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
    num=0
    for i in range(n1):
    	num=num+(first_list[i]-second_list[i])*(first_list[i]-second_list[i])

    return round(sqrt(num/n1),3)


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
    val = rmse(first_list,second_list)
    return round(val*val,3)


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
    	num=num+abs(first_list[i]-second_list[i])

    return round(num/n1,3)


# Function to compute NSE. You cant use Python functions
def nse(first_list, second_list):
    # nse Logic
    return nse_value


# Function to compute Pearson correlation coefficient. You cant use Python functions
def pcc(first_list, second_list):
    # nse Logic
    return pcc_value


# Function to compute Skewness. You cant use Python functions
def skewness(first_list):
    # Skewness Logic
    return skewness_value
    
def sorting(first_list):
    # Sorting Logic
    temp = first_list
    n=len(first_list)
    for i in range(n-1):
        for j in range(n-i-1):
            if temp[j]>temp[j+1]:
                temp[j],temp[j+1]=temp[j+1],temp[j]

    return temp

# Function to compute Kurtosis. You cant use Python functions
def kurtosis(first_list):
    # Kurtosis Logic
    return kurtosis_value


# Function to compute sum. You cant use Python functions
def summation(first_list):
    # sum Logic
    for val in first_list:
    	if isinstance(val,int)==False and isinstance(val,float)==False:
    		return 0
    sum=0
    for val in first_list:
        sum=sum+val

    return sum
