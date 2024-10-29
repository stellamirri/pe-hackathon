import pandas as pd
# %pip install xlrd

df = pd.read_excel('Donnees_2022.xls')

# Dans cette partie, on cherche à réétablir le classement des pays selon leur bonheur pour l'année 2022. Pour cela, on choisit une approche simple où tous les critères ont le même poids. La démarche est la suivante :
# 1- on classe les pays pour chaque critère ;
# 2- on fait la somme de leurs classements ; 
# 3- le pays ayant la somme la plus petite est le plus heureux.

df_2022 = df.loc[df['year'] == 2022]  # on crée un sous-tableau pour l'année 2022
df_2022

# +
# On veut obtenir les classements de chaque pays par critère.

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
    df_2022['classement' + critere] = 1 + df_2022.index
    
df_2022.set_index('Country name', inplace = True)

df_2022.rename(columns = {('classement', 'Life Ladder') : 'classement Life Ladder', ('classement', 'Log GDP per capita'): 'classement Log GDP per capita',
                        ('classement', 'Social support') : 'classement Social support',
       ('classement', 'Healthy life expectancy at birth') : 'classement Healthy life expectancy at birth',
           ('classement', 'Freedom to make life choices'): 'classement Freedom to make life choices',
                             ('classement', 'Generosity'): 'classement Generosity',
                        ('classement', 'Positive affect'): 'classement Positive affect',
                    'classementPerceptions of corruption': 'classement Perceptions of corruption',
                              'classementNegative affect': 'classement Negative affect'}, inplace = True) #on renomme les colonnes pour avoir quelque chose de clair


df_2022

# +
#On veut obtenir le classement général de chaque pays. 
#Pour chaque pays, on fait la somme de tous ses classements. 
#Le pays ayant la somme la plus faible est le plus heureux.

df_2022_classement = df_2022.loc[:,'classement Life Ladder' : 'classement Negative affect'] #on crée un sous-tableau contenant que les classements par critère
df_2022_classement['somme classements'] = df_2022_classement.sum(axis =1) #on crée une nouvelle colonne contenant la somme des classements du pays
df_2022_classement.sort_values(by = 'somme classements', inplace = True)
df_2022_classement.reset_index(inplace = True)
df_2022_classement['classement général'] = 1 + df_2022_classement.index #on s'arrange pour créer une colonne contenant le classement général du pays
df_2022_classement.set_index('Country name', inplace = True)
df_2022_classement
