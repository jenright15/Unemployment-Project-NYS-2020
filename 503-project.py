# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 14:43:02 2020

@author: johne
"""
#import os
#print(os.getcwd())
import numpy as np
import pandas as pd

## Unemployment Insurance Data ##################################
data = pd.read_csv('Unemployment_Insurance_Beneficiaries_and_Benefit_Amounts_Paid__Beginning_2001.csv')
#print(data);

##converting the data into a data frame
df = pd.DataFrame(data)
print(df);

import matplotlib.pyplot as plt
plt.bar('Year', df.columns[5], data = df)
plt.ylabel('Benefit Amounts (Millions of Dollars)')
plt.xlabel('Year since 2001')
plt.title('Unemployment Benefits Recieved in NY ');

#simple linear regression on benefit amount compared to year
target = pd.DataFrame(df, columns = [df.columns[5]])
X = df['Year']
y = target[df.columns[5]]
import statsmodels.api as sm
model = sm.OLS(y,X).fit()
predictions = model.predict(X)
model.summary();

#from sklearn import tree
#clf = tree.DecisionTreeClassifier()
#clf = clf.fit(df.columns[0], df.columns[5])

## looking at benefit payments per month in 2020
nd = df[['Year','Month','Beneficiaries',df.columns[5]]]
nd = nd[nd['Year']>=2020]
plt.bar('Month', nd.columns[3], data = nd)
plt.xlabel('Month')
plt.ylabel('Payments (Millions of Dollars)')
plt.title('UI Payments in NY 2020 ');

## Income Data for NY ########################################
income_data = pd.read_csv('Income_NY.csv')
income_df = pd.DataFrame(income_data);

plt.bar(income_df.columns[0], income_df.columns[2], data = income_df)
plt.xlabel('Year')
plt.ylabel('AGI')
plt.title('Average AGI for NY ')