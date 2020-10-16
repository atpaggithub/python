#!/usr/bin/env python
# coding: utf-8

# ### <p style="text-align: right;"> &#9989; Jenna Thibodeau</p>

# # __CMSE  201 &ndash; Fall 2020__
# 
# <img src="https://cmse.msu.edu/sites/_cmse/assets/Image/image002.jpg"
#      alt="CMSE Logo"
#      align="right" 
#      height="100" 
#      width="100" />

# # Homework 03: Exploring Italy's Migration Data
# <img src="https://upload.wikimedia.org/wikipedia/commons/f/fc/Italy%2C_foreign_residents_as_a_percentage_of_the_total_population%2C_2011.svg" width=500px>

# ## Goals
# 
# ### By the end of the homework assignment you will have practiced:
# 
# 1. Loading in data
# 2. Cleaning data
# 3. Plotting data
# 4. Using seaborn
# 7. Read documentation

# ## Assignment instructions
# 
# Work through the following assignment, making sure to follow all of the directions and answer all of the questions.
# 
# **This assignment is due at 11:59pm on Friday, October 16.** 
# 
# It should be uploaded into D2L Homework #3.  Submission instructions can be found at the end of the notebook.

# ## Grading
# 
# - Cleaning, understanding data and reading documentation (25 pts)
# - Plotting, interpreting, researching (28pts)
# 
# **Total:** 53 pts
# 

# ---
# # 1. Introduction
# 
# In this homework you will use `pandas` to do some Exploratory Data Analysis (EDA). This consists in searching, acquiring, cleaning, and analyzing data. A large amount of time of a data scientist is spent in the first two items of that list. We have decided to save you some time and provide you with the data so that you can focus on  
# the last two items on the list. 
# 
# The Population Division of the Department of Economics and Social Affairs of the United Nations periodically collects migration data from countries around the world and this notebook uses data from their [2015 revision](https://www.un.org/en/development/desa/population/migration/data/empirical2/migrationflows.asp). 
# 
# You can follow the link and choose to do some EDA on any country of your choice, but for this homework you will focus on Italy.
# 
# Let's start by importing the necessary libraries

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd 
import seaborn as sns 
import numpy as np


# ## Gathering Data
# 
# Import the data from the excel file. Pandas has a function specific for reading excel files, here is the [link](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html).

# In[2]:


# Let's read in the data and print the first few lines
italy_migration_filepath = 'Italy.xlsx'
italy_data = pd.read_excel(italy_migration_filepath)
italy_data.head(10) 


# ---
# # 2. Cleaning Data
# 
# As you can see there are a lot of `Nan` entries in the data and many "Unnamed" columns. Open the file with Microsoft Excel or an equivalent tool. If you don't currently have Excel on your computer, you should be able to acquire it on [spartan365.msu.edu](http://spartan365.msu.edu/). Alternatively, you may find a useful option [here](http://www.repairmsexcel.com/blog/open-excel-files-without-excel).
# 
# Once you're opened the file, take a look at it. You should find that the first 19 lines contain only the UN symbol and other reference information, we don't need them. So we better skip all these lines. Actually we only care about data from line 21 and on. Also the file contains four sheet of data, in this homework we will need only the data from sheet "**Italy by Citizenship**".
# 
# &#9989;&nbsp; **Question 2.1: (5pts)** Look up the documentation for the [`read_excel`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html) function and read in the data from *Italy by Citizenship* sheet by skipping the first 20 lines from the top and the last two lines from the bottom. Then, to check that everything was loaded correctly, print the first 10 lines and, in another cell, the last 5 lines.

# In[3]:


citizens = pd.read_excel('Italy.xlsx', sheet_name="Italy by Citizenship",skiprows=20,skipfooter=2)
citizens


# In[4]:


citizens.head(10)


# Now print the last five lines

# In[5]:


citizens.tail(5)


# Good! Notice that we have data both for immigrants (people entering Italy) and emigrants (people leaving Italy). However, there are lot of `..` entries, which means that we have no data for those years. Let's replace them with zeros.
# 
# &#9989;&nbsp; **Question 2.2: (2pts)** Replace all the `..` entries with `0` and then print the first 5 lines to make sure it worked.
# 
# *Hint*: there is a `pandas` function that you can use to do the replacement!
# Also, note that the "`..`" entries are different than `...` because the appearance of `...` just means that `pandas` is suppressing some of the data to make the table fit on your screen.

