import pandas as pd
from sqlalchemy import create_engine
import urllib

df=pd.read_excel("Time Series Project\Finals\Islamabad_Data.xlsx")



#create connection string
params=urllib.parse.quote_plus(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost\\SQLEXPRESS;"
    "DATABASE=WeatherForecast;"
    "Trusted_Connection=yes;"
)
#Create engine object
engine=create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)
#transfer data from excel to sql
df.to_sql('Islamabad',con=engine,index=False,if_exists="replace")
print("successfully stored...")