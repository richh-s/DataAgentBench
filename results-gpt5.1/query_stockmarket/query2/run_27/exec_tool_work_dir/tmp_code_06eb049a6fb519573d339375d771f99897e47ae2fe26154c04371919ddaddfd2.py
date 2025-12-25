code = """import json, pandas as pd
from pathlib import Path

# Load ETF symbols from NYSE Arca
file_path = Path(var_call_S6GPOXmDDHbT0rCjcRFM89Ae)
etf_symbols = pd.read_json(file_path)["Symbol"].tolist()

# Intersect with available trade tables
trade_tables = pd.read_json(Path(var_call_qaAXfkVzZq6eVuumz3goWJKf))[0].tolist()
valid_symbols = sorted(set(etf_symbols).intersection(trade_tables))

result = json.dumps({"valid_symbols": valid_symbols})
print("__RESULT__:")
print(result)"""

env_args = {'var_call_S6GPOXmDDHbT0rCjcRFM89Ae': 'file_storage/call_S6GPOXmDDHbT0rCjcRFM89Ae.json', 'var_call_qaAXfkVzZq6eVuumz3goWJKf': 'file_storage/call_qaAXfkVzZq6eVuumz3goWJKf.json'}

exec(code, env_args)