# In[6]:


# Put your code here
dots = citizens.replace("..",0)
dots.head(5)


# &#9989;&nbsp; **Question 2.3: (2pts)** Let's look at immigration data only. Create a new dataset containing data for Immigrants only and and print the first 3 lines. Call this dataset `imm_data`.
# 
# *Hint*: you should be able to do this using a mask!

# In[7]:


# Put your code here
imm_data = dots[dots.Type=='Immigrants']
imm_data.iloc[0:3]


# Almost done. Notice that the first few columns contain information that are not particularly interesting in this case, thus, it is better to remove them. 
# 
# &#9989;&nbsp; **Question 2.4: (2pts)** Remove the columns **Type**, **Coverage**, **AREA**, **AreaName**, **REG**, **RegName**, **DEV**, **DevName** and print the first 5 lines.

# In[8]:


imm_data2=imm_data.drop(imm_data.columns[[0,1,3,4,5,6,7,8]], axis=1)
imm_data2.head(5)


# Perfect, we have cleaned our dataset enough that we can start learning something from it. Let's look at some statistics first.
# 
# &#9989;&nbsp; **Question 2.5: (5pts)** Run the command `.describe()` on your immigration data set and answer the following questions:
# 1. What do the rows that are output from the `describe` function tell you?
# 2. Without counting and by looking only at the output of `decsribe()`, how many countries are in the dataset and how many years?

# In[9]:


# Put your code here
imm_data2.describe()


# <font size=+3>&#9998;</font> *The rows display different stats values from the data set derived from the citizens of Italy that Immigrated to the country. there are 12 years represented and 5 different countries *

# Let's now look at the countries with the most represenation in Italy. We will do this in two ways. 

# &#9989;&nbsp; **Question 2.6: (5pts)** First, write a loop to print the country with the largest amount of immigrants for each year. 
# 
# *Hint:* There are many different ways to do this. You can try using `iloc` to move through the data or you can search `pandas` documentation for a function that grabs the index of the maximum value for a given column.

# In[10]:


# Put your code here
for column in imm_data2:
    print(column)
    if column!="OdName":
        max_data=imm_data2[column].idxmax()
        country = imm_data2['OdName'][max_data]
        print(country)


# Now answer the following questions:
# 
# 1. What are the countries with the most immigrants?    
# 2. Why is Afghanistan the country with most immigrants from 1980--1990?

# <font size=+3>&#9998;</font> *1.Afghanistan, Italy and Romania, 2. Afghanistan has the most immigrants from 1980-1990 becuase of the Soviet Invasion going on at that time period*

# &#9989;&nbsp; **Question 2.7: (4pts)** Second, add a new column to the dataframe that contains the total number of immigrants for each country (i.e. the sum of all the year columns). Then, sort this data in a descending order and save it in a new dataframe (call it `sorted_df`). Print the top ten countries with the largest total number of immigrants. 
# 
# *Hint:* You might want look up the documentation for [`sort_values` ](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sort_values.html)

# In[11]:


imm_data2['total immigrants']=imm_data2.sum(axis=1)
imm_data2.head()


# In[12]:


sorted_df=imm_data2.sort_values(by=['total immigrants'],ascending=False)
sorted_df.head(10)


# ---
# # 3. Plotting
# 
# Up to now we have played around with the data and look at some initial statistics. Now it is time for plotting.
# But first a little more data restructuring! This may not be the most exciting part of doing data analysis, but this is an critical part of working with data. 
# 
# &#9989;&nbsp; **Question 3.1: (5pts)** First, let's flip our sorted dataset so that we have years as the rows and countries information as the columns. After you transpose the data, make the name of the countries the new column headers. After you've done that, drop the first row with the country names since it is redundant information. Finally print the last 5 rows.

# In[15]:


sorted_df=sorted_df.transpose()
sorted_df.head()


# In[16]:


sorted_df.columns=sorted_df.iloc[0,]
sorted_df.head()


# In[17]:


