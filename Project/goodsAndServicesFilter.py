import pandas as pd

goodsAndServices = pd.read_csv('./Data/Goods And Services Data (Long).csv')
usaGoodsAndServices = goodsAndServices[(goodsAndServices['LOCATION'] == 'USA')]
usaGoodsAndServices = usaGoodsAndServices[usaGoodsAndServices['FREQUENCY'] == 'A']
usaGoodsAndServices.rename(columns={'TIME': 'DATE'}, inplace=True)
usaGoodsAndServices.set_index('DATE', inplace=True)
usaGoodsAndServicesEXP = usaGoodsAndServices[usaGoodsAndServices['SUBJECT'] == 'EXP']
usaGoodsAndServicesEXP = usaGoodsAndServicesEXP[usaGoodsAndServicesEXP['MEASURE'] == 'MLN_USD']
usaGoodsAndServicesEXP.to_csv('./Data/USA-Goods-And-Services_Filtered.csv')

gbrGoodsAndServices = goodsAndServices[(goodsAndServices['LOCATION'] == 'GBR')]
gbrGoodsAndServices = gbrGoodsAndServices[gbrGoodsAndServices['FREQUENCY'] == 'A']
gbrGoodsAndServices.rename(columns={'TIME': 'DATE'}, inplace=True)
gbrGoodsAndServices.set_index('DATE', inplace=True)
gbrGoodsAndServicesEXP = gbrGoodsAndServices[gbrGoodsAndServices['SUBJECT'] == 'EXP']
gbrGoodsAndServicesEXP = gbrGoodsAndServicesEXP[gbrGoodsAndServicesEXP['MEASURE'] == 'MLN_USD']
gbrGoodsAndServicesEXP.to_csv('./Data/GBR-Goods-And-Services_Filtered.csv')