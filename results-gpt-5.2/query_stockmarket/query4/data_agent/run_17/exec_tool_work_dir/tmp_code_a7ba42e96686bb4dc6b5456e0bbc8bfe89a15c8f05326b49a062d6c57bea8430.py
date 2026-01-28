code = """import json, pandas as pd

# Load NYSE non-ETF symbols list
src = var_call_gYJbskZiMLDqMqhJmUIqMw5P
if isinstance(src, str):
    with open(src, 'r') as f:
        nyse_rows = json.load(f)
else:
    nyse_rows = src

nyse_df = pd.DataFrame(nyse_rows)
nyse_syms = set(nyse_df['Symbol'].dropna().astype(str))

# Load available trade tables list
src2 = var_call_yC5xzU04KLrHiVtr69INvnjw
if isinstance(src2, str):
    with open(src2, 'r') as f:
        trade_tables = json.load(f)
else:
    trade_tables = src2
trade_syms = set(trade_tables)

# Candidate symbols with trade data
cands = sorted(nyse_syms.intersection(trade_syms))

# Build one UNION ALL query to count up/down days in 2017 for all candidates
parts = []
for s in cands:
    tbl = '"' + s.replace('"','""') + '"'
    parts.append(
        f"SELECT '{s}' AS Symbol, "
        f"SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) AS up_days, "
        f"SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) AS down_days "
        f"FROM {tbl} WHERE Date >= '2017-01-01' AND Date < '2018-01-01'"
    )

query = "\nUNION ALL\n".join(parts)

print('__RESULT__:')
print(json.dumps({'candidate_count': len(cands), 'union_query': query[:5000], 'union_query_truncated': len(query) > 5000}))"""

env_args = {'var_call_gYJbskZiMLDqMqhJmUIqMw5P': 'file_storage/call_gYJbskZiMLDqMqhJmUIqMw5P.json', 'var_call_yC5xzU04KLrHiVtr69INvnjw': 'file_storage/call_yC5xzU04KLrHiVtr69INvnjw.json'}

exec(code, env_args)
