#!/usr/bin/env python
# coding: utf-8

# # Data Input and Output
# 
# This notebook is the reference code for getting input and output, pandas can read a variety of file types using its pd.read_ methods. Let's take a look at the most common data types:

# In[1]:


import numpy as np
import pandas as pd


# # CSV
# # EXCEL
# # HTML
# # SQL

# # conda install sqlalchemy
# # conda install lxml
# # conda install html5lib
# # conda install BeautifulSoup4

# In[3]:


get_ipython().system('conda install sqlalchemy')


# In[6]:


get_ipython().system('conda install lxml --yes')


# In[7]:


get_ipython().system('conda install html5lib')


# In[9]:


get_ipython().system('conda install BeautifulSoup4 --yes')


# In[10]:


get_ipython().system('pip list')


# ## CSV
# 
# ### CSV Input

# In[11]:


df = pd.read_csv('example')
df


# ### CSV Output

# In[12]:


df.to_csv('example',index=False)


# ## Excel
# Pandas can read and write excel files, keep in mind, this only imports data. Not formulas or images, having images or macros may cause this read_excel method to crash. 

# ### Excel Input

# In[15]:


pd.read_excel('Excel_Sample.xlsx',sheet_name='Sheet1')


# ### Excel Output

# In[16]:


df.to_excel('Excel_Sample.xlsx',sheet_name='Sheet1')


# ## HTML
# 
# You may need to install htmllib5,lxml, and BeautifulSoup4. In your terminal/command prompt run:
# 
#     conda install lxml
#     conda install html5lib
#     conda install BeautifulSoup4
# 
# Then restart Jupyter Notebook.
# (or use pip install if you aren't using the Anaconda Distribution)
# 
# Pandas can read table tabs off of html. For example:

# ### HTML Input
# 
# Pandas read_html function will read tables off of a webpage and return a list of DataFrame objects:

# https://www.jamaran.news/%D8%A8%D8%AE%D8%B4-%D9%88%D8%B1%D8%B2%D8%B4%DB%8C-160/1517831-%D8%AC%D8%AF%D9%88%D9%84-%D8%B1%D8%AF%D9%87-%D8%A8%D9%86%D8%AF%DB%8C-%D9%85%D8%AF%D8%A7%D9%84%DB%8C-%D8%A7%D9%84%D9%85%D9%BE%DB%8C%DA%A9-%D8%AA%D9%88%DA%A9%DB%8C%D9%88

# In[47]:


df = pd.read_html('https://www.jamaran.news/%D8%A8%D8%AE%D8%B4-%D9%88%D8%B1%D8%B2%D8%B4%DB%8C-160/1517831-%D8%AC%D8%AF%D9%88%D9%84-%D8%B1%D8%AF%D9%87-%D8%A8%D9%86%D8%AF%DB%8C-%D9%85%D8%AF%D8%A7%D9%84%DB%8C-%D8%A7%D9%84%D9%85%D9%BE%DB%8C%DA%A9-%D8%AA%D9%88%DA%A9%DB%8C%D9%88')


# In[50]:


df[0]


# In[53]:


df = pd.read_excel('Excel_Sample.xlsx',sheet_name='Sheet1')


# _____
# _____
# # SQL (Optional)
# 
# 

# 
# 
# The key functions are:
# 
# * read_sql_table(table_name, con[, schema, ...])	
#     * Read SQL database table into a DataFrame.
# * read_sql_query(sql, con[, index_col, ...])	
#     * Read SQL query into a DataFrame.
# * read_sql(sql, con[, index_col, ...])	
#     * Read SQL query or database table into a DataFrame.
# * DataFrame.to_sql(name, con[, flavor, ...])	
#     * Write records stored in a DataFrame to a SQL database.

# In[28]:


from sqlalchemy import create_engine


# In[57]:


engine = create_engine('sqlite:///:memory:')


# In[58]:


df.to_sql('data', engine)


# In[59]:


sql_df = pd.read_sql('data',con=engine)


# In[60]:


sql_df


# In[ ]:




