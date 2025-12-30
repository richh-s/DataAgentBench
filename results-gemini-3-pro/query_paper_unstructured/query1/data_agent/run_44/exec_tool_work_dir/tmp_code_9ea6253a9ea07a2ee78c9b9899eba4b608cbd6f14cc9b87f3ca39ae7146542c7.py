code = """print(default_api.query_db(db_name="paper_docs_database", query={"collection": "paper_docs", "count": True}))
print(default_api.query_db(db_name="citations_database", query="PRAGMA table_info(Citations);"))
print(default_api.query_db(db_name="citations_database", query="SELECT * FROM Citations LIMIT 5;"))"""

env_args = {'var_function-call-4625483642172775665': 'file_storage/function-call-4625483642172775665.json'}

exec(code, env_args)
