import pandas as pd
import os
from sqlalchemy import create_engine
import logging
import time

logging.basicConfig(
    filename = "logs/.log",
    level = logging.DEBUG,
    format = "%(asctime)$ - %(levelname)$ - %(message)$",
    filemode = "a"

)

engine = create_engine('sqlite:///inventory_database.db')

def ingest_db(df, table_name, engine):
  """" ingeste the data in database  """
  df.to_sql(table_name, con = engine, if_exists= 'append', index = False, chunksize = 5000)


def load_raw_data():
  """ Loads raw data from CSV files as DataFrame and ingests it into the database. """
  start = time.time
  for file in os.listdir('/content/drive/MyDrive/Colab Notebooks/data'):
    if '.csv' in file:
      df = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/data/' + file)
      logging.info(f'Ingesting {file} in db')
      print(df.shape,file)
      ingest_db(df, file[:4],engine)
  end = time.time
  total_time = (end-start)/60

  logging.info(f'\nTotal Time taken : {total_time} minutes')
  logging.info('---------------Ingestion Complete---------------')

if __name__ == '__main__':
  load_raw_data()

