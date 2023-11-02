#!/usr/bin/env python
# coding: utf-8

# ## kilometer to miles

# In[7]:


kilometers = float(input("Distance in kilometers: "))
convert = 0.621371  # 1 kilometer = 0.621371 miles
miles = kilometers * convert


# In[8]:


print(f"{kilometers} kilometers is equal to {miles:.2f} miles")


# ## miles to kilometer

# In[11]:


miles1 = float(input("Distance in miles: "))
convert1 = 1.60934  # 1 mile = 1.60934 kilometers
kilometers1 = miles1 * convert1


# In[12]:


print(f"{miles1} miles is equal to {kilometers1} kilometers")


# In[ ]:




