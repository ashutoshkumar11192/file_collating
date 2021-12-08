#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import glob


# In[2]:


path = r'D:\Ashutosh\RTO Lock'
xlsb_files = glob.glob(path + '/*.xlsb')
xlsx_files = glob.glob(path + '/*.xlsx')
csv_files = glob.glob(path + '/*.csv')
all_files = xlsb_files + xlsx_files + csv_files


# In[3]:


all_files


# In[4]:


li = []
for i,j in enumerate(all_files):
    if all_files[i].endswith('.xlsx') == True:
        filename = all_files[i]
        df = pd.read_excel(filename, index_col=None, header=0)
        df['filename'] = filename
        li.append(df)
    elif all_files[i].endswith('.xlsb') == True:
        filename = all_files[i]
        df = pd.read_excel(filename, index_col=None, header=0, engine='pyxlsb')
        df['filename'] = filename
        li.append(df)
    elif all_files[i].endswith('.csv') ==True:
        filename = all_files[i]
        df = pd.read_csv(filename)
        df['filename'] = filename
        li.append(df)


# In[5]:


frame = pd.concat(li, axis=0,ignore_index=False)


# In[7]:


frame


# In[6]:


frame.to_csv('a.csv', index=False)


# In[ ]:




