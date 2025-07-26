import pandas as pd
from sqlalchemy import create_engine
from snowflake.sqlalchemy import URL  # Importação correta da URL do Snowflake

# PostgreSQL configs
p_user = 'postgres_user'
p_password = 'postgres_password'
p_host = 'postgres_host'
p_port = 'postgres_port'
p_database = 'postgres_database'

# Snowflake configs
s_user = "snowflake_user"
s_password = "snowflake_password"
s_account = "snowflake_account"
s_warehouse = "snowflake_wharehouse"
s_database = "snowflake_database"
s_schema = "snowflake_schema"

# Engine para o PostgreSQL
source = create_engine(f'postgresql+psycopg2://{p_user}:{p_password}@{p_host}:{p_port}/{p_database}')

# Engine para o Snowflake (forma correta de montar a URL)
destination = create_engine(
    URL(
        user=s_user,
        password=s_password,
        account=s_account,
        warehouse=s_warehouse,
        database=s_database,
        schema=s_schema,
    )
)

# Query do PostgreSQL
query = 'SELECT * FROM wharehouse.products'

# Carregando do PostgreSQL
df = pd.read_sql(query, source)

# Enviando para Snowflake
# Primeiro campo representa o nome da nova tabela no snowflake
df.to_sql('products', destination, schema=s_schema, if_exists='replace', index=False)