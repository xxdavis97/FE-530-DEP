import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

goods = pd.read_csv('Trade In Goods (Long).csv')
# SETUP GOODS AND SERVICES
gbrGoods = goods[(goods['LOCATION'] == 'GBR')]
gbrGoods = gbrGoods[gbrGoods['FREQUENCY'] == 'A']
gbrGoods.rename(columns={'TIME': 'DATE'}, inplace=True)
gbrGoods.set_index('DATE', inplace=True)
gbrGoods = gbrGoods[3:]

services = pd.read_csv('Trade In Services (Long).csv')
gbrServices = services[(services['LOCATION'] == 'GBR')]
gbrServices = gbrServices[gbrServices['FREQUENCY'] == 'A']
gbrServices.rename(columns={'TIME': 'DATE'}, inplace=True)
gbrServices.set_index('DATE', inplace=True)
gbrServices = gbrServices[3:]

# EXPORTS
gbrGoods = gbrGoods[gbrGoods['SUBJECT'] == 'EXP']
gbrServices = gbrServices[gbrServices['SUBJECT'] == 'EXP']

# INFLATION
inflation = pd.read_csv('GBR Inflation Data (Long).csv')
inflation['DATE'] = pd.DatetimeIndex(inflation['DATE']).year
inflation.set_index('DATE', inplace=True)

# CORRELATIONS
flatInflation = inflation.values.flatten()
GoodsDF = gbrGoods['Value'].to_frame()
GoodsDF['Inflation'] = flatInflation
GoodsInflationCorr = GoodsDF.corr().values[0][1]
print(GoodsInflationCorr)

ServicesDF = gbrServices['Value'].to_frame()
ServicesDF['Inflation'] = flatInflation
ServicesInflationCorr = ServicesDF.corr().values[0][1]
print(ServicesInflationCorr)

# PLOT ORTS
fig = plt.figure()
ax = plt.gca()
ax2 = ax.twinx()
ax.plot(gbrGoods.index, gbrGoods['Value'] / 1000, sns.xkcd_rgb["pale red"], label='British Goods')
ax.plot(gbrServices.index, gbrServices['Value'] / 1000, sns.xkcd_rgb["amber"], label='British Services')
ax2.plot(inflation.index, inflation['FPCPITOTLZGGBR'], label='Inflation')
ax.set_title('British Goods and Services Exports Compared With Inflation')
ax.set_xlabel('Year')
ax.set_ylabel('British Exports (In Billions)')
ax2.set_ylabel('Inflation Rate (%)')
ax.legend()
ax2.legend()
plt.show()



