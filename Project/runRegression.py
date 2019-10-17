import pandas as pd
import statsmodels.api as sm

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
usaGoodsAndServices.rename(columns={'TIME': 'DATE'}, inplace=True)
usaGoodsAndServices.set_index('DATE', inplace=True)
usaGoodsAndServicesEXP = usaGoodsAndServices[usaGoodsAndServices['SUBJECT'] == 'EXP']
usaGoodsAndServicesEXP = usaGoodsAndServicesEXP[usaGoodsAndServicesEXP['MEASURE'] == 'MLN_USD']

#SETUP REGERESSION DATAFRAME
regressionFrame = pd.DataFrame()
flatInflation = inflation.values.flatten()[10:]
regressionFrame['Inflation'] = flatInflation
regressionFrame.index = usaGoodsAndServicesEXP.index
regressionFrame['Change In Exports'] = usaGoodsAndServicesEXP[['Value']].pct_change()
regressionFrame['Change In GDP'] = gdp.pct_change()['GDP'].values.flatten()
# regressionFrame['LaggedGDP'] = regressionFrame['GDP'].shift(1)
regressionFrame['Inflation Lag 1'] = regressionFrame['Inflation'].shift(1)
regressionFrame.dropna(inplace=True)

# PERFORM REGRESSION
# X = regressionFrame[['Inflation Lag 1', 'Change In Exports', 'Change In GDP']]
X = regressionFrame[['Change In Exports', 'Change In GDP']]
y = regressionFrame['Inflation']
# X2 = sm.add_constant(X)
est = sm.OLS(y, X).fit()
print(est.summary())



#GBR

#USA
#SETUP DATA
goodsAndServices = pd.read_csv('./Data/Goods And Services Data (Long).csv')
gdp = pd.read_csv('./Data/GBR_GDP.csv')
gdp.set_index('DATE', inplace=True)

inflation = pd.read_csv('./Data/GBR Inflation Data (Long).csv')
inflation['DATE'] = pd.DatetimeIndex(inflation['DATE']).year
inflation.set_index('DATE', inplace=True)

gbrGoodsAndServices = goodsAndServices[(goodsAndServices['LOCATION'] == 'GBR')]
gbrGoodsAndServices = gbrGoodsAndServices[gbrGoodsAndServices['FREQUENCY'] == 'A']
gbrGoodsAndServices.rename(columns={'TIME': 'DATE'}, inplace=True)
gbrGoodsAndServices.set_index('DATE', inplace=True)
gbrGoodsAndServicesEXP = gbrGoodsAndServices[gbrGoodsAndServices['SUBJECT'] == 'EXP']
gbrGoodsAndServicesEXP = gbrGoodsAndServicesEXP[gbrGoodsAndServicesEXP['MEASURE'] == 'MLN_USD']

#SETUP REGERESSION DATAFRAME
regressionFrame = pd.DataFrame()
flatInflation = inflation.values.flatten()[10:]
regressionFrame['Inflation'] = flatInflation
regressionFrame.index = gbrGoodsAndServicesEXP.index
regressionFrame['Change In Exports'] = gbrGoodsAndServicesEXP[['Value']].pct_change()
regressionFrame['Change In GDP'] = gdp.pct_change()['GDP'].values.flatten()
# regressionFrame['LaggedGDP'] = regressionFrame['GDP'].shift(1)
regressionFrame['Inflation Lag 1'] = regressionFrame['Inflation'].shift(1)
regressionFrame.dropna(inplace=True)

# PERFORM REGRESSION
# X = regressionFrame[['Inflation Lag 1', 'Change In Exports', 'Change In GDP']]
X = regressionFrame[['Change In Exports', 'Change In GDP']]
y = regressionFrame['Inflation']
# X2 = sm.add_constant(X)
est = sm.OLS(y, X).fit()
print(est.summary())



