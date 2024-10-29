import pandas as pd
import numpy as np

score_region = pd.csv.read('')'''on attend ici la data frame du classement par pays (classement 1D)'''
pays_region = pd.read_csv('correspondance_pays_region.csv')
regions = pays_region.unique()
score_group_region = score_region.set_index('name_fr').groupby(by = )