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

engine = sqlalchemy.create_engine("mysql+pymysql://student:PanapoiC19!@localhost/american_dream_db")

#Je créer la db dans laquelle je vais stocker mon dataframe
# mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE american_dream_db")

#Je lis mes deux fichiers et les insère dans un DataFrame
data_analyst_db = pd.read_csv("/home/apprenant/PycharmProjects/american_dream/data/DataAnalyst.csv")
salary_survey_db = pd.read_excel("/home/apprenant/PycharmProjects/american_dream/data/2020_Data_Professional_Salary_Survey_Responses.xlsx", engine='openpyxl', skiprows=3)

#j'affiche les colonnes de mon premier fichier
print(data_analyst_db.columns)
#j'affiche les colonnes de mon second fichier
print(salary_survey_db.columns)

# j'insère la data du fichier csv dans la db sql
# data_analyst_db.to_sql('Job Title', engine, if_exists='replace', index=False)
# data_analyst_db.to_sql('Location', engine, if_exists='replace', index=False)
# data_analyst_db.to_sql('Company Name', engine, if_exists='replace', index=False)
# data_analyst_db.to_sql('Size', engine, if_exists='replace', index=False)
# data_analyst_db.to_sql('Revenue', engine, if_exists='replace', index=False)
# data_analyst_db.to_sql('Sector', engine, if_exists='replace', index=False)
# data_analyst_db.to_sql('Salary Estimate', engine, if_exists='replace', index=False)
# data_analyst_db.to_sql('Type of ownership', engine, if_exists='replace', index=False)

