#!/usr/bin/env python
# coding: utf-8

# ## Using NumPy
# 
# Once you've installed NumPy you can import it as a library:

# In[1]:


import numpy as np


# In[2]:


my_list = [1,2,3]
my_list


# In[3]:


np.array(my_list)


# In[4]:


my_matrix = [[1,2,3],[4,5,6],[7,8,9]]
my_matrix


# In[5]:


np.array(my_matrix)


# ## Built-in Methods
# 
# There are lots of built-in ways to generate Arrays

# ### arange
# 
# Return evenly spaced values within a given interval.

# In[6]:


np.arange(0,10)


# In[7]:


np.arange(0,11,2)


# ### zeros and ones
# 
# Generate arrays of zeros or ones

# In[8]:


np.zeros(3)


# In[9]:


np.zeros((5,5))


# In[10]:


np.ones(3)


# In[11]:


np.ones((3,3))


# ### linspace
# Return evenly spaced numbers over a specified interval.

# In[29]:


np.linspace(0,10,3)


# In[31]:


np.linspace(0,10,50)


# ## eye
# 
# Creates an identity matrix

# In[37]:


np.eye(4)


# ## Random 
# 
# Numpy also has lots of ways to create random number arrays:
# 
# ### rand
# Create an array of the given shape and populate it with
# random samples from a uniform distribution
# over ``[0, 1)``.

# In[47]:


np.random.rand(2)


# In[46]:


np.random.rand(5,5)


# ### randn
# 
# Return a sample (or samples) from the "standard normal" distribution. Unlike rand which is uniform:

# In[48]:


np.random.randn(2)


# In[45]:


np.random.randn(5,5)


# ### randint
# Return random integers from `low` (inclusive) to `high` (exclusive).

# In[13]:


np.random.randint(1,100)


# In[51]:


np.random.randint(1,100,10)


# ## Array Attributes and Methods
# 
# Let's discuss some useful attributes and methods or an array:

# In[55]:


arr = np.arange(25)
ranarr = np.random.randint(0,50,10)


# In[56]:


arr


# In[57]:


ranarr


# ## Reshape
# Returns an array containing the same data with a new shape.

# In[54]:


arr.reshape(5,5)


# ### max,min,argmax,argmin
# 
# These are useful methods for finding max or min values. Or to find their index locations using argmin or argmax

# In[64]:


ranarr


# In[61]:


ranarr.max()


# In[62]:


ranarr.argmax()


# In[63]:


ranarr.min()


# In[60]:


ranarr.argmin()


# ## Shape
# 
# Shape is an attribute that arrays have (not a method):

# In[65]:


# Vector
arr.shape


# In[66]:


# Notice the two sets of brackets
arr.reshape(1,25)


# In[69]:


arr.reshape(1,25).shape


# In[70]:


arr.reshape(25,1)


# In[76]:


arr.reshape(25,1).shape


# ### dtype
# 
# You can also grab the data type of the object in the array:

# In[75]:


arr.dtype

