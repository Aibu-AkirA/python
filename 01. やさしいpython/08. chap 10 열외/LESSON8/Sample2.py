#!/usr/bin/env python
# coding: utf-8

# In[1]:


f = open("Sample.txt", "r")
lines = f.readlines()
for line in lines:
    print(line, end="")
    
f.close()


# In[ ]:




