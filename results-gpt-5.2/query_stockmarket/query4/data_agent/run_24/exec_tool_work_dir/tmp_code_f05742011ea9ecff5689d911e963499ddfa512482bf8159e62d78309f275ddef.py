code = """import json, pandas as pd

# Load NYSE non-ETF symbols
path_info = var_call_1azq8avYekP4AJfnP0YbucJf
with open(path_info, 'r') as f:
    info = json.load(f)

df_info = pd.DataFrame(info)

# Load available trade tables
path_tbls = var_call_1WDp8YTpSz1oSWbHEA5yX3HS
with open(path_tbls, 'r') as f:
    tbls = set(json.load(f))

# Intersect to those with price data tables
symbols = [s for s in df_info['Symbol'].tolist() if s in tbls]

# For each symbol, compute up and down days in 2017
# Use DuckDB SQL per symbol; store results
from collections import defaultdict

results = []
for sym in symbols:
    q = f"""
    SELECT
      SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) AS up_days,
      SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) AS down_days
    FROM \"{sym}\"
    WHERE Date >= '2017-01-01' AND Date < '2018-01-01'
    """
    results.append({'Symbol': sym, 'query': q.strip()})

# batch in chunks with parallelizable approach not available inside python; we'll just output symbol list and queries for next step
out = json.dumps({'n_symbols': len(symbols), 'symbols_preview': symbols[:20], 'queries': results[:5]})
print('__RESULT__:')
print(out)"""

env_args = {'var_call_1azq8avYekP4AJfnP0YbucJf': 'file_storage/call_1azq8avYekP4AJfnP0YbucJf.json', 'var_call_1WDp8YTpSz1oSWbHEA5yX3HS': 'file_storage/call_1WDp8YTpSz1oSWbHEA5yX3HS.json'}

exec(code, env_args)
