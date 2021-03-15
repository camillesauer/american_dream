#Je fais le lien avec mon fichier python
from src.d01_data.load_data import *

#j'affiche les valeurs d'une colonne
# test = salary_survey_db.unique['CompanyEmployeesOverall']
# print(test)


engine = sqlalchemy.create_engine("mysql+pymysql://student:PanapoiC19!@localhost/american_dream_db")
df = pd.read_sql('SELECT * FROM DataAnalyst', con=engine)
print(df.columns)

df1 = pd.read_sql('SELECT * FROM SalarySurvey', con=engine)
print(df1.columns)

#Je supprime les colonnes dont je n'ai pas besoin dans les tables
# mycursor = mydb.cursor()
# mycursor.execute("ALTER TABLE "DataAnalyst" DROP "column_name"; american_dream_db")

# mycursor.execute("ALTER TABLE "SalarySurvey" DROP "column_name"; american_dream_db")
