
# coding: utf-8

# In[237]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import sys
sys.path.insert(0,'C:/Users/이세령/picasso/KOSDAQ-Gap-Strategy/CODE')
import mylib
matplotlib.rc('font', family='Malgun Gothic',size=8, weight = 'bold')


# In[238]:


KOSDAQTIK = pd.read_excel('C:/Users/이세령/picasso/KOSDAQ-Gap-Strategy/DATA/KOSDAQTIK.xlsx', header=2)


# In[239]:


KOSDAQTIK.head()


# In[240]:


KOSDAQTIK.dtypes


# In[241]:


KOSDAQTIK['hour'] = KOSDAQTIK.Date.dt.hour


# In[242]:


KOSDAQTIK['minute'] = KOSDAQTIK.Date.dt.minute


# In[243]:


KOSDAQTIK['Date'].dt.day.head()


# In[244]:


buy = KOSDAQTIK[(KOSDAQTIK.hour.between(15,15)) & (KOSDAQTIK.minute.between(30,30))].OPEN


# In[245]:


buy.head()


# In[246]:


get_ipython().magic('matplotlib inline')


# In[247]:


KOSDAQTIK.OPEN.shift(79).plot()
KOSDAQTIK.LAST_PRICE.plot()


# In[248]:


sell = KOSDAQTIK[(KOSDAQTIK.hour <= 9) & (KOSDAQTIK.minute.between(0,0))].OPEN


# In[249]:


sell.head()


# In[250]:


buy.head()


# In[251]:


KOSDAQTIK['buy'] = buy


# In[252]:


KOSDAQTIK['sell'] = sell


# In[253]:


KOSDAQTIK['buy'].dropna().head()


# In[254]:


s = KOSDAQTIK['sell'].dropna()


# In[255]:


s.head()


# In[256]:


gain = pd.Series((sell.values-buy.values)/buy.values)


# In[258]:


(1+gain).cumprod().plot()


# In[260]:


(1+gain).cumprod().tail()


# In[299]:


len(gain[gain>0])/len(gain)


# In[301]:


gain.mean()


# In[303]:


gain.plot()


# In[305]:


KOSDAQTIK.head()


# In[316]:


bet(data):
    start = 0.10
    cir = 1
    max_cir = 8
    for i in data:
        while cir <= max_cir:
            if i=true:
                cir +=1
            else:
                cir = 1
    weight = start*cir
    return weight
        


# In[317]:


bet(gain>0)

