
# coding: utf-8

# In[1]:


import numpy            #imports a particuluar module


# In[2]:


import math            #To use a particular function of a module- syntax: "module_name.func_name()"
print(math.pi)


# In[4]:


import datetime                                
print(datetime.datetime.now())


# In[5]:


import math as m            #use 'as' keyword in order to avoid long names
print(m.pi)


# In[6]:


#import specific names from module without importing module as whole
from datetime import datetime 
print(datetime.now())


# In[8]:


#equivalent to importing the entire package
from math import *
print(math.pi)


# In[9]:


#list all name in a module
print(dir(numpy))


# In[10]:


#find the functionality of an unknown function in a module
print(numpy.memmap.__doc__)

