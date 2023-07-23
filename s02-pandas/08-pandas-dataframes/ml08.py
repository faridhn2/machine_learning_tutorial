#!/usr/bin/env python
# coding: utf-8

# # DataFrames
# 
# DataFrames are the workhorse of pandas and are directly inspired by the R programming language. We can think of a DataFrame as a bunch of Series objects put together to share the same index. Let's use pandas to explore this topic!

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


from numpy.random import randn
np.random.seed(101)


# In[3]:


df = pd.DataFrame(randn(5,4),index='A B C D E'.split(),columns='W X Y Z'.split())


# In[186]:


df


# ## Selection and Indexing
# 
# Let's learn the various methods to grab data from a DataFrame

# In[4]:


df['W']


# In[5]:


# Pass a list of column names
df[['W','Z']]


# In[6]:


# SQL Syntax (NOT RECOMMENDED!)
df.W


# DataFrame Columns are just Series

# In[7]:


type(df['W'])


# **Creating a new column:**

# In[8]:


df['new'] = df['W'] + df['Y']


# In[9]:


df


# ** Removing Columns**

# In[10]:


df.drop('new',axis=1)


# In[11]:


# Not inplace unless specified!
df


# In[12]:


df.drop('new',axis=1,inplace=True)


# In[13]:


df


# Can also drop rows this way:

# In[14]:


df.drop('E',axis=0)


# ** Selecting Rows**

# In[15]:


df.loc['A']


# Or select based off of position instead of label 

# In[16]:


df.iloc[2]


# ** Selecting subset of rows and columns **

# In[17]:


df.loc['B','Y']


# In[18]:


df.loc[['A','B'],['W','Y']]


# ### Conditional Selection
# 
# An important feature of pandas is conditional selection using bracket notation, very similar to numpy:

# In[19]:


df


# In[20]:


df>0


# In[21]:


df[df>0]


# In[22]:


df[df['W']>0]


# In[23]:


df[df['W']>0]['Y']


# In[24]:


df[df['W']>0][['Y','X']]


# For two conditions you can use | and & with parenthesis:

# In[25]:


df[(df['W']>0) & (df['Y'] > 1)]


# ## More Index Details
# 
# Let's discuss some more features of indexing, including resetting the index or setting it something else. We'll also talk about index hierarchy!

# In[26]:


df


# In[27]:


# Reset to default 0,1...n index
df.reset_index()


# In[28]:


newind = 'CA NY WY OR CO'.split()


# In[29]:


df['States'] = newind


# In[30]:


df


# In[214]:


df.set_index('States')


# In[31]:


df


# In[216]:


df.set_index('States',inplace=True)


# In[33]:


df


# ## Multi-Index and Index Hierarchy
# 
# Let us go over how to work with Multi-Index, first we'll create a quick example of what a Multi-Indexed DataFrame would look like:

# In[34]:


# Index Levels
outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)


# In[35]:


hier_index


# In[36]:


df = pd.DataFrame(np.random.randn(6,2),index=hier_index,columns=['A','B'])
df


# Now let's show how to index this! For index hierarchy we use df.loc[], if this was on the columns axis, you would just use normal bracket notation df[]. Calling one level of the index returns the sub-dataframe:

# In[37]:


df.loc['G1']


# In[263]:


df.loc['G1'].loc[1]


# In[265]:


df.index.names


# In[266]:


df.index.names = ['Group','Num']


# In[267]:


df


# In[270]:


df.xs('G1')


# In[271]:


df.xs(['G1',1])


# In[273]:


df.xs(1,level='Num')

