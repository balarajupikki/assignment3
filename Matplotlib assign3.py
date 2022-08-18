#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


x=np.arange(0,100)
y=x*2
z=x**2


# In[3]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[9]:


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y)
ax.set_xlabel('x axis')
ax.set_ylabel('y axis')
ax.set_title('title')


# In[10]:


fig =plt.figure()
ax1 = fig.add_axes([0,0,1,1])
ax2 = fig.add_axes([0.2,0.5,0.2,0.2])


# In[11]:


ax1.plot(x,y,color='red')
ax2.plot(x,y,color='red')
fig


# In[12]:


fig = plt.figure()
ax1 = fig.add_axes([0,0,1,1])
ax2 = fig.add_axes([0.2,0.5,0.4,0.4])


# In[22]:


fig = plt.figure()
ax1 = fig.add_axes([0,0,1,1])
ax2 = fig.add_axes([0.2,0.5,0.4,0.4])
ax1.set_xlabel('x')
ax1.set_ylabel('z')
ax1.plot(x,z)
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title('zoom')
ax2.plot(x,y)
ax2.set_xlim(left=20,right=22)
ax2.set_ylim(bottom=30,top=50)


# In[23]:


fig = plt.figure()
ax1 = fig.add_axes([0,0,1,1])
ax2 = fig.add_axes([0.2,0.5,0.4,0.4])
ax1.set_xlabel('x')
ax1.set_ylabel('z')
ax1.plot(x,z)
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title('zoom')
ax2.plot(x,y)
ax2.set_xlim(left=20,right=22)
ax2.set_ylim(bottom=30,top=50)


# In[24]:


fig,axes = plt.subplots(1,2)


# In[20]:


fig,axes = plt.subplots(1,2)
axes[0].plot(x,y,lw=3,ls='--')
axes[1].plot(x,z,color='r',lw=4)


# In[21]:


fig,axes = plt.subplots(1,2,figsize=(12,2))
axes[0].plot(x,y,lw=3,ls='--')
axes[1].plot(x,z,color='r',lw=4)


# In[ ]:




