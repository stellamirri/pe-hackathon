import pandas as pd

# %pip install openpyxl

# %pip install xlrd

df = pd.read_excel('Donnees_2022.xls')

df

df_2022 = df.loc[df['year'] == 2022]  # on crée un sous-tableau pour l'année 2022
#df_2022.set_index('Country name', inplace = True) 
#df_2022 = df_2022.sort_values(by = 'Life Ladder', ascending = False)
#df_2022.reset_index(inplace = True)
#df_2022['classement Life Ladder'] = 1 + df_2022.index
df_2022

# +
colonnes_descendantes = ['Life Ladder', 'Log GDP per capita', 'Social support', 'Healthy life expectancy at birth', 'Freedom to make life choices','Generosity', 'Positive affect']	#le plus haut le mieux
colonnes_ascendantes = ['Perceptions of corruption', 'Negative affect']  #le plus bas c'est le mieux c'est 

for critere in colonnes_descendantes :
    df_2022.set_index( 'Country name', inplace = True) 
    df_2022 = df_2022.sort_values(by = critere, ascending = False)
    df_2022.reset_index(inplace = True)
    df_2022['classement', critere ] = 1 + df_2022.index

for critere in colonnes_ascendantes :
    df_2022.set_index( 'Country name', inplace = True) 
    df_2022 = df_2022.sort_values(by = critere, ascending = True)
    df_2022.reset_index(inplace = True)
    df_2022['classement', critere ] = 1 + df_2022.index
    
df_2022

# -


