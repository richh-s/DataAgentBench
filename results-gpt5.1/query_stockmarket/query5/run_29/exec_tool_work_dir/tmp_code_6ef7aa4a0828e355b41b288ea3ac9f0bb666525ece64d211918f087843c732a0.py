code = """import json, pandas as pd
from pathlib import Path

symbols_file = var_call_HxfL9asL0ayhMz0cskk4oPHV
with open(symbols_file) as f:
    all_symbols = json.load(f)

info_file = var_call_WqcjZhoCvOus899JUXVR4snj
with open(info_file) as f:
    info = json.load(f)

cap_df = pd.DataFrame(info)
cap_symbols = set(cap_df['Symbol'])
tradable_symbols = [s for s in all_symbols if s in cap_symbols]

chunks = [tradable_symbols[i:i+50] for i in range(0, len(tradable_symbols), 50)]

queries = []
for chunk in chunks:
    syms = ','.join([f'"{s}"' for s in chunk])
    queries.append(f"SELECT symbol, COUNT(*) AS n_days FROM (" + " UNION ALL ".join([f"SELECT '{s}' AS symbol, CAST(Date AS DATE) AS d, High, Low FROM '{s}' WHERE Date LIKE '2019-%'" for s in chunk]) + ") t WHERE (High - Low) / Low > 0.2 GROUP BY symbol")

result = {'symbols': tradable_symbols, 'queries': queries[:5]}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_HxfL9asL0ayhMz0cskk4oPHV': 'file_storage/call_HxfL9asL0ayhMz0cskk4oPHV.json', 'var_call_WqcjZhoCvOus899JUXVR4snj': 'file_storage/call_WqcjZhoCvOus899JUXVR4snj.json'}

exec(code, env_args)
