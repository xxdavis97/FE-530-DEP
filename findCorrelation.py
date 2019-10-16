import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

goods = pd.read_csv('Trade In Goods (Long).csv')
# SETUP GOODS AND SERVICES
usaGoods = goods[(goods['LOCATION'] == 'USA')]
usaGoods = usaGoods[usaGoods['FREQUENCY'] == 'A']
usaGoods.rename(columns={'TIME': 'DATE'}, inplace=True)
usaGoods.set_index('DATE', inplace=True)

services = pd.read_csv('Trade In Services (Long).csv')
usaServices = services[(services['LOCATION'] == 'USA')]
usaServices = usaServices[usaServices['FREQUENCY'] == 'A']
usaServices.rename(columns={'TIME': 'DATE'}, inplace=True)
usaServices.set_index('DATE', inplace=True)

goodsAndServices = pd.read_csv('Goods And Services Data (Long).csv')
usaGoodsAndServices = goodsAndServices[(goodsAndServices['LOCATION'] == 'USA')]
usaGoodsAndServices = usaGoodsAndServices[usaGoodsAndServices['FREQUENCY'] == 'A']
usaGoodsAndServices.rename(columns={'TIME': 'DATE'}, inplace=True)
usaGoodsAndServices.set_index('DATE', inplace=True)
usaGoodsAndServicesEXP = usaGoodsAndServices[usaGoodsAndServices['SUBJECT'] == 'EXP']
usaGoodsAndServicesEXP = usaGoodsAndServicesEXP[usaGoodsAndServicesEXP['MEASURE'] == 'MLN_USD']

# EXPORTS
usaGoodsEXP = usaGoods[usaGoods['SUBJECT'] == 'EXP']
usaServicesEXP = usaServices[usaServices['SUBJECT'] == 'EXP']
# IMPORTS
usaGoodsIMP = usaGoods[usaGoods['SUBJECT'] == 'EXP']
usaServicesIMP = usaServices[usaServices['SUBJECT'] == 'EXP']

# INFLATION
inflation = pd.read_csv('Inflation Data (Long).csv')
inflation['DATE'] = pd.DatetimeIndex(inflation['DATE']).year
inflation.set_index('DATE', inplace=True)

# CORRELATIONS
flatInflation = inflation.values.flatten()
expGoodsDF = usaGoodsEXP['Value'].to_frame()
expGoodsDF['Inflation'] = flatInflation
expGoodsInflationCorr = expGoodsDF.corr().values[0][1]
print(expGoodsInflationCorr)

expServicesDF = usaServicesEXP['Value'].to_frame()
expServicesDF['Inflation'] = flatInflation
expServicesInflationCorr = expServicesDF.corr().values[0][1]
print(expServicesInflationCorr)

# Correlation between goods/services combined (-.627)
expGoodsAndServicesDF = usaGoodsAndServicesEXP['Value'].to_frame()
expGoodsAndServicesDF['Inflation'] = flatInflation[10:]
expGoodsAndServicesInflationCorr = expGoodsAndServicesDF.corr().values[0][1]
print(expGoodsAndServicesInflationCorr)


impGoodsDF = usaGoodsIMP['Value'].to_frame()
impGoodsDF['Inflation'] = flatInflation
impGoodsInflationCorr = impGoodsDF.corr().values[0][1]
print(impGoodsInflationCorr)

impServicesDF = usaServicesIMP['Value'].to_frame()
impServicesDF['Inflation'] = flatInflation
impServicesInflationCorr = impServicesDF.corr().values[0][1]
print(impServicesInflationCorr)

# PLOT EXPORTS
fig = plt.figure()
ax = plt.gca()
ax2 = ax.twinx()
ax.plot(usaGoodsEXP.index, usaGoodsEXP['Value'] / 1000, sns.xkcd_rgb["pale red"], label='US Goods')
ax.plot(usaServicesEXP.index, usaServicesEXP['Value'] / 1000, sns.xkcd_rgb["amber"], label='US Services')
ax2.plot(inflation.index, inflation['FPCPITOTLZGUSA'], label='Inflation')
ax.set_title('US Goods and Services Exports Compared With Inflation')
ax.set_xlabel('Year')
ax.set_ylabel('US Exports (In Billions)')
ax2.set_ylabel('Inflation Rate (%)')
ax.legend()
ax2.legend()
# plt.show()

# GOODS AND SERVICES
plt.clf()
ax = plt.gca()
ax2 = ax.twinx()
ax.plot(usaGoodsAndServicesEXP.index, usaGoodsAndServicesEXP['Value'] / 1000, sns.xkcd_rgb["pale red"], label='US Goods And Services')
ax2.plot(inflation.index, inflation['FPCPITOTLZGUSA'], label='Inflation')
ax.set_title('US Goods and Services Exports Compared With Inflation')
ax.set_xlabel('Year')
ax.set_ylabel('US Exports (In Billions)')
ax2.set_ylabel('Inflation Rate (%)')
ax.legend()
ax2.legend()
plt.show()

# PLOT IMPORTS
# plt.clf()
# ax = plt.gca()
# ax2 = ax.twinx()
# ax.plot(usaGoodsIMP.index, usaGoodsIMP['Value'] / 1000, sns.xkcd_rgb["pale red"], label='US Goods')
# ax.plot(usaServicesIMP.index, usaServicesIMP['Value'] / 1000, sns.xkcd_rgb["amber"], label='US Services')
# ax2.plot(inflation.index, inflation['FPCPITOTLZGUSA'], label='Inflation')
# ax.set_title('US Goods and Services Imports Compared With Inflation')
# ax.set_xlabel('Year')
# ax.set_ylabel('US Exports (In Billions)')
# ax2.set_ylabel('Inflation Rate (%)')
# ax.legend()
# ax2.legend()
# plt.show()



