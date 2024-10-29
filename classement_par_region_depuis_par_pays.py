import pandas as pd
import numpy as np

raw_data = pd.read_excel('Donnees_2022.xls')
print(raw_data.head(2))
per_year_data = raw_data.groupby (by = 'year')
data_2011 = per_year_data.get_group(2011)#.set_index(['Coutry name'], inplace = True)
data_2011.set_index('Country name', inplace = True)
print(data_2011.head(2))

score_pays = data_2011#pd.read_csv('liste_pays_et_continents.csv', sep = ";", usecols = ['name_en']) #on attend ici la data frame du classement par pays (classement 1D)'''
pays_region = pd.read_csv('correspondance_pays_region.csv', index_col = ['name_en'])

#score_pays.set_index('name_en', inplace = True)
pays_region = pays_region.loc[score_pays.index,:]

regions = pays_region['Region'].unique()
score_group_pays = score_pays.groupby(by = pays_region['Region'])
print(score_group_pays.sum())
