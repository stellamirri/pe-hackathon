# évolution du bonheur selon les pays entre 2010 et 2022

import pandas as pd 
import numpy as np 
# %pip install xlrd

df = pd.read_excel('Data_bonheur.xlsx')
df

#sélection de l'année 2022
df_2022 = df.loc[df['year'] == 2022]
df_2022

#tri par ordre décroissant de l'échelle de vie
df_2022_trie = df_2022.sort_values(by = 'Life Ladder', axis = 0, ascending=False)
df_2022_trie

df_2022_trie_classement = df_2022_trie.reset_index()
df_2022_trie_classement

df_2022_trie_classement['classement_life_ladder'] = df_2022_trie_classement.index + 1
df_2022_trie_classement

df_2010 = df.loc[df['year'] == 2010]

# +
df_2010 = df.loc[df['year'] == 2010]
ascendant = ['Life Ladder', 'Log GDP per capita', 'Social support', 'Healthy life expectancy at birth', 'Freedom to make life choices', 'Generosity', 'Positive affect']
descendant = ['Perceptions of corruption', 'Negative affect']

for i in ascendant :
    df_2010.set_index('Country name', inplace = True)
    df_2010 = df_2010.sort_values(by = i, axis = 0, ascending=False)
    df_2010.reset_index(inplace = True)
    df_2010['classement', i] = df_2010.index + 1

for j in descendant :
    df_2010.set_index('Country name', inplace = True)
    df_2010 = df_2010.sort_values(by = j, axis = 0, ascending=True)
    df_2010.reset_index(inplace = True)
    df_2010['classement', j] = df_2010.index + 1

df_2010


# +
# code d'Anais

df_2022 = df.loc[df['year'] == 2022]
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



# +
# évolution des points en Life Ladder dans chaque pays entre 2010 et 2022.

pays = df['Country name'].unique()
df_2022_name = df_2022.set_index('Country name')
df_2010_name = df_2010.set_index('Country name')
df_2022['evol']= df_2022['Life Ladder'] - df_2010['Life Ladder']
df_evol = df_2022.loc[:, ['Country name', 'evol']]
df_evol_trie = df_evol.sort_values(by = 'evol' , ascending = False)
df_evol_trie
# -

new_df = df_evol_trie.set_index('Country name')
new_df['evol'].plot(style = 'rv')

# +
#on peut de même tracer l'évolution des autres variables pour chaque pays.

# +
df_2022_name = df_2022.set_index('Country name')
df_2010_name = df_2010.set_index('Country name')
colonnes = ['Life Ladder', 'Log GDP per capita', 'Social support', 'Healthy life expectancy at birth', 'Freedom to make life choices', 'Generosity', 'Positive affect', 'Perceptions of corruption', 'Negative affect']

for c in colonnes : 
    df_2022_name['evol de', c]= df_2022_name[c] - df_2010_name[c]

df_2022_name
# -

france_df = df_2022_name.loc['France', :]
france_df

#je n'ai pas réussi à "plotter" l'évolution des données de la France entre 2010 et 2022 
france_df[('evol de', 'Life Ladder'), ('evol de', 'Log GDP per capita'), ('evol de', 'Social support'), ('evol de', 'Healthy life expectancy at birth'), ('evol de', 'Freedom to make life choices'), ('evol de', 'Generosity'), ('evol de', 'Positive affect'), ('evol de', 'Perceptions of corruption'), ('evol de', 'Negative affect')].plot(style = 'rv')    
