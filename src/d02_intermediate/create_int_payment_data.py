#Je fais le lien avec mon fichier python
from src.d01_data.load_data import *

#j'affiche les valeurs d'une colonne
# test = salary_survey_db.unique['CompanyEmployeesOverall']
# print(test)


engine = sqlalchemy.create_engine("mysql+pymysql://student:PanapoiC19!@localhost/american_dream_db")

#J'affiche un échantillon de mes données pour analyser la pertinence des différentes colonnes
df = pd.read_sql('SELECT * FROM DataAnalyst', con=engine)
# print(df.columns)

#J'affiche un échantillon de mes données pour analyser la pertinence des différentes colonnes
df1 = pd.read_sql('SELECT * FROM SalarySurvey', con=engine)
# print(df1.columns)

"""
Je supprime les colonnes dont je n'ai pas besoin dans les tables
mycursor = mydb.cursor()
mycursor.execute("ALTER TABLE "DataAnalyst" DROP "column_name"; american_dream_db")
mycursor.execute("ALTER TABLE "SalarySurvey" DROP "column_name"; american_dream_db")

ou

Je choisis uniquement les colonnes qui pourraient m'être utiles pour mon étude

df1 = df1[['SalaryUSD','Country','PostalCode','EmploymentStatus','JobTitle','ManageStaff','YearsWithThisTypeOfJob',
          'HowManyCompanies','OtherPeopleOnYourTeam', 'CompanyEmployeesOverall',
          'PopulationOfLargestCityWithin20Miles','EmploymentSector', 'LookingForAnotherJob', 'CareerPlansThisYear',
          'Gender', 'OtherJobDuties']]
          
df = df[['Job Title', 'Location', 'Company Name', 'Size', 'Revenue', 'Sector', 'Salary Estimate', 'Type of ownership']]
"""

# Visualiser le nombre de valeurs nulles
# print(df1.isnull().sum())
# print(df1.shape)

#Voir les valeurs sans les valeurs nulles + je compte leur nombre
# print(df1.OtherJobDuties.unique())
# print(df1.OtherJobDuties.value_counts())

#Je regarde s'il y a des dates
# print(df1.dtypes)

#Je regarde s'il y a des valeurs doubles
# print(df1.duplicated().value_counts())
# il n'y a que des false il n'y a donc pas de doublons
# s'il y avait eu doublon j'aurais utilisé un dropduplicate