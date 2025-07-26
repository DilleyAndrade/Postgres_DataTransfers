import pandas as pd
from sqlalchemy import create_engine
import boto3

#Postgres connection informations
user='postgres_user'
password='postgres_password'
host='postgres_host'
port='postgres_port'
database='postgres_database'
schema = 'postgres_schema'

engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}')

#S3 connection information
s3_bucket = 'bucket_name'

s3_client = boto3.client(
  's3',
  aws_access_key_id = 'access_key_id',
  aws_secret_access_key = 'secret_access_key',
  region_name = 'region'
)

#Create a list with all tables in the schema
search_tables_query = f"select table_name from information_schema.tables where table_schema = '{schema}' and table_type <> 'VIEW'"
df_search_tables = pd.read_sql(search_tables_query, engine)
table_list = df_search_tables['table_name']

#Create csv with postgres tables
for table_name in table_list:
  #Read tables and convert to csv
  select_table_query = f'select * from {schema}.{table_name}'
  df = pd.read_sql(select_table_query, engine)
  df.to_csv(f'csv_files/{table_name}.csv', sep=';', index=False)
  
  #Send to S3
  s3_directory = f'{table_name}.csv' 
  s3_client.upload_file(f'csv_files/{table_name}.csv', s3_bucket, s3_directory)
  print(f'File {table_name}.csv sended to S3')