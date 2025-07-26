# 🚀 Enviando Dados para Snowflake e AWS(S3) com Python, SQLAlchemy e Pandas

> Um exemplo prático de como conectar Python ao Snowflake e AWS(S3) e enviar dados de um DataFrame utilizando SQLAlchemy e Pandas.

---

## 📌 Sobre o Projeto

Este projeto demonstra como configurar uma conexão entre Python e Snowflake/AWS(S3) usando SQLAlchemy, e como carregar dados diretamente de um DataFrame Pandas para uma tabela no Snowflake ou bucket S3. É uma abordagem ideal para cargas pequenas ou integrações rápidas via script.

---

## 📦 Tecnologias Utilizadas

- [Python 3.10+](https://www.python.org/)
- [Pandas](https://pandas.pydata.org/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Snowflake SQLAlchemy Dialect](https://docs.snowflake.com/en/user-guide/sqlalchemy)
- [Snowflake Connector for Python](https://docs.snowflake.com/en/developer-guide/python-connector)
- [Aws](https://aws.amazon.com/)

---

## ⚙️ Como usar

1. **Configure as credenciais do Postgre, Snowflake e S3** no script `main.py`:

```python
user='postgres_user'
password='postgres_password'
host='postgres_host'
port='postgres_port'
database='postgres_database'
schema = 'postgres_schema'
```

```python
user = "SEU_USUARIO"
password = "SUA_SENHA"
account = "SEU_ACCOUNT_ID"
warehouse = "SEU_WAREHOUSE"
database = "SEU_DATABASE"
schema = "SEU_SCHEMA"
```

```python
s3_client = boto3.client(
  's3',
  aws_access_key_id = 'access_key_id',
  aws_secret_access_key = 'secret_access_key',
  region_name = 'region'
)
```

2. **Execute o script principal**:

```bash
python postgre_to_s3.py
python postgre_to_snowflake.py
``'
---

## 📂 Estrutura do Projeto

```
.
├── mapostgre_to_snowflaken.py  # Script principal que envia os dados para o snowflake
├── postgre_to_s3               # Script principal que envia os dados para o S3
├── csv_files                   # Pasta onde os arquivos csv são salvos antes de ir para o s3
└── README.md                   # Este arquivo
```

---

## 🛑 Problemas comuns

- ❌ **Incorrect username or password**  
  Verifique se o usuário e senha estão corretos e não contém espaços extras.

- ❌ **User account locked**  
  Aguarde ou contate o administrador Snowflake para desbloquear. Evite múltiplas tentativas seguidas.

---

## 👤 Autor

**Dilley Andrade**  
Engenheiro de Dados | SQL | ETL | Python — Focado em soluções de dados, ETL, BI e engenharia de dados. (81) 98663-2609 | dilleyandrade@gmail.com | http://linkedin.com/in/dilleyandrade | http://github.com/DilleyAndrade

---

## 📃 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
