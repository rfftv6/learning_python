# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 10:09:00 2016

This script calculates descriptive statistics from a file with 
numerical and categorical data

@author: rv469735
"""

#import libraries
import pandas as pd
import sys
import matplotlib.pyplot as plt


pd.set_option('display.max_colwidth', -1)

#increase rows in prinout
pd.set_option('display.max_rows', 500) 

#reading the CSV file with the data on the same directory as the py file
df= pd.read_csv('diamonds.csv')

#selecting only the columns with data
df_select= df.drop(df.columns[[0]], axis=1) 

#selecting all the categorical values to tally numerical values
df_categorical=df_select.groupby(['cut','color','clarity']).describe()

#February 6, 2017 what if i want a specific cut?
#df_categorical=df_select['cut'].groupby([df_select['color'],df_select['clarity']]).describe()

#df_categorical=df_select['depth'].describe()
#df_categorical1=df_select['clarity'].unique()
#df_categorical2=df_select['color'].unique()
                        

#February 6, 2017 what can be placed btw describe()


#alternatively one can ony select one of the numerical values like 'x'
#df_categorical=df_select.groupby(['clarity','cut','color'])['x'].describe()

#df_categorical=df_select.groupby(['color']).describe()

#df_categorical=df_select['color'].groupby([df_select['cut'],df_select['clarity']]).describe()



#df_categorical3=df_select.groupby([df_select['cut'],df_select['clarity'],df_select['color']]).describe()

#sys.stdout=open('output.txt', 'w')
#print(df_categorical)

fig, ax=plt.subplots()
#
colors = {'D':'red', 'E':'blue', 'F':'green', 'G':'skyblue', 'H':'yellow', 'I':'plum','J':'navy'}
#
ax.scatter(df['cut'], df['depth'], c=df['color'].apply(lambda x: colors[x]))
plt.title('diamonds')
plt.ylabel('depth')
plt.xlabel('cut')
plt.legend()
plt.axis([0, 5.1, 40, 80])
plt.grid(True)
plt.show()


