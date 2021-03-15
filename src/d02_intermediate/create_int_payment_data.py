#Je fais le lien avec mon fichier python
from src.d01_data.load_data import *

#j'affiche les valeurs d'une colonne
test = salary_survey_db.unique['CompanyEmployeesOverall']
print(test)

#j'affiche les valeurs d'une colonne
#df_1 = salary_survey_db.loc.head[:,'EmploymentStatus']
#print(df_1)