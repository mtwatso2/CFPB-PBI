# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 15:02:23 2023

@author: MWatson717
"""

import pandas as pd

p = pd.read_csv('complaints_010924.csv')


p['Product'].value_counts()

p['Product'] = p['Product'].replace(['Credit reporting or other personal consumer reports',
                                     'Payday loan',
                                     'Payday loan, title loan, or personal loan',
                                     'Credit card',
                                     'Prepaid card',
                                     'Credit reporting'],
                                    
                                    ['Credit reporting, credit repair services, or other personal consumer reports',
                                     'Payday loan, title loan, personal loan, or advance loan',
                                     'Payday loan, title loan, personal loan, or advance loan',
                                     'Credit card or prepaid card',
                                     'Credit card or prepaid card',
                                     'Credit reporting, credit repair services, or other personal consumer reports'])

p['Product'].value_counts()

tr = ['Money Order',
      "Traveler's check or cashier's check"]

rw = ["Money order, traveler's check or cashier's check",
      "Money order, traveler's check or cashier's check"]

p['Sub-product'] = p['Sub-product'].replace(tr, rw)


data = p[['Date received', 'Product', 'Sub-product', 'Company', 'State']]


states = ['AA', 'AE', 'AP', 'AS', 'FM', 'GU', 'MH', 'MP', 'PR', 'PW',
          'UNITED STATES MINOR OUTLYING ISLANDS', 'VI', 'AK', 'HI']

data2 = data[~data['State'].isin(states)] #4489201

data2.isnull().sum() #missing 43941 states

data2 = data2[data2['State'].notna()] #works, left with 4445260, 

data2.isnull().sum()

data2['Sub-product'] = data2['Sub-product'].fillna('(Blank)')

data2.isnull().sum()

data2['Year']  = pd.DatetimeIndex(data2['Date received']).year
data2['Month'] = pd.DatetimeIndex(data2['Date received']).month


panel1 = data2.groupby(by=['Year', 'Month', 'Product', 'Sub-product'], as_index=False).agg(Count=('Product', 'count'))

panel2 = data2.groupby(by=['Year', 'State', 'Product'], as_index=False).agg(Count=('Product', 'count'))

panel3 = data2.groupby(by=['Year', 'Company', 'Product'], as_index=False).agg(Count=('Product', 'count'))

panel1.to_csv('panel1.csv', index=False)
panel2.to_csv('panel2.csv', index=False)
panel3.to_csv('panel3.csv', index=False)

#data.to_csv('CFPB_pbi_010924.csv', index=False)

