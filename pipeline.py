import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime


df = pd.read_csv('data/temperature_readings.csv', header=None, names=["id", "room_id", "noted_date", "temp", "location"])


df["noted_date"] = pd.to_datetime(df["noted_date"], format="%d-%m-%Y %H:%M")
df["location"] = df["location"].str.strip()
df.drop_duplicates(inplace=True)


engine = create_engine('postgresql://postgres:senha@localhost:5432/iot_db')
df.to_sql('temperature_readings', engine, if_exists='replace', index=False)
print("Dados importados com sucesso!")
print(f"Total de registros importados: {len(df)}")          