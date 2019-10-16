import pandas as pd
import statsmodels.formula.api as sm

#USA

#SETUP DATA
goodsAndServices = pd.read_csv('Goods And Services Data (Long).csv')
inflation = pd.read_csv('Inflation Data (Long).csv')
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
regressionFrame['Exports'] = usaGoodsAndServicesEXP['Value']

#PERFORM REGRESSION
# Formula would be like Inflation ~ Exports + ...
result = sm.ols(formula="Inflation ~ Exports", data=regressionFrame).fit()
print(result.params)
print(result.summary())


