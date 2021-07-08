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


# In[8]:


df_smartphone.dtypes


# In[9]:


# Not surprisingly the Sales column is stored as an object. 
# The ‘$’ and ‘,’ are dead giveaways that the Sales column is not a numeric column. 
#.  More than likely we want to do some math on the column so let’s try to convert it to a float.

In the real world data set, you may not be so quick to see that there are non-numeric values in the column. In my data set, my first approach was to try to use astype()

df_smartphone['price'].astype('float')


# In[10]:


# The traceback includes a ValueError and shows that it could not convert the $1,000.00 string to a float.

#  Ok. That should be easy to clean up.

#   Basically, I assumed that an object column contained all strings. 

#    In reality, an object column can contain a mixture of multiple types.

#     Let’s look at the types in this data set.


# In[12]:


df_smartphone['price'].apply(type)


# In[ ]:


# This nicely shows the issue. 
#  The apply(type) code runs the type function on each value in the column.
#   As you can see, some of the values are NoneType and some are strings. 
#    Overall, the column dtype is an object.


# In[ ]:


# First, we can add a formatted column that shows each type:


# In[ ]:


df_smartphone['price_Type'] = df_smartphone['price'].apply(lambda x: type(x).__name__)


# In[ ]:


# here is a more compact way to check the types of data in a column using value_counts()


# In[14]:


df_smartphone['price'].apply(type).value_counts()


# In[15]:


def clean_currency(x):
    """ If the value is a string, then remove currency symbol and delimiters
    otherwise, the value is numeric and can be converted
    """
    if isinstance(x, str):
        return(x.replace('$', '').replace(',', ''))
    return(x)


# In[ ]:


# This function will check if the supplied value is a string and if it is, 
# will remove all the characters we don’t need. 
# If it is not a string, then it will return the original value.


# In[16]:


# Here is how we call it and convert the results to a float. I also show the column with the types:

df_smartphone['price'] = df_smartphone['price'].apply(clean_currency).astype('float')
df_smartphone['price_Type'] = df_smartphone['price'].apply(lambda x: type(x).__name__)


# In[17]:


# We can also check the dtypes

df_smartphone.dtypes


# In[18]:


# Or look at the value_counts 

df_smartphone['price'].apply(type).value_counts()


# In[ ]:




