code = """import json, pandas as pd
from datetime import datetime

# Load ETF symbols from NYSE Arca
path = var_call_WUi3vmoHmC78nA9fqo38vTMV
with open(path, 'r') as f:
    etf_records = json.load(f)

etf_symbols = [r['Symbol'] for r in etf_records]

# We'll build a DuckDB SQL script that checks each symbol table for 2015 Adj Close > 200
# However, here we only prepare the list; querying will be done outside Python via query_db per instructions.

result = json.dumps(etf_symbols)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_WUi3vmoHmC78nA9fqo38vTMV': 'file_storage/call_WUi3vmoHmC78nA9fqo38vTMV.json', 'var_call_ueGJMCiIOBoJqbiWYhZkMGIU': 'file_storage/call_ueGJMCiIOBoJqbiWYhZkMGIU.json'}

exec(code, env_args)
