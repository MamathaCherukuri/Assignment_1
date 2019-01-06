#!/usr/bin/env python
# coding: utf-8

#  #Question1
# '''Install Jupyter notebook and run the first program and share the screenshot of the output.'''
# 

# In[29]:


print('Hello World')


# #Question2
# 
# '''2. Write a program which will find all such numbers which are divisible by 7 but are not a
# multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed
# in a comma-separated sequence on a single line.'''

# In[26]:



list_num=[]
for i in range(2000,3201):
    if (i%7==0) and (i%5!=0):
        list_num.append(str(i))
    
print(','.join(list_num))


# '''Question3'''Write a Python program to accept the user's first and last name and then getting them printed in the the reverse order with a space between first name and last name.'''

# In[24]:


first_name=input("Enter your First Name:")
last_name=input("Enter your Last Name:")
print(last_name+" "+first_name)


# Question4'''Write a Python program to find the volume of a sphere with diameter 12 cm.
# Formula: V=4/3 * π * r'''
# 

# In[25]:



D=float(input("Enter Diamter: "))

Pi=(22.0/7.0)
Volume=(4.0/3.0)*Pi*(D/2.0)**3
print(Volume)


# 
# 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# 

# 

# 

# 

# 

# 

# 

# 

# 
