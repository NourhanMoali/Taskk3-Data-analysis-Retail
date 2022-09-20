#!/usr/bin/env python
# coding: utf-8

# # THE SPARKS FOUNDATION 
# ## TASK3:Exploratory Data Analysis -Retai  

# # Nourhan Mohammed Ali Ebrahim 

# # #Dataset Source..
# 
# https://bit.ly/3i4rbWl

# # Importing All the Required libraries..

# In[8]:


import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[14]:


import pandas as pd 
ssd=pd.read_csv("data.csv")
print(ssd)


# In[15]:


ssd.info()


# In[16]:


ssd.describe()


# In[18]:


ssd.duplicated().sum()


# In[19]:


ssd.drop_duplicates(inplace=True )


# In[20]:


ssd.shape


# # Num of Unique Entries in The Dataset..

# In[ ]:


ssd=ssd.drop(['Country','Postal Code'],axis=1)


# In[23]:


ssd


# In[28]:


#sales/ profit/ in each sub category 
import matplotlib.pyplot as plt
subcategory_sale_profit=ssd.groupby('Sub-Category')[['Sales','Profit']].sum()
subcategory_sale_profit.sort_values('Sales',ascending=False,inplace=True)
subcategory_sale_profit.plot(kind="bar",figsize=(20,6))
plt.title('Sales/Profit in each Sub-Category')
plt.xlabel("Category")
plt.ylabel("Sales/Profit")
plt.show()


# In[29]:


state_sale_profit =ssd.groupby('State')[['Sales','Profit']].sum()
state_sale_profit.sort_values('Sales',ascending=False,inplace=True)
state_sale_profit
state_sale_profit.plot(kind="bar",figsize=(25,15))
plt.title("Sales/Profit in each State")
plt.xticks(rotation=90)
plt.xlabel("State")
plt.ylabel("Sales/Profit")
plt.show()


# In[34]:


import seaborn as sns
corr=ssd.corr()
sns.heatmap(corr,annot=True,cmap="Greens")


# In[36]:


sns.pairplot(ssd,hue='Ship Mode')


# In[37]:


ssd['Ship Mode'].value_counts()


# In[38]:


sns.countplot(x=ssd["Ship Mode"])


# In[40]:


ssd['Segment'].value_counts()


# In[41]:


sns.pairplot(ssd,hue='Segment')


# In[42]:


sns.countplot(x='Segment',data=ssd,palette='rainbow')


# In[46]:


ssd['Category'].value_counts()


# In[47]:


sns.countplot(x="Category",data=ssd)


# In[48]:


sns.pairplot(ssd,hue='Category')


# In[50]:


ssd['Sub-Category'].value_counts()


# In[55]:



ssd['Sub-Category'].value_counts().plot.pie(autopct='dark')
plt.show()


# In[56]:


ssd['State'].value_counts()


# In[59]:


#Observation 1
sns.countplot(x='State',data=ssd,palette="rocket_r",order=ssd["State"].value_counts().index)
plt.xticks(rotation=90)
plt.show()


# In[60]:


#observation 2:

ssd.hist(figsize=(15,10),bins=50)
plt.show()


# In[64]:


#Observation 3:

ssd['Region'].value_counts().plot.pie
plt.show()


# # Profit vs Discount

# In[63]:


fig,ax=plt.subplots(figsize=(20,10))
ax.scatter(ssd['Sales'],ssd['Profit'])
ax.set_xlabel('Sales')
ax.set_ylabel('Profit')
plt.show()


# In[66]:


sns.lineplot(x='Discount',y='Profit',label='Profit',data=ssd)
plt.legend()
plt.show()


# #Observation 4:
# 
# # Profit vs Quantity..
# 

# In[67]:


sns.lineplot(x='Quantity',y='Profit',label='Profit',data=ssd)
plt.legend()
plt.show()


# In[70]:


ssd.groupby('Segment')[['Profit','Sales']].sum().plot.bar(color=['red','green'])
plt.ylabel('Profit/Loss and Sales')
plt.show()


# In[71]:


#Observation 5:

plt.figure(figsize=(10,10))
plt.title('Segment sise Sales in each region')
sns.barplot(x='Region',y='Sales',data=ssd,hue='Segment',order=ssd['Region'].value_counts().index,palette='rocket')
plt.xlabel('Region')
plt.show()


# In[84]:


#Observation 6:
ps=ssd.groupby('State')[['Sales','Profit']].sum().sort_values(by='Sales',ascending=False)
ps[:].plot.bar(color=['pink','yellow'],figsize=(15,10))
plt.title('Profit/loss and Sales acrossstates')
plt.xlabel('States')
plt.ylabel('Profit/loss and Sales')
plt.show()


# In[86]:


#Observation 8:

t_states=ssd['State'].value_counts().nlargest(10)
t_states


# In[87]:



ssd.groupby('Category')[['Profit','Sales']].sum().plot.bar(color=['pink','yellow'],alpha=0.9,figsize=(8,5))
plt.ylabel('Profit/Loss and sales')
plt.show()


# In[88]:


#Observation 9:
ps=ssd.groupby('Sub-Category')[['Sales','Profit']].sum().sort_values(by='Sales',ascending=False)
ps[:].plot.bar(color=['pink','yellow'],figsize=(15,10))
plt.title('Profit/loss and Sales acrossstates')
plt.xlabel('Sub-Category')
plt.ylabel('Profit/loss and Sales')
plt.show()


# In[ ]:




