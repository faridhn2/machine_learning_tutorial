#!/usr/bin/env python
# coding: utf-8

# # Groupby
# 
# The groupby method allows you to group rows of data together and call aggregate functions

# In[1]:


import pandas as pd
# Create dataframe
data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
       'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
       'Sales':[200,120,340,124,243,350]}


# In[2]:


df = pd.DataFrame(data)


# In[3]:


df


# ** Now you can use the .groupby() method to group rows together based off of a column name. For instance let's group based off of Company. This will create a DataFrameGroupBy object:**

# In[4]:


df.groupby('Company')


# You can save this object as a new variable:

# In[5]:


by_comp = df.groupby("Company")


# And then call aggregate methods off the object:

# In[6]:


by_comp.mean()


# In[37]:


df.groupby('Company').mean()


# More examples of aggregate methods:

# In[7]:


by_comp.std()


# In[8]:


by_comp.min()


# In[9]:


by_comp.max()


# In[10]:


by_comp.count()


# In[11]:


by_comp.describe()


# In[12]:


by_comp.describe().transpose()


# In[13]:


by_comp.describe().transpose()['GOOG']

