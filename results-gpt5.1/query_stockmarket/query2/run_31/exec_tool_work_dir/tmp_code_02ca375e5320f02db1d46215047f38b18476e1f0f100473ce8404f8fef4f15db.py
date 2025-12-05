code = """import json, pandas as pd
from pathlib import Path

# Load full ETF list from NYSE Arca
path = Path(var_call_v2W9vVsdDISFeENOzQWtNGGm)
etf_df = pd.read_json(path)

symbols = etf_df['Symbol'].tolist()

# Build DuckDB SQL to union all relevant symbol tables with filter
# We only keep those that hit Adj Close > 200 during 2015
conditions = []
for sym in symbols:
    safe = sym.replace('"', '""')
    conditions.append(f"SELECT DISTINCT '{safe}' AS Symbol FROM '{safe}' WHERE strftime('%Y', Date) = '2015' AND ""Adj Close"" > 200")

union_sql = " UNION ALL ".join(conditions)

result_query = {
    'collection': None,
    'filter': None,
    'projection': None,
    'limit': None,
    'raw_sql': union_sql
}

result = json.dumps(result_query)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_v2W9vVsdDISFeENOzQWtNGGm': 'file_storage/call_v2W9vVsdDISFeENOzQWtNGGm.json', 'var_call_VbMy6AN6JEzn4WAz8BgCFxmR': 'file_storage/call_VbMy6AN6JEzn4WAz8BgCFxmR.json'}

exec(code, env_args)
