#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from scipy import stats


# In[2]:


df_smartphone = pd.read_json('/Users/brunobernardo/E-commerce-/Smartphones/search_output.jsonl')


# In[3]:


df_smartphone


# In[4]:


df_smartphone.info()


# In[5]:


df_smartphone.shape


# In[6]:


df_smartphone['price'] = df_smartphone['price'].str.replace('$', '')
df_smartphone['price']


# In[7]:


df_smartphone.head()


# In[ ]:




