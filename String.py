
# coding: utf-8

# In[22]:


#python program for checking string Pallindrome
s1="Madam"
s1=s1.lower()
s2=reversed(s1)

if list(s2)==list(s1):
    print("Palindrome")
else:
    print("Not Pallindrome")


# In[24]:


#sort words in alphabetical order
str="my name is jasjyot singh"

words=str.split()

words.sort()

for word in words:
    print(word)


# In[34]:


str1="Hello";                       '''3 ways of initalising a string in python'''
str2='Hello World'
str3='''Hello Jasjyot'''
print("{}\n{}\n{}".format(str1,str2,str3))

print(str1[0])     #string indexing
print(str1[-2])
print(str2[2:5])     #string slicing
#print(str1[10])     #index error

#str1[0]='A'          #Error as strings are immutable
del str1              #delete string

print(str2+" "+str3)
print(str2*3)

print('or' in 'Hello World')

str2=str2.lower()        #lowers all chars of string
print(str2)


str2=str2.upper()        #capitalizes all chars of string
print(str2)

str2="Beyond your greatest fear, lies the blissful experience of your life."             #splitting a string on the basis of space 
lst=str2.split()
print(lst)

str4=' '.join(lst)                   #joining a string on the basis of space.
print(str4)

print(str4.find(", lies"))            #finding the position of substring

str5=str4.replace('Beyond','Behind')    #replace does not change the original string
print("str4= ",str4)
print("str5= ",str5)

