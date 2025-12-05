code = """import json, pandas as pd
from pathlib import Path

symbols_path = Path(var_call_iEBtDxMAHoPXpuNpwJSTxltV)
with symbols_path.open() as f:
    all_symbols = json.load(f)

info_path = Path(var_call_4iJIIQz2GS4RwnpQeZUqnqNE)
with info_path.open() as f:
    info = pd.DataFrame(json.load(f))

nyse_symbols = set(info['Symbol'])
valid_symbols = [s for s in all_symbols if s in nyse_symbols]

chunks = [valid_symbols[i:i+200] for i in range(0, len(valid_symbols), 200)]

queries = []
for chunk in chunks:
    syms = ','.join(chunk)
    q = f"SELECT symbol, SUM(CASE WHEN Close > Open AND strftime('%Y', Date)='2017' THEN 1 ELSE 0 END) AS up_days, SUM(CASE WHEN Close < Open AND strftime('%Y', Date)='2017' THEN 1 ELSE 0 END) AS down_days FROM (" + " UNION ALL ".join([f"SELECT '{s}' AS symbol, Date, Open, Close FROM '{s}'" for s in chunk]) + ") t GROUP BY symbol;"
    queries.append(q)

print("__RESULT__:")
print(json.dumps(queries))"""

env_args = {'var_call_iEBtDxMAHoPXpuNpwJSTxltV': 'file_storage/call_iEBtDxMAHoPXpuNpwJSTxltV.json', 'var_call_4iJIIQz2GS4RwnpQeZUqnqNE': 'file_storage/call_4iJIIQz2GS4RwnpQeZUqnqNE.json'}

exec(code, env_args)
