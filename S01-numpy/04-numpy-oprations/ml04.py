#!/usr/bin/env python
# coding: utf-8

# # NumPy Operations

# ## Arithmetic
# 
# You can easily perform array with array arithmetic, or scalar with array arithmetic. Let's see some examples:

# In[1]:


import numpy as np
arr = np.arange(0,10)


# In[2]:


arr + arr


# In[3]:


arr * arr


# In[4]:


arr - arr


# In[5]:


# Warning on division by zero, but not an error!
# Just replaced with nan
arr/arr


# In[6]:


# Also warning, but not an error instead infinity
1/arr


# In[10]:


arr**3


# ## Universal Array Functions
# 
# 

# In[12]:


#Taking Square Roots
np.sqrt(arr)


# In[13]:


#Calcualting exponential (e^)
np.exp(arr)


# In[14]:


np.max(arr) #same as arr.max()


# In[15]:


np.sin(arr)


# In[16]:


np.log(arr)

