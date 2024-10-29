import pandas as pd
import matplotlib.pyplot as plt
# %pip install xlrd

df = pd.read_excel('Donnees_2022.xls')

# +
colonnes_descendantes = ['Life Ladder', 'Log GDP per capita', 'Social support', 'Healthy life expectancy at birth', 'Freedom to make life choices','Generosity', 'Positive affect']	#le plus haut le mieux
colonnes_ascendantes = ['Perceptions of corruption', 'Negative affect']  #le plus bas c'est le mieux c'est 

classement_par_annee = pd.DataFrame(index = df['Country name'].unique())

for annee in range(2010,2023):
    
    df_annee = df.loc[df['year'] == annee] 

    for critere in colonnes_descendantes :
        df_annee.set_index( 'Country name', inplace = True) 
        df_annee = df_annee.sort_values(by = critere, ascending = False)
        df_annee.reset_index(inplace = True)
        df_annee['classement', critere ] = 1 + df_annee.index

    for critere in colonnes_ascendantes :
        df_annee.set_index( 'Country name', inplace = True) 
        df_annee = df_annee.sort_values(by = critere, ascending = True)
        df_annee.reset_index(inplace = True)
        df_annee['classement' + critere] = 1 + df_annee.index
    
    df_annee.set_index('Country name', inplace = True)

    df_annee.rename(columns = {('classement', 'Life Ladder') : 'classement Life Ladder', ('classement', 'Log GDP per capita'): 'classement Log GDP per capita',
                        ('classement', 'Social support') : 'classement Social support',
       ('classement', 'Healthy life expectancy at birth') : 'classement Healthy life expectancy at birth',
           ('classement', 'Freedom to make life choices'): 'classement Freedom to make life choices',
                             ('classement', 'Generosity'): 'classement Generosity',
                        ('classement', 'Positive affect'): 'classement Positive affect',
                    'classementPerceptions of corruption': 'classement Perceptions of corruption',
                              'classementNegative affect': 'classement Negative affect'}, inplace = True)


    df_annee_classement = df_annee.loc[:,'classement Life Ladder' : 'classement Negative affect']
    df_annee_classement['somme classements'] = df_annee_classement.sum(axis =1) 
    df_annee_classement.sort_values(by = 'somme classements', inplace = True)
    df_annee_classement.reset_index(inplace = True)
    df_annee_classement['classement général'] = 1 + df_annee_classement.index 
    df_annee_classement.set_index('Country name', inplace = True) 

    classement_par_annee[annee] = df_annee_classement['classement général']

classement_par_annee

# +
bis = classement_par_annee.T

#Exemples de l'évolution d'un classement pour des pays

bis['Sweden'].plot(marker = 'o')
bis['Finland'].plot(marker = 'o')
bis['State of Palestine'].plot(marker = 'o')
bis['Lebanon'].plot(marker = 'o')
plt.ylabel('classement')
plt.xlabel('année')
plt.show()
