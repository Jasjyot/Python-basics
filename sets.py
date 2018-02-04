
# coding: utf-8

# In[3]:


set1={1,2,3,4,5} #create set
set2=set([4,5,6,7,8,9]) #we can make set from list also
print('{}\n{}'.format(set1,set2))


# In[4]:


set3={}
print(type(set3))  #dict

set4=set()         #proper method to initialize emty set.
print(type(set4))    #set


# In[5]:


print(set1)
set1.add(0) #add elements to set
print(set1)


# In[6]:


set1.update([0.1,0.2,0.3,0.4]) #add multiple elements to set
print(set1)


# In[13]:


set1.update([1,1.1,1.2],[2.1,2.2,2.3],{2.6,2.7})   #update() is meant for only iterable objects which can store multiple data
#set1.update(1,2,3)  #error: 'int' object is not iterable  
print(set1)


# In[21]:


set1.discard(0.1) #discards 1 element at a time
set1.discard(10)  #does not produce error if the argument to function is not present in set 
print(set1)


# In[22]:


set1.remove(0.3) #removes one element at time
#set1.remove(10)  #produces error if the argument to function is not present in set
print(set1)


# In[23]:


set1.pop() #removes random element
print(set1)


# In[24]:


set1.clear() #removes all items of set
print(set1)


# In[30]:


set1.update([1,2,3,4,5])

print(set1|set2) #union
print(set1.union(set2))

print(set1&set2)   #intersection
print(set1.intersection(set2))

print(set1-set2)    #difference
print(set1.difference(set2))

print(set1^set2)    #symmetric difference: (set1 | set2)- (set1 & set2)
print(set1.symmetric_difference(set2))


# In[32]:


set3={1,2,3}
print(set3.issubset(set1))  


# In[35]:


set5=set()
set6=frozenset()

#sets cannot be used as keys in dict as they are mutable, hence unhashable
#frozen sets are immutable and therefore hashable

dict={set6:'Hello'}
print(dict[set6])

#dict={set5:'Hello'}    #error
#print(dict[set5])

