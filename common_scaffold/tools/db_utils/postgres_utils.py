import pandas as pd
from common_scaffold.tools.BaseTool import FatalError
from common_scaffold.tools.db_utils import db_config
import sqlalchemy
import psycopg2
import os
import subprocess
import logging

"""
Postgres Config:
- db_type
- db_name
- sql_file
"""

# Reference: https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-database#install-postgresql

def pg_ident(identifier: str) -> str:
    """Safely quote PostgreSQL identifiers."""
    return '"' + identifier.replace('"', '""') + '"'


def load_db(sql_file: str, db_name: str):
    if check_db_exists(db_name):
        logging.getLogger(__name__).warning(f"Database '{db_name}' already exists. Cleaning up before loading dump.")
        clean_up(db_name)
        # raise FatalError(f"Database '{db_name}' already exists. Cannot load dump into existing database.")
    try:
        logging.getLogger(__name__).debug(f"Loading PostgreSQL dump from '{sql_file}' into database '{db_name}'")
        conn = psycopg2.connect(
            dbname="postgres",
            user=db_config.PG_USER,
            password=db_config.PG_PASSWORD,
            host=db_config.PG_HOST,
            port=db_config.PG_PORT,
        )
        conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
        cur = conn.cursor()
        # Create the database
        cur.execute(f"CREATE DATABASE {pg_ident(db_name)} WITH ENCODING = \'UTF8\' LC_COLLATE=\'C\' LC_CTYPE=\'C\' TEMPLATE=template0;")
        cur.close()
        conn.close()

        cmd = [
            db_config.PG_CLIENT,
            f"-h{db_config.PG_HOST}",
            f"-U{db_config.PG_USER}",
            "-d", db_name,
            "-f", sql_file
        ]
        env = os.environ.copy()
        env["PGPASSWORD"] = db_config.PG_PASSWORD
        env["PGCLIENTENCODING"] = "UTF8"
        # subprocess.run(cmd, check=True, env=env)
        result = subprocess.run(cmd, check=True, env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.stdout:
            logging.getLogger(__name__).debug(f"PostgreSQL load stdout: {result.stdout}")
        if result.stderr:
            logging.getLogger(__name__).warning(f"PostgreSQL load stderr: {result.stderr}")
    except Exception as e:
        raise FatalError(f"PostgreSQL load error ({type(e).__name__}): {str(e)}")
    finally:
        if "cur" in locals():
            cur.close()
        if "conn" in locals():
            conn.close()


def check_db_exists(db_name):
    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user=db_config.PG_USER,
            password=db_config.PG_PASSWORD,
            host=db_config.PG_HOST,
            port=db_config.PG_PORT,
        )
        conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
        cur = conn.cursor()
        cur.execute("SELECT 1 FROM pg_database WHERE datname=%s;", (db_name,))
        exists = cur.fetchone() is not None
        return exists
    except Exception as e:
        raise FatalError(f"PostgreSQL existence check error ({type(e).__name__}): {str(e)}")
    finally:
        if "cur" in locals():
            cur.close()
        if "conn" in locals():
            conn.close()
    

def clean_up(db_name):
    logging.getLogger(__name__).debug(f"Cleaning up PostgreSQL database '{db_name}'")
    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user=db_config.PG_USER,
            password=db_config.PG_PASSWORD,
            host=db_config.PG_HOST,
            port=db_config.PG_PORT,
        )
        conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
        cur = conn.cursor()
        cur.execute("SELECT 1 FROM pg_database WHERE datname=%s;", (db_name,))
        exists = cur.fetchone() is not None
        if exists:
            # Terminate all active connections to the target DB
            cur.execute("""SELECT pg_terminate_backend(pid) FROM pg_stat_activity WHERE datname=%s AND pid <> pg_backend_pid();""", (db_name,))

            # Drop the database
            cur.execute(f"DROP DATABASE {pg_ident(db_name)};")
    except Exception as e:
        raise FatalError(f"PostgreSQL cleanup error ({type(e).__name__}): {str(e)}")
    finally:
        if "cur" in locals():
            cur.close()
        if "conn" in locals():
            conn.close()



class PostgresQueryDBTool:
    @staticmethod
    def check_args(db_client, query):
        if 'db_name' not in db_client:
            raise FatalError(f"Missing `db_name` for postgres db_client: {db_client}")
        
        return {
            "db_name": db_client["db_name"],
            "sql": query
        }

    @staticmethod
    def exec(db_name, sql):
        uri = (
            f"postgresql+psycopg2://{db_config.PG_USER}:{db_config.PG_PASSWORD}"
            f"@{db_config.PG_HOST}:{db_config.PG_PORT}/{db_name}"
            "?options=-c default_transaction_read_only=on"
        )

        with sqlalchemy.create_engine(uri).connect() as conn:
            try:
                result_df = pd.read_sql(sqlalchemy.text(sql), conn)
            except Exception as e:
                raise ValueError(f"Postgres query exectution error ({type(e).__name__}): {str(e)}")
        return db_config.serialize(result_df)
            
class PostgresListDBTool:
    @staticmethod
    def check_args(db_client):
        if 'db_name' not in db_client:
            raise FatalError(f"Missing `db_name` for postgres db_client: {db_client}")
        
        return {
            "db_name": db_client["db_name"],
            "query":"SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';"
        }
    
    @staticmethod
    def exec(db_name, query):
        uri = (
            f"postgresql+psycopg2://{db_config.PG_USER}:{db_config.PG_PASSWORD}"
            f"@{db_config.PG_HOST}:{db_config.PG_PORT}/{db_name}"
            "?options=-c default_transaction_read_only=on"
        )

        with sqlalchemy.create_engine(uri).connect() as conn:
            try:
                result_df = pd.read_sql(sqlalchemy.text(query), conn)
                return result_df.iloc[:, 0].tolist()
            except Exception as e:
                raise FatalError(f"Postgres list tables execution error ({type(e).__name__}): {str(e)}")