new_sorted_df=sorted_df.drop(['OdName'])
new_sorted_df.tail(5)


# Finally we have a good dataset with data in the right order and so on. Remember from question 2.6 we looked for the top ten countries with most immigrants.
# 
# &#9989;&nbsp; **Question 3.2: (8pts)** Plot their time series, **but only for the first six**. Make the plot 10 inches by 7 inches (width by height) in size. Make sure to not plot the row **Total**. Don't forget to label your axis and include a legend!
# 
# *Note:* In this case you use either `seaborn` or `pandas` plotting functions. Either way is fine. Read through the documentation of either to find out how to make the plot 10x7. 

# In[19]:


import matplotlib.pyplot as plt


# In[26]:


# Put your code here
years=list(range(1980,2014))
plt.rcParams['figure.figsize']=(10,7)
plt.plot(years,new_sorted_df['Romania'],label='Romania')
plt.plot(years,new_sorted_df['Italy'],label='Italy')
plt.plot(years,new_sorted_df['Morocco'],label='Morocco')
plt.plot(years,new_sorted_df["Albania"],label='Albania')
plt.plot(years,new_sorted_df['Ukraine'],label='Ukraine')
plt.plot(years,new_sorted_df['China'],label='China')
plt.xlabel('years')
plt.ylabel('Population')


# Based on your plot, answer the following questions:
# 1. What new information does this plot convey that you could not gather from the previous section? 
# 2. Why is there a spike for Romania in 2007? You might want to search the internet for this. 

# <font size=+3>&#9998;</font> *Put your answers here.*

# Another interesting information we can extract from this data set is to look at the size of the migration flows.
# 
# &#9989;&nbsp; **Question 3.3: (5pts)** Make a histogram for the year 2005. Make this plot 10 inches by 7 inches (width by height).

# In[ ]:


# Put your code here


# Answer the following questions:
# 
# 1. What does this plot tell you?
# 2. How many bins are there?
# 3. Why such a high number in the first bin?
# 4. Can you think of a way to remove the peak in the first bin?

# ## Correlations
# 
# Let's see if there are any correlation between the top 6 countries. To do this we will use the method `pairplot` from `seaborn`. 
# 
# &#9989;&nbsp; **Question 3.4 (10pts):** Use [`pairplot`](https://seaborn.pydata.org/generated/seaborn.pairplot.html) to make a map of correlations between the six countries.
# 
# *Hint:* you might want to first make a new dataframe that contains only the top six countries and without the **Total** row.

# In[ ]:


# Put your code here


# Now that you've made your plot, answer the following questions:
# 
# 1. What do the plots on the diagonal indicate?
# 2. What do the off-diagonal plots indicate?
# 3. Do you see any correlation (positive or negative) between the countries? Specify which countries, if any, you observe to have a correlation and whether it is a positive or negative correlation.

# <font size=+3>&#9998;</font> *Put your answers here.*

# ---
# ## Assignment Wrap-up
# 
# Please fill out the following Google Form before you submit your assignment. **You must completely fill this out in order to receive credit for the assignment!**
# 
# **COMPLETE THIS SURVEY through [this link](https://forms.office.com/Pages/ResponsePage.aspx?id=MHEXIi9k2UGSEXQjetVofddd5T-Pwn1DlT6_yoCyuCFUMTIwRjdDVFlLTElPOTVYTzNCTVk0UkVHNi4u) or through cell below.**

# In[ ]:


from IPython.display import HTML
HTML(
"""
<iframe 
	src="https://forms.office.com/Pages/ResponsePage.aspx?id=MHEXIi9k2UGSEXQjetVofddd5T-Pwn1DlT6_yoCyuCFUMTIwRjdDVFlLTElPOTVYTzNCTVk0UkVHNi4u" 
	width="80%" 
	height="1200px" 
	frameborder="0" 
	marginheight="0" 
	marginwidth="0">
	Loading...
</iframe>
"""
)


# ---
# 
# ### Congratulations, you're done!
# 
# Submit this assignment by uploading it to the course Desire2Learn web page.  
# Go to the "Homework Assignments" section, find the submission folder link for Homework #3, and upload it there.
# 

# &#169; Copyright 2020,  Michigan State University Board of Trustees
