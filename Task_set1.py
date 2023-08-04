#!/usr/bin/env python
# coding: utf-8

# # Import NumPy

# In[1]:


import numpy as np


# In[2]:


a=np.array([1,2,3,4,5,6,7,8,9])


# # Find Minimum

# In[3]:


np.min(a)


# # Find Max

# In[4]:


np.max(a)


# # Find Mean

# In[5]:


np.mean(a)


# # Find Median

# In[6]:


np.median(a)


# # Find Standard Deviation

# In[7]:


np.std(a)


# # Reshape array from 1D to 2D

# In[8]:


new=a.reshape(3,3)


# In[9]:


new


# # Extract odd numbers from array

# In[11]:


print(new[new%2!=0])


# In[ ]:




