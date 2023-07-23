#!/usr/bin/env python
# coding: utf-8

# 
# # Ecommerce Purchases Exercise 
# 

# In[1]:


import pandas as pd


# In[2]:


ecom = pd.read_csv('Ecommerce Purchases')


# **Check the head of the DataFrame.**

# In[3]:


ecom.head()


# ** How many rows and columns are there? **

# In[88]:


ecom.info()


# ** What is the average Purchase Price? **

# In[90]:


ecom['Purchase Price'].mean()


# ** What were the highest and lowest purchase prices? **

# In[92]:


ecom['Purchase Price'].max()


# In[93]:


ecom['Purchase Price'].min()


# ** How many people have English 'en' as their Language of choice on the website? **

# In[94]:


ecom[ecom['Language']=='en'].count()


# ** How many people have the job title of "Lawyer" ? **
# 

# In[95]:


ecom[ecom['Job'] == 'Lawyer'].info()


# ** How many people made the purchase during the AM and how many people made the purchase during PM ? **
# 
# **(Hint: Check out [value_counts()](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.value_counts.html) ) **

# In[96]:


ecom['AM or PM'].value_counts()


# ** What are the 5 most common Job Titles? **

# In[97]:


ecom['Job'].value_counts().head(5)


# ** Someone made a purchase that came from Lot: "90 WT" , what was the Purchase Price for this transaction? **

# In[99]:


ecom[ecom['Lot']=='90 WT']['Purchase Price']


# ** What is the email of the person with the following Credit Card Number: 4926535242672853 **

# In[100]:


ecom[ecom["Credit Card"] == 4926535242672853]['Email'] 


# ** How many people have American Express as their Credit Card Provider *and* made a purchase above $95 ?**

# In[101]:


ecom[(ecom['CC Provider']=='American Express') & (ecom['Purchase Price']>95)].count()


# ** Hard: How many people have a credit card that expires in 2025? **

# In[102]:


sum(ecom['CC Exp Date'].apply(lambda x: x[3:]) == '25')


# ** Hard: What are the top 5 most popular email providers/hosts (e.g. gmail.com, yahoo.com, etc...) **

# In[56]:


ecom['Email'].apply(lambda x: x.split('@')[1]).value_counts().head(5)

