code = """import json, pandas as pd
from pathlib import Path

# Load full ETF symbol list from NYSE Arca
file_path = Path(var_call_LKrEEyjuDJjEfn1thLHilNFH)
records = json.loads(file_path.read_text())
etf_symbols = [r['Symbol'] for r in records]

# Load all available trade tables
trade_tables = var_call_LsbypdgzgNt4V6ajPjcHoD6q

# Intersection of ETFs and available price tables
symbols = sorted(set(etf_symbols).intersection(trade_tables))

result = json.dumps(symbols)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_LKrEEyjuDJjEfn1thLHilNFH': 'file_storage/call_LKrEEyjuDJjEfn1thLHilNFH.json', 'var_call_LsbypdgzgNt4V6ajPjcHoD6q': 'file_storage/call_LsbypdgzgNt4V6ajPjcHoD6q.json'}

exec(code, env_args)
