#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# ### Creating a Series
# 
# You can convert a list,numpy array, or dictionary to a Series:

# In[2]:


labels = ['a','b','c']
my_list = [10,20,30]
arr = np.array([10,20,30])
d = {'a':10,'b':20,'c':30}


# ** Using Lists**

# In[3]:


pd.Series(data=my_list)


# In[4]:


pd.Series(data=my_list,index=labels)


# In[5]:


pd.Series(my_list,labels)


# ** NumPy Arrays **

# In[6]:


pd.Series(arr)


# In[7]:


pd.Series(arr,labels)


# ** Dictionary**

# In[8]:


pd.Series(d)


# ### Data in a Series
# 
# A pandas Series can hold a variety of object types:

# In[9]:


pd.Series(data=labels)


# In[10]:


# Even functions (although unlikely that you will use this)
pd.Series([sum,print,len])


# ## Using an Index
# 
# The key to using a Series is understanding its index. Pandas makes use of these index names or numbers by allowing for fast look ups of information (works like a hash table or dictionary).
# 
# Let's see some examples of how to grab information from a Series. Let us create two sereis, ser1 and ser2:

# In[11]:


ser1 = pd.Series([1,2,3,4],index = ['USA', 'Germany','USSR', 'Japan'])                                   


# In[12]:


ser1


# In[13]:


ser2 = pd.Series([1,2,5,4],index = ['USA', 'Germany','Italy', 'Japan'])                                   


# In[14]:


ser2


# In[15]:


ser1['USA']


# Operations are then also done based off of index:

# In[16]:


ser1 + ser2

