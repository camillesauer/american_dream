import pandas as pd
import numpy as np
import mysql.connector
import sqlalchemy
import pymysql

#je me connecte à sql
mydb = mysql.connector.connect(
  host="localhost",
  user="student",
  database="american_dream_db",
  password="PanapoiC19!"
)

#je me connecte à ma première db
engine = sqlalchemy.create_engine("mysql+pymysql://student:PanapoiC19!@localhost/american_dream_db")


#Je crée la db dans laquelle je vais stocker mon dataframe
# mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE american_dream_db")

#Je lis mes deux fichiers et les insère dans un DataFrame
data_analyst_db = pd.read_csv("/home/apprenant/PycharmProjects/american_dream/data/DataAnalyst.csv")
salary_survey_db = pd.read_excel("/home/apprenant/PycharmProjects/american_dream/data/2020_Data_Professional_Salary_Survey_Responses.xlsx", engine='openpyxl', skiprows=3)

#j'affiche les colonnes de mon premier fichier
# print(data_analyst_db.columns)
#j'affiche les colonnes de mon second fichier
# print(salary_survey_db.columns)

# j'insère la data du fichier csv et excel dans la db sql et crée deux tables distinctes
# salary_survey_db.to_sql('SalarySurvey', engine, if_exists='replace', index=False)
# data_analyst_db.to_sql('DataAnalyst', engine, if_exists='replace', index=False)

#j'enregistre mes dataframes dans mysql
def save_to_mysql(db_connect, df_to_save, df_name):
  df_to_save.to_sql(con=db_connect, name=df_name, if_exists='replace')
