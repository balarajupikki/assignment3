#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import matplotlib.pyplot as plt


# In[5]:


df=pd.read_csv('df3.csv.csv')
get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


df


# In[6]:


df.info()


# In[7]:


df.head()


# In[8]:


df.plot.scatter(x='a',y='b',c='red',s=50,figsize=(12,3))


# In[10]:


df['a'].plot.hist()


# In[12]:


plt.style.use('ggplot')


# In[13]:


df['a'].plot.hist(alpha=0.5,bins=25)


# In[14]:


df[['a','b']].plot.box()


# In[15]:


df['d'].plot.kde()


# In[16]:


df['d'].plot.density(lw=5,ls='--')


# In[27]:


df.b[0:30].plot.area(alpha=0.4)


# In[28]:


f = plt.figure()
df.b[0:30].plot.area(alpha=0.4,ax=f.gca())
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
plt.show()


# In[ ]:




