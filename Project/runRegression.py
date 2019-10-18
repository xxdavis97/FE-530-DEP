import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
from multicollinearity import multicollinearity_check

#USA
#SETUP DATA
goodsAndServices = pd.read_csv('./Data/Goods And Services Data (Long).csv')
gdp = pd.read_csv('./Data/GDP.csv')
gdp.set_index('DATE', inplace=True)

inflation = pd.read_csv('./Data/Inflation Data (Long).csv')
inflation['DATE'] = pd.DatetimeIndex(inflation['DATE']).year
inflation.set_index('DATE', inplace=True)

usaGoodsAndServices = goodsAndServices[(goodsAndServices['LOCATION'] == 'USA')]
usaGoodsAndServices = usaGoodsAndServices[usaGoodsAndServices['FREQUENCY'] == 'A']
usaGoodsAndServices = usaGoodsAndServices[usaGoodsAndServices['MEASURE'] == 'MLN_USD']
usaGoodsAndServices.rename(columns={'TIME': 'DATE'}, inplace=True)
usaGoodsAndServices.set_index('DATE', inplace=True)
usaGoodsAndServicesEXP = usaGoodsAndServices[usaGoodsAndServices['SUBJECT'] == 'EXP']
usaGoodsAndServicesIMP = usaGoodsAndServices[usaGoodsAndServices['SUBJECT'] == 'IMP']
usaGoodsAndServices = usaGoodsAndServicesEXP
usaGoodsAndServices.rename(columns={'Value' : 'Exports'}, inplace=True)
usaGoodsAndServices['Imports'] = usaGoodsAndServicesIMP[['Value']].values.flatten()
usaGoodsAndServices['Total Trade Volume'] = usaGoodsAndServices['Exports'] + usaGoodsAndServices['Imports']
usaGoodsAndServices = usaGoodsAndServices[['Total Trade Volume']]

#MULTICOLLINEARITY
corrFrame = pd.DataFrame()
corrFrame['DATE'] = usaGoodsAndServices.index
corrFrame.set_index('DATE', inplace=True)
corrFrame['Total Trade Volume'] = usaGoodsAndServices[['Total Trade Volume']].pct_change()
corrFrame['GDP'] = gdp.pct_change()['GDP'].values.flatten()
corrFrame.dropna(inplace=True)
# multicollinearity_check(corrFrame)
# print(corrFrame.corr())

#SETUP REGERESSION DATAFRAME
regressionFrame = pd.DataFrame()
flatInflation = inflation.values.flatten()[10:]
regressionFrame['Inflation'] = flatInflation
regressionFrame.index = usaGoodsAndServicesEXP.index
regressionFrame['Change In Total Trade Volume'] = usaGoodsAndServices[['Total Trade Volume']].pct_change()
regressionFrame['Change In GDP'] = gdp.pct_change()['GDP'].values.flatten()
# regressionFrame['LaggedGDP'] = regressionFrame['GDP'].shift(1)
regressionFrame['Inflation Lag 1'] = regressionFrame['Inflation'].shift(1)
regressionFrame.dropna(inplace=True)

# PERFORM REGRESSION
# X = regressionFrame[['Inflation Lag 1', 'Change In Exports', 'Change In GDP']]
X = regressionFrame[['Change In Total Trade Volume', 'Change In GDP']]
y = regressionFrame['Inflation']
# X2 = sm.add_constant(X)
est = sm.OLS(y, X).fit()
# print(est.summary())


#GBR
#SETUP DATA
goodsAndServices = pd.read_csv('./Data/Goods And Services Data (Long).csv')
gdp = pd.read_csv('./Data/GBR_GDP.csv')
gdp.set_index('DATE', inplace=True)

inflation = pd.read_csv('./Data/GBR Inflation Data (Long).csv')
inflation['DATE'] = pd.DatetimeIndex(inflation['DATE']).year
inflation.set_index('DATE', inplace=True)

gbrGoodsAndServices = goodsAndServices[(goodsAndServices['LOCATION'] == 'GBR')]
gbrGoodsAndServices = gbrGoodsAndServices[gbrGoodsAndServices['FREQUENCY'] == 'A']
gbrGoodsAndServices = gbrGoodsAndServices[gbrGoodsAndServices['MEASURE'] == 'MLN_USD']
gbrGoodsAndServices.rename(columns={'TIME': 'DATE'}, inplace=True)
gbrGoodsAndServices.set_index('DATE', inplace=True)
gbrGoodsAndServicesEXP = gbrGoodsAndServices[gbrGoodsAndServices['SUBJECT'] == 'EXP']
gbrGoodsAndServicesIMP = gbrGoodsAndServices[gbrGoodsAndServices['SUBJECT'] == 'IMP']
gbrGoodsAndServices = gbrGoodsAndServicesEXP
gbrGoodsAndServices.rename(columns={'Value' : 'Exports'}, inplace=True)
gbrGoodsAndServices['Imports'] = gbrGoodsAndServicesIMP[['Value']].values.flatten()
gbrGoodsAndServices['Total Trade Volume'] = gbrGoodsAndServices['Exports'] + gbrGoodsAndServices['Imports']
gbrGoodsAndServices = gbrGoodsAndServices[['Total Trade Volume']]

#MULTICOLLINEARITY
corrFrame = pd.DataFrame()
corrFrame['DATE'] = gbrGoodsAndServices.index
corrFrame.set_index('DATE', inplace=True)
corrFrame['Total Trade Volume'] = gbrGoodsAndServices[['Total Trade Volume']].pct_change()
corrFrame['GDP'] = gdp.pct_change()['GDP'].values.flatten()
corrFrame.dropna(inplace=True)
multicollinearity_check(corrFrame)
# print(corrFrame.corr())

#SETUP REGERESSION DATAFRAME
regressionFrame = pd.DataFrame()
flatInflation = inflation.values.flatten()[10:]
regressionFrame['Inflation'] = flatInflation
regressionFrame.index = gbrGoodsAndServicesEXP.index
regressionFrame['Change In Total Trade Volume'] = gbrGoodsAndServices[['Total Trade Volume']].pct_change()
regressionFrame['Change In GDP'] = gdp.pct_change()['GDP'].values.flatten()
# regressionFrame['LaggedGDP'] = regressionFrame['GDP'].shift(1)
regressionFrame['Inflation Lag 1'] = regressionFrame['Inflation'].shift(1)
regressionFrame.dropna(inplace=True)

# PERFORM REGRESSION
# X = regressionFrame[['Inflation Lag 1', 'Change In Exports', 'Change In GDP']]
X = regressionFrame[['Change In Total Trade Volume', 'Change In GDP']]
y = regressionFrame['Inflation']
# X2 = sm.add_constant(X)
est = sm.OLS(y, X).fit()
# print(est.summary())



