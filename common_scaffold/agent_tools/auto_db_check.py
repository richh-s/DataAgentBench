from common_scaffold.db_utils.loader import ensure_db
import logging
logger = logging.getLogger(__name__)

def ensure_mysql_data(db_name, sql_file):
    logger.debug(f"\n=== 🔗 MySQL: Ensuring database `{db_name}` is initialized ===")
    ensure_db(db_type="mysql", db_name=db_name, sql_file=sql_file)
    logger.debug(f"✅ MySQL `{db_name}` ready.")

def ensure_mongo_data(db_name, dump_folder):
    logger.debug(f"\n=== 🔗 MongoDB: Ensuring database `{db_name}` is initialized ===")
    ensure_db(db_type="mongo", db_name=db_name, dump_folder=dump_folder)
    logger.debug(f"✅ MongoDB `{db_name}` ready.")

def ensure_postgres_data(db_name, sql_file):
    logger.debug(f"\n=== 🔗 PostgreSQL: Ensuring database `{db_name}` is initialized ===")
    ensure_db(db_type="postgres", db_name=db_name, sql_file=sql_file)
    logger.debug(f"✅ PostgreSQL `{db_name}` ready.")

def auto_ensure_databases(db_clients: dict):
    logger.debug("\n=== 🚀 Starting database checks ===")
    for name, cfg in db_clients.items():
        db_type = cfg.get("db_type")
        logger.debug(f"\n🔍 Checking `{name}` ({db_type}) …")

        if db_type == "mysql":
            ensure_mysql_data(
                db_name=cfg["db_name"],
                sql_file=cfg["sql_file"]
            )
        elif db_type == "postgres":
            ensure_postgres_data(
                db_name=cfg["db_name"],
                sql_file=cfg["sql_file"]
            )
        elif db_type == "mongo":
            ensure_mongo_data(
                db_name=cfg["db_name"],
                dump_folder=cfg["dump_folder"]
            )
        else:
            logger.debug(f"✅ `{name}` ({db_type}) does not require initialization.")
    logger.debug("\n🎉 All databases are ready!")
