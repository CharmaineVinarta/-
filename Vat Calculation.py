#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Input the total revenue and VAT rate (in percentage)
revenue = float(input("Enter the total revenue: $"))
vat_rate = float(input("Enter the VAT rate (in percentage): "))


# In[2]:


# Calculate the VAT amount
vat_amount = (revenue * vat_rate) / 100


# In[3]:


# Calculate the total amount (including VAT)
total = revenue + vat_amount


# In[4]:


# Display the results
print(f"Revenue: ${revenue:.2f}")
print(f"VAT Rate: {vat_rate}%")
print(f"VAT Amount: ${vat_amount:.2f}")
print(f"Total (including VAT): ${total:.2f}")


# In[ ]:




