import pandas as pd
import numpy as np

data_analyst_db = pd.read_csv("/home/apprenant/PycharmProjects/american_dream/data/DataAnalyst.csv")
salary_survey_db = pd.read_excel("/home/apprenant/PycharmProjects/american_dream/data/2020_Data_Professional_Salary_Survey_Responses.xlsx", engine='openpyxl')

print(data_analyst_db.columns)
print(salary_survey_db.columns)
