code = """import json

# Read the full list of tables from the file
list_file_path = locals()['var_functions.list_db:2']
with open(list_file_path, 'r') as f:
    tables = json.load(f)

# Check if REAL table exists
real_table_exists = "REAL" in tables

print("__RESULT__:")
print(json.dumps({
    "real_table_exists": real_table_exists,
    "total_tables": len(tables)
}))"""

env_args = {'var_functions.query_db:0': [{'Symbol': 'REAL', 'Company Description': 'The RealReal, Inc. is a leader in the luxury consignment market, offering a platform for buying and selling authenticated pre-owned designer fashion, jewelry, and art.'}], 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json'}

exec(code, env_args)
