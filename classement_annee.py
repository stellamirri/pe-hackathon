# %pip install xlrd

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# OBJECTIF : regarder le lien entre les différents critères

df = pd.read_excel('Donnees_2022.xls')

sub_df = df.loc[df['year'] == 2022]

# Réalisation de la table classée 

# +
#le classement doit prendre les plus grandes valeurs de life ladder, lig GDP, social support, 
#life expectancy, freedom, generosity, positive affect 
# ce qui doit être bas  : perception of cooruption, negative affect
# pour chaque critère ajouter une colonne puis sommer les valeurs horizontalement
# -

liste_desc = ['Negative affect', 'Perceptions of corruption']
for critere in liste_desc :
    sub_df = sub_df.set_index('Country name')
    sub_df = sub_df.sort_values(by = critere, axis = 0, ascending = True)
    sub_df = sub_df.reset_index()
    sub_df['classement', critere] = sub_df.index +1

liste = ['Life Ladder', 'Log GDP per capita', 'Social support',
       'Healthy life expectancy at birth', 'Freedom to make life choices',
       'Generosity', 'Positive affect']
for critere in liste :
    sub_df = sub_df.set_index('Country name')
    sub_df = sub_df.sort_values(by = critere, axis = 0, ascending = False)
    sub_df = sub_df.reset_index()
    sub_df['classement', critere] = sub_df.index +1

sub_df.columns

sous_df = sub_df.loc[:,['Country name',('classement', 'Negative affect'),
              ('classement', 'Perceptions of corruption'),
                            ('classement', 'Life Ladder'),
                     ('classement', 'Log GDP per capita'),
                         ('classement', 'Social support'),
       ('classement', 'Healthy life expectancy at birth'),
           ('classement', 'Freedom to make life choices'),
                             ('classement', 'Generosity'),
                        ('classement', 'Positive affect')]]
sous_df

sous_df = sous_df.set_index('Country name')
sous_df

sous_df = sous_df.T
sous_df.plot()
#on ne voit pas de dynamique globale

sous_df.index = ['Negative affect', 'Perceptions of corruption', 'Life Ladder', 'Log GDP per capita', 'Social support', 'Healthy life expectancy at birth', 'Freedom to make life choices', 'Generosity', 'Positive affect']
sous_df.plot()
plt.xticks(rotation=90)
plt.show()

# On ne remarque pas d'évolution typique entre les critères.
#
# Il y a-t-il un lien entre la richesse et le bonheur ?

pays_riches = ['Luxembourg', 'Ireland', 'United Arab Emirates', 'Switzerland', 'Norway']
riche_df = sous_df.loc[:, pays_riches]
riche_df.plot(kind = 'bar')
plt.xticks(rotation=90)
plt.show()

sous_df

# Mais quid de la France ?

france_df = sous_df.loc[:, 'France']
france_df = france_df.sort_values(axis = 0)
france_df.plot(kind = 'bar')
plt.xticks(rotation=90)
plt.show()

# Lien entre negative affect et positive affect

# +
affect_df = sous_df.loc[['Negative affect', 'Positive affect']]

affect_df.plot()
# -

# On remarque que les pays mal classés en négative affect le sont aussi en positive affect, alors qu'il y a plus de mobilité avec les pays bien classés en positive affect ou negative affect.

lux_df = sous_df.loc[:, 'Luxembourg']
lux_df = lux_df.sort_values(axis = 0)
lux_df.plot(kind = 'bar')
plt.xticks(rotation=90)
plt.show()

viet_df = sous_df.loc[:, 'Vietnam']
viet_df = viet_df.sort_values(axis = 0)
viet_df.plot(kind = 'bar')
plt.xticks(rotation=90)
plt.show()

liban_df = sous_df.loc[:, 'Lebanon']
liban_df = liban_df.sort_values(axis = 0)
liban_df.plot(kind = 'bar')
plt.xticks(rotation=90)
plt.show()

nicar_df = sous_df.loc[:, 'Nicaragua']
nicar_df = nicar_df.sort_values(axis = 0)
nicar_df.plot(kind = 'bar')
plt.xticks(rotation=90)
plt.show()

finland_df = sous_df.loc[:, 'Finland']
finland_df = finland_df.sort_values(axis = 0)
finland_df.plot(kind = 'bar')
plt.xticks(rotation=90)
plt.show()

# Peut-on relier richesse et générosité ?

plt.plot(sous_df.loc['Generosity'], sous_df.loc['Log GDP per capita'], 'o')


