#!/usr/bin/env python
# coding: utf-8

# ## kilo and meter

# In[8]:


weight = float(input("Enter weight (kilo): "))
height = float(input("Enter height (meter): "))


# In[9]:


bmi = weight/(height ** 2)


# In[10]:


print(f"Body Mas Index (BMI) is: {bmi:.2f}")


# In[11]:


if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi < 24.9:
    print("Healthy Weight Range")
elif 25 <= bmi < 29.9:
    print("Overweight")
else:
    print("OBESE")


# ## lbs and inches

# In[12]:


weight1 = float(input("Enter weight (lbs): "))
height1 = float(input("Enter height (inch): "))


# In[15]:


bmi1 = (weight1/ (height1 * height1)) * 703


# In[17]:


print(f"Body Mas Index (BMI) is: {bmi1:.2f}")


# In[ ]:




