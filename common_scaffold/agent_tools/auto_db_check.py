from common_scaffold.db_utils.loader import ensure_db

def ensure_mysql_data(db_name, sql_file):
    print(f"\n=== 🔗 MySQL: Ensuring database `{db_name}` is initialized ===")
    ensure_db(db_type="mysql", db_name=db_name, sql_file=sql_file)
    print(f"✅ MySQL `{db_name}` ready.")

def ensure_mongo_data(db_name, dump_folder):
    print(f"\n=== 🔗 MongoDB: Ensuring database `{db_name}` is initialized ===")
    ensure_db(db_type="mongo", db_name=db_name, dump_folder=dump_folder)
    print(f"✅ MongoDB `{db_name}` ready.")

def auto_ensure_databases(db_clients: dict):
    print("\n=== 🚀 Starting database checks ===")
    for name, cfg in db_clients.items():
        db_type = cfg.get("db_type")
        print(f"\n🔍 Checking `{name}` ({db_type}) …")

        if db_type == "mysql":
            ensure_mysql_data(
                db_name=cfg["db_name"],
                sql_file=cfg["sql_file"]
            )
        elif db_type == "mongo":
            ensure_mongo_data(
                db_name=cfg["db_name"],
                dump_folder=cfg["dump_folder"]
            )
        else:
            print(f"✅ `{name}` ({db_type}) does not require initialization.")
    print("\n🎉 All databases are ready!")
