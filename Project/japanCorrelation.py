import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

goods = pd.read_csv('./Data/Trade In Goods (Long).csv')
# SETUP GOODS AND SERVICES
jpnGoods = goods[(goods['LOCATION'] == 'JPN')]
jpnGoods = jpnGoods[jpnGoods['FREQUENCY'] == 'A']
jpnGoods.rename(columns={'TIME': 'DATE'}, inplace=True)
jpnGoods.set_index('DATE', inplace=True)

services = pd.read_csv('./Data/Trade In Services (Long).csv')
jpnServices = services[(services['LOCATION'] == 'JPN')]
jpnServices = jpnServices[jpnServices['FREQUENCY'] == 'A']
jpnServices.rename(columns={'TIME': 'DATE'}, inplace=True)
jpnServices.set_index('DATE', inplace=True)

# EXPORTS
jpnGoods = jpnGoods[jpnGoods['SUBJECT'] == 'EXP']
jpnServices = jpnServices[jpnServices['SUBJECT'] == 'EXP']

# INFLATION
inflation = pd.read_csv('./Data/Japan Inflation Data (Long).csv')
inflation['DATE'] = pd.DatetimeIndex(inflation['DATE']).year
inflation.set_index('DATE', inplace=True)

# CORRELATIONS
flatInflation = inflation.values.flatten()[36:]
print(len(flatInflation), jpnGoods['Value'].size)
GoodsDF = jpnGoods['Value'].to_frame()
GoodsDF['Inflation'] = flatInflation
GoodsInflationCorr = GoodsDF.corr().values[0][1]
print(GoodsInflationCorr)

ServicesDF = jpnServices['Value'].to_frame()
ServicesDF['Inflation'] = flatInflation
ServicesInflationCorr = ServicesDF.corr().values[0][1]
print(ServicesInflationCorr)

# PLOT EXPORTS
fig = plt.figure()
ax = plt.gca()
ax2 = ax.twinx()
ax.plot(jpnGoods.index, jpnGoods['Value'] / 1000, sns.xkcd_rgb["pale red"], label='Japanese Goods')
ax.plot(jpnServices.index, jpnServices['Value'] / 1000, sns.xkcd_rgb["amber"], label='Japanese Services')
ax2.plot(inflation.index[36:], inflation['FPCPITOTLZGJPN'][36:], label='Inflation')
ax.set_title('Japanese Goods and Services Exports Compared With Inflation')
ax.set_xlabel('Year')
ax.set_ylabel('Japanese Exports (In Billions)')
ax2.set_ylabel('Inflation Rate (%)')
ax.legend()
ax2.legend()
plt.show()



