#!/usr/bin/env python
# coding: utf-8

# In[21]:


import numpy as np
scores=np.loadtxt('survey_large.txt', dtype='int')
print(scores.size)
print("Minimum Scores : ",scores.min())
print("Maximum Scores : ",scores.max())


# In[ ]:


#nps --> Net Promoters Score
#based on nps score, companies decide which product is best
#survey_large --> ratings
#ratings from 1 - 6 : detractors
#ratings from 7 - 8 : Neutrals
#ratings from 9 - 10 : Promoters


# 
# # NPS = (No of promoters - No of detractors)/Total no of people who particiapted in survey

# print("scores > 8 : ",scores>8)
# promoters = scores[scores>8]
# print("Size of promoters : ", promoters.size)
# detractors = scores[scores<6]
# print("Size of detractors : ", detractors.size)
# total = scores.size
# promotersNo = promoters.size
# detractorsNo = detractors.size
# nps = (promotersNo-detractorsNo)/total
# print("NPS value : ", nps)
# print("NPS % : ", nps*100)

# In[30]:


#Experiment 3
import pandas as pd 
df = pd.read_csv('gapminder-FiveYearData.csv')
df.head()  #starting 5 rows


# In[33]:


df.shape #(rows,columns)
#features or attributes
print("(No. of samples, features) : ", df.shape) 


# In[34]:


df.tail


# In[35]:


df.columns


# In[37]:


df.dtypes


# In[38]:


df.info()


# In[49]:


country_df = df['country']
print(country_df)
print("-------------------------------------------------------------------------------------------")
print("No of unique countries : ",country_df.nunique())
print("-------------------------------------------------------------------------------------------")
print("Names of unique countries : ",country_df.unique())


# In[52]:


#selecting multiple columns
country_con_year = df[['country','continent', 'year']]
print(country_con_year)


# In[81]:


#index
print(df.loc[0])
print("--------------------------------------------------------------------------------")
print(df.iloc[0])
print("--------------------------------------------------------------------------------")
print(df.iloc[-1])
print("--------------------------------------------------------------------------------")
print(df.iloc[[0,1,3]])
print("--------------------------------------------------------------------------------")
print(df.loc[[0,1,3]])
print("--------------------------------------------------------------------------------")
print(df.iloc[:,[0,1]])  
print("--------------------------------------------------------------------------------")

#negative index can be used in iloc, but negative index cannot be used in loc


# In[71]:


sub=list(range(4))
print(sub)
subset1 = df.iloc[:,sub]
print(subset)


# In[70]:


subset1.head()


# In[72]:


df.groupby('year')['lifeExp'].mean()


# In[76]:


df.groupby(['year','continent'])['lifeExp'].mean()


# In[78]:


df.groupby(['year','continent'])[['lifeExp','gdpPercap']].mean()


# In[101]:


#gdp growth of india in the year 2007
country_India = df[df['country']=='India']
print(country_India.size)
print("--------------------------------------------")
print(country_India.count())
print("--------------------------------------------")
year = df[df['year']==2007]
print(year.count())
print("--------------------------------------------")
india_2007 = df[(df['country'] == 'India') & (df['year'] == 2007)]
print(india_2007)




# In[110]:


#gdp of top 5 countries
gdp = df.groupby(['year'])['gdpPercap'].mean()
print(gdp)
gdp_mean = df.groupby(['country'])['gdpPercap'].mean()
top_5_countries = gdp_mean.sort_values(ascending=False).head(5)
print("-------------------------------------------------")
print(top_5_countries)


# In[116]:


#based on the dataset find which continent has largest data set
con1 = df.groupby(['continent'])['pop'].sum()
print(con1)
print("--------------------------------------------------")

print(con1.max())
print("continent with largest data set : ", df.loc[0])


# In[ ]:




