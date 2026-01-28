code = """import json

# Read the list of tables from the file
with open(var_functions.list_db:5, 'r') as f:
    tables = json.load(f)

# Check if REAL table exists
real_table_exists = "REAL" in tables
print("__RESULT__:")
print(json.dumps(real_table_exists))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': [{'Nasdaq Traded': 'Y', 'Symbol': 'REAL', 'Listing Exchange': 'Q', 'Market Category': 'Q', 'ETF': 'N', 'Round Lot Size': '100.0', 'Test Issue': 'N', 'Financial Status': 'N', 'NextShares': 'N', 'Company Description': 'The RealReal, Inc. is a leader in the luxury consignment market, offering a platform for buying and selling authenticated pre-owned designer fashion, jewelry, and art.'}], 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json'}

exec(code, env_args)
