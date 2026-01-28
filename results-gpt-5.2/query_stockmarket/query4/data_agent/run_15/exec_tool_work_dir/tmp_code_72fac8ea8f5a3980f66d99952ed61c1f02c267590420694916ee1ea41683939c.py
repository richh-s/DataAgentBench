code = """import json, pandas as pd
from pathlib import Path

# load nyse non-etf symbols and names
nyse_path = Path(var_call_B341fO4iHaEslwCWjtPTsjZT)
nyse = json.loads(nyse_path.read_text())
nyse_syms = {r['symbol']: r['company_name'] for r in nyse}

# load available trade tables
trade_path = Path(var_call_OSi3UoiWvjZY8X5Bm2v9eKP5)
trade_tables = set(json.loads(trade_path.read_text()))

symbols = sorted(set(nyse_syms.keys()) & trade_tables)

# generate SQL to compute up/down counts for 2017 for all symbols
parts = []
for s in symbols:
    # table names are symbols; quote with double quotes
    parts.append(
        f"SELECT '{s}' AS symbol, "
        f"SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) AS up_days, "
        f"SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) AS down_days "
        f"FROM \"{s}\" WHERE Date >= '2017-01-01' AND Date < '2018-01-01'"
    )
query = "\nUNION ALL\n".join(parts)

print('__RESULT__:')
print(json.dumps({'query': query, 'n_symbols': len(symbols)}))"""

env_args = {'var_call_YGhympfwGa77IINj2W696UPj': ['stockinfo'], 'var_call_B341fO4iHaEslwCWjtPTsjZT': 'file_storage/call_B341fO4iHaEslwCWjtPTsjZT.json', 'var_call_OSi3UoiWvjZY8X5Bm2v9eKP5': 'file_storage/call_OSi3UoiWvjZY8X5Bm2v9eKP5.json'}

exec(code, env_args)
