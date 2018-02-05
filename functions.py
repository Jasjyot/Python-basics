
# coding: utf-8

# In[2]:


def print_name(name):
    print("Hello "+str(name))
print(print_name.__doc__)


# In[11]:


def print_name(name):
    '''This function prints name'''
    print("Hello "+str(name))
print(print_name.__doc__)     #returns documentation string description of function
print_name("jasjyot")


# In[12]:


# HCF of 2 nos
def hcf(num1,num2):
    min=num1
    hcf=1
    if num1>num2:
        min=num2
    for i in range(1,min+1):
        if ((num1%i==0) and (num2%i==0)):
            hcf=i
    return hcf

print(hcf(98,78))
        
    

