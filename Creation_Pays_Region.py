import pandas as pd
import numpy as np
df = pd.read_excel("Donnees_2022.xls")
#print(df.head(3))
#print(df['Country name'].unique().size)
region_colonnes =['name_fr','south_america', 'central_america_caraibes','continental_europe', 'asia_oceania','central_europe_and_the_baltics', 'east_asia_pacific', 'euro_area','europe_central_asia', 'european_union', 'latin_america_caribbean', 'middle_east_north_africa', 'north_america','sub_saharan_africa']
dg =pd.read_csv('liste_pays_et_continents.csv', sep = ";", usecols = region_colonnes, index_col=['name_fr'])
print(dg.head(3))#dg['name_fr'].unique().size == dg['name_fr'].size)
print(dg.index)
dg['Region']= ''
for region in dg.columns:
    dg.loc[dg[region]==True,'Region'] = region
dg.loc[:,['Region']].to_csv('correspondance_pays_region.csv')

