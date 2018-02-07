
# coding: utf-8

# In[3]:


'''
NumPy
* Contains many objects like float, Integers
* Basically extension to python formulti dimensional arrays
* Hardware optimized efficient operations
* scintific computing, machine learning
* Also known as array computing
'''

import numpy as np
a=np.array([1,2,3,4])                 #list is converted to numpy array
print(a)
print(type(a))


# In[5]:


print(a.ndim)                           #dimension: no of fields req for accessing a data from list
print(a.shape)                          #shape: no of enteries in each field of dimension


# In[23]:


arr=np.array([[[1,2,3],[2,3,4]],[[5,6,7],[1,5,6]]])
print(arr.shape)
print(arr.ndim)                


# In[26]:


b=np.arange(10) #numpy version of func range()
print(b) #creates a numpy array from 0 to n-1.
print(type(b)) 


# In[30]:


brr=np.linspace(1,2,6)    #linspace(start, end, no. of points between interval [start, end] )
print(brr)  #divides the distance in equal intervals


# In[35]:


c=np.ones((2,3,4))    #creates numpy array where 1 is pre assigned
crr=np.zeros((5,6,2))   #declares numpy array where 0 is pre assigned 
print("{} \n\n\n\n {}".format(c,crr))


# In[47]:


d=np.eye(3)   #eye stands for Identity matrix
print(d)


# In[49]:


drr=np.diag([4,5,69,65])  #creates 2*2 np array with given diagonal elements
print(drr)


# In[52]:


e=np.random.rand(3,3,2)    #creates array using random values for given shape
print(e)


# In[56]:


print (a.dtype)  #dtype is an attribute of numpy object
a=np.arange(10, dtype="float64")
print(a)
print(a.dtype)


# In[58]:


print(c.dtype)   #default dataypes of np_arrays formed by 'ones' and 'zeros' is 'float'
print(crr.dtype)


# In[64]:


err=np.array([1+2j,6-9j,0-1j])      #Complex datatype
print(err)
print(err.dtype)


# In[68]:


f=np.array([True,False,True])        #bool datatype
print(f.dtype)
print(f)


# In[74]:


#Multiplying with scalars
j=np.array([1,2,3,4])
print(j)
j=j+1            #adds 1 to each element
print(j)

j=j*8
print(j)         #multiplies 8 to each element

j=j-4
print(j)         #subtracts 4 from each element 

j=j/4     #divides
print(j)

j=j%5
print(j)


# In[86]:


#Logical Operations
singh1=np.array([1,2,3,-4],dtype="bool")
singh2=np.array([0,-6,-7,8],dtype="bool")
print(singh1)
print(singh2)

result=np.logical_or(singh1,singh2)
print(result)
result=np.logical_and(singh1,singh2)
print(result)


# In[91]:


a=np.arange(4)
a+=1
print(np.sin(a))
print(np.log(a))    #evaluates log base 10
print(np.exp(a))   #evaluates e^x


# In[101]:


#basic reductions

array1=np.array([1,2,3,4,5])
array2=np.array([[1,2],[1,2]])
print(array1.sum())
print(array2.sum(axis=0))    #sums col wise


# In[106]:


#min, max values
print(array1.min())
print(array1.max())

print(array1.argmin())    #returns index of max, min values
print(array1.argmax())


# In[115]:


# Array Shape manipulation
print(array2.ravel(),"\n")     #flatens the array into 1D
print(array2.T)    #Transpose

array2=array2.ravel()
array2=array2.reshape(2,2)        #brnging back to original shape
                                  #2D to 1D trnsformation
print(array2)


# In[121]:


#Sorting Data
js=np.array([[5,4,6],[2,3,2]])

# explicit sort
sj=np.sort(js,axis=1)
print(sj)

#in-place sort
js.sort(axis=1)
print(js)

