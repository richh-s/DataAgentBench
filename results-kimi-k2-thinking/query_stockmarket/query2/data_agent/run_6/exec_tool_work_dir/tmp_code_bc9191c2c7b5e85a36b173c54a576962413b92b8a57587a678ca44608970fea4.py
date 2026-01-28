code = """import json

# Load the list of tables from stocktrade_database
tables_file = locals()['var_functions.list_db:6']
tables = []

# Read the full list of tables
with open(tables_file, 'r') as f:
    tables = json.load(f)

# Load the NYSE Arca ETF symbols from previous query
arca_etfs_file = locals()['var_functions.query_db:0']
arca_etfs = []
with open(arca_etfs_file, 'r') as f:
    arca_etfs = json.load(f)

# Extract just the symbols from NYSE Arca ETFs
arca_symbols = {item['Symbol'] for item in arca_etfs}

# Find the intersection - ETFs that are both in NYSE Arca and have price data tables
available_etfs = []
for table in tables:
    if table in arca_symbols:
        available_etfs.append(table)

print("__RESULT__:")
print(json.dumps({
    "total_arca_etfs": len(arca_symbols),
    "total_tables_in_db": len(tables),
    "available_etfs_count": len(available_etfs),
    "sample_available_etfs": available_etfs[:20]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': 'file_storage/functions.execute_python:2.json', 'var_functions.execute_python:5': {'count': 1435, 'symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA'], 'total_symbols': 1435}, 'var_functions.list_db:6': 'file_storage/functions.list_db:6.json'}

exec(code, env_args)
