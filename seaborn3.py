
import pandas as pd


# In[9]:


df=pd.read_csv(r"D:\\download\\Car_sales.csv")
print (df)


df.info()


# In[11]:


df.describe()


# In[20]:


df.value_counts()
df


# # use of sns and matplotlib.pyplot (seaborn to plot heatmap)
# # 1. histogram
# # 2.box plots 
# # 3.scatter plots 

# In[51]:


import seaborn as sns 
import matplotlib.pyplot as plt
import numpy as np


# In[59]:


left = [1,2,3,4,5,6]
height = [140,150,160,193,275,116]
tick_label =['Acura','Audi', 'volvo', 'BMW', 'Cadillac','Chevrolet']
plt.bar (left, height , tick_label= tick_label, width = 0.6 ,  color= ['red', 'green','blue'])
plt.xlabel('cars')
plt.ylabel('Horsepower')
plt. title('sales of cars')
plt.show()


# In[65]:


np.random.seed(150)
df=np.random.normal(loc= 0, scale=1 ,size=100)
plt.boxplot(df)
plt.title('basic box plot')
plt.ylable('value')
plt.show()


# In[80]:


import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv("D:\\download\\Car_sales.csv",nrows=20)
x=df["Manufacturer"]
y= df["Horsepower"]
plt.scatter(x,y)
plt.xlabel("model name")
plt.ylabel("horsepower")
plt.figure(figsize= (20,60))
df
plt.show()


# In[95]:


import matplotlib.pyplot as plt
import seaborn as sns
sns.scatterplot(df)
plt.xlabel("tips")
plt.ylabel("horsepower")


# In[102]:


df=np.random.rand(10,10)
sns.heatmap(df)
plt.show()


# In[99]:


df=np.random.rand(10,10)
sns.coldmap(df)
plt.show()


# In[ ]:




