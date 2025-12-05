code = """import json, pandas as pd
from pathlib import Path

# Load full ETF symbol list from NYSE Arca
file_path = Path(var_call_QPHASP4mzHxCMcSZSeKizc5Y)
with open(file_path, 'r') as f:
    etf_records = json.load(f)

etf_symbols = sorted({r['Symbol'] for r in etf_records})

# We'll generate queries to stocktrade_database to find those whose 2015 Adj Close ever > 200.
# Because we must use tools for DB queries, we just prepare the symbol list here and output it.

result = etf_symbols

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_QPHASP4mzHxCMcSZSeKizc5Y': 'file_storage/call_QPHASP4mzHxCMcSZSeKizc5Y.json', 'var_call_egPOeVjWNmJnv9fc8vw6Wj0L': 'file_storage/call_egPOeVjWNmJnv9fc8vw6Wj0L.json'}

exec(code, env_args)
