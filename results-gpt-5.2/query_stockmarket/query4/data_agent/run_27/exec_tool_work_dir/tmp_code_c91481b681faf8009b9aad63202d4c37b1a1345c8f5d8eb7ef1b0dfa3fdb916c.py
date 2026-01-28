code = """import json, pandas as pd

# load NYSE non-ETF symbols
syms_path = var_call_WVoSx04qn4Zmhus3YGKtwMJW
with open(syms_path, 'r') as f:
    syms = json.load(f)
df_syms = pd.DataFrame(syms)

# load available trade tables
tables_path = var_call_SXxuCg2PazNuuuXO4t5ddkAl
with open(tables_path, 'r') as f:
    tables = json.load(f)
set_tables = set(tables)

# keep only symbols that exist as trade tables
candidates = df_syms[df_syms['Symbol'].isin(set_tables)].copy()

# if any symbols contain characters not valid in duckdb identifiers, we will quote them
symbols = candidates['Symbol'].tolist()

results = []
for sym in symbols:
    # Build query: count up and down days in 2017
    # quote identifier with double quotes; escape any embedded quotes (unlikely)
    qsym = '"' + sym.replace('"', '""') + '"'
    query = f"""SELECT 
        SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) AS up_days,
        SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) AS down_days
      FROM {qsym}
      WHERE Date >= '2017-01-01' AND Date < '2018-01-01';"""
    results.append({'Symbol': sym, 'query': query})

out = pd.DataFrame(results).head(5000).to_dict('records')
print('__RESULT__:')
print(json.dumps({'n_candidates': int(len(symbols)), 'sample_queries': out[:3], 'symbols': symbols}))"""

env_args = {'var_call_WVoSx04qn4Zmhus3YGKtwMJW': 'file_storage/call_WVoSx04qn4Zmhus3YGKtwMJW.json', 'var_call_SXxuCg2PazNuuuXO4t5ddkAl': 'file_storage/call_SXxuCg2PazNuuuXO4t5ddkAl.json'}

exec(code, env_args)
