#!/usr/bin/env python
# coding: utf-8

# ## Amazon - Web Scraping - Products and Sales

# ### Working with Dataframe

# In[1]:


import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from scipy import stats
from sqlalchemy import create_engine


# ### Intro
# 
# #### Extracting 8 diffenrent product Dataframe from Amazon Web Scraping - 2021
# 
# #### Including Data Cleaning

# ### 1-) Headphones

# In[2]:


df_headphones = pd.read_json('/Users/brunobernardo/E-commerce-/headphone/search_output_headphones.jsonl')


# In[3]:


df_headphones


# In[4]:


# removing dollar sign

df_headphones['price'] = df_headphones['price'].str.replace('$', '')
df_headphones['price']


# In[5]:


# removing "out of 5 stars"

df_headphones['rating'] = df_headphones['rating'].str.replace('out of 5 stars', '')
df_headphones['rating']


# In[6]:


# removing None values

# removing None values


df_headphones.dropna(
    axis=0,
    how='any',
    thresh=None,
    subset=None,
    inplace=True
)


# In[7]:


# Add Product_Type column

df_headphones.loc[:,'Product_Type'] = "headphones" 


# In[8]:


# Final dataframe 

df_headphones


# #### The next 7 products will use the same procedures

# ### 2-) Processors

# In[9]:


df_processors = pd.read_json('/Users/brunobernardo/E-commerce-/Processors 2/search_output_processors2.jsonl')


# In[10]:


df_processors


# In[11]:


df_processors['price'] = df_processors['price'].str.replace('$', '')
df_processors['price']


# In[12]:


df_processors['rating'] = df_processors['rating'].str.replace('out of 5 stars', '')
df_processors['rating']


# In[13]:


df_processors.dropna(
    axis=0,
    how='any',
    thresh=None,
    subset=None,
    inplace=True
)


# In[14]:


df_processors.loc[:,'Product_Type'] = "processors" 


# In[15]:


df_processors


# ### 3-) Cameras

# In[16]:


df_cameras = pd.read_json('/Users/brunobernardo/E-commerce-/Cameras/search_output_cameras.jsonl')


# In[17]:


df_cameras


# In[18]:


df_cameras['price'] = df_cameras['price'].str.replace('$', '')
df_cameras['price']


# In[19]:


df_cameras['rating'] = df_cameras['rating'].str.replace('out of 5 stars', '')
df_cameras['rating']


# In[20]:


df_cameras.dropna(
    axis=0,
    how='any',
    thresh=None,
    subset=None,
    inplace=True
)


# In[21]:


df_cameras.loc[:,'Product_Type'] = "cameras" 


# In[22]:


df_cameras


# ### 4-) Keyboards

# In[23]:


df_keyboards = pd.read_json('/Users/brunobernardo/E-commerce-/Keyboards/search_output_keyboard.jsonl')


# In[24]:


df_keyboards


# In[25]:


df_keyboards['price'] = df_keyboards['price'].str.replace('$', '')
df_keyboards['price']


# In[26]:


df_keyboards['rating'] = df_keyboards['rating'].str.replace('out of 5 stars', '')
df_keyboards['rating']


# In[27]:


df_keyboards.dropna(
    axis=0,
    how='any',
    thresh=None,
    subset=None,
    inplace=True
)


# In[28]:


df_keyboards.loc[:,'Product_Type'] = "keyboards" 


# In[29]:


df_keyboards


# ### 5-) Smartphones

# In[30]:


df_smartphones = pd.read_json('/Users/brunobernardo/E-commerce-/Smartphones/search_output.jsonl')


# In[31]:


df_smartphones


# In[32]:


df_smartphones['price'] = df_smartphones['price'].str.replace('$', '')
df_smartphones['price']


# In[33]:


df_smartphones['rating'] = df_smartphones['rating'].str.replace('out of 5 stars', '')
df_smartphones['rating']


# In[34]:


df_smartphones.loc[:,'Product_Type'] = "smartphones" 


# In[35]:


df_smartphones.dropna(
    axis=0,
    how='any',
    thresh=None,
    subset=None,
    inplace=True
)


# In[36]:


df_smartphones


# ### 6-) Monitors

# In[37]:


df_monitors = pd.read_json('/Users/brunobernardo/E-commerce-/Monitors/search_output_monitors.jsonl')


# In[38]:


df_monitors


# In[39]:


df_monitors['price'] = df_monitors['price'].str.replace('$', '')
df_monitors['price']


# In[40]:


df_monitors['rating'] = df_monitors['rating'].str.replace('out of 5 stars', '')
df_monitors['rating']


# In[41]:


df_monitors.dropna(
    axis=0,
    how='any',
    thresh=None,
    subset=None,
    inplace=True
)


# In[42]:


df_monitors.loc[:,'Product_Type'] = "monitors" 


# In[43]:


df_monitors


# ### 7-) Mouses

# In[44]:


df_mouses = pd.read_json('/Users/brunobernardo/E-commerce-/Mouses/search_output_mouses.jsonl')


# In[45]:


df_mouses


# In[46]:


df_mouses['price'] = df_mouses['price'].str.replace('$', '')
df_mouses['price']


# In[47]:


df_mouses['rating'] = df_mouses['rating'].str.replace('out of 5 stars', '')
df_mouses['rating']


# In[49]:


df_mouses.dropna(
    axis=0,
    how='any',
    thresh=None,
    subset=None,
    inplace=True
)


# In[51]:


df_mouses.loc[:,'Product_Type'] = "mouse"  


# In[52]:


df_mouses


# ### 8-) DSLR Cameras

# In[53]:


df_dslrcameras = pd.read_json('/Users/brunobernardo/E-commerce-/DSLR Cameras/search_output_dslrcameras.jsonl')


# In[54]:


df_dslrcameras


# In[55]:


df_dslrcameras['price'] = df_dslrcameras['price'].str.replace('$', '')
df_dslrcameras['price']


# In[56]:


df_dslrcameras['rating'] = df_dslrcameras['rating'].str.replace('out of 5 stars', '')
df_dslrcameras['rating']


# In[57]:


df_dslrcameras.dropna(
    axis=0,
    how='any',
    thresh=None,
    subset=None,
    inplace=True
)


# In[58]:


df_dslrcameras.loc[:,'Product_Type'] = "dslr_cameras" 


# In[59]:


df_dslrcameras


# ## pd.concat - Joint Dataframes 

# In[60]:


df_products = pd.concat([df_headphones, df_processors, df_cameras, df_keyboards, df_smartphones, df_monitors, df_mouses,df_dslrcameras])


# In[61]:


df_products


# In[62]:


df_products.isnull().sum()


# ## Link to SQL - Final dataframe with 8 products 

# In[63]:


# remove the password
sqlEngine = create_engine('mysql+pymysql://root:@127.0.0.1/amazon', pool_recycle=3600)

dbConnection    = sqlEngine.connect()

# This is for creating data base
# sqlEngine.execute("CREATE DATABASE IF NOT EXISTS AMAZON") #create db --> not using this for now
sqlEngine.execute("USE AMAZON") # select new db

tableName   = "Products"


try:
    frame = df_products.to_sql(tableName, dbConnection, if_exists='replace',index = False)

except ValueError as vx:
    print(vx)

except Exception as ex:   
    print(ex)

else:
    print("Table %s created successfully."%tableName);   

finally:
    dbConnection.close()


# In[ ]:




