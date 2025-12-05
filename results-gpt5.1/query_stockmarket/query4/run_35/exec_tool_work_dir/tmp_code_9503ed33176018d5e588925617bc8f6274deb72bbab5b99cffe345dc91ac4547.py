code = """import json, pandas as pd
from pathlib import Path

symbols = pd.read_json(Path(var_call_CNkDai7HXIca35FpcmrySLw5)).Symbol.tolist()

# Build DuckDB SQL to compute up vs down days in 2017 per symbol
cases = []
for s in symbols:
    cases.append(f"SELECT '{s}' AS symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) AS up_days, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) AS down_days FROM '{s}' WHERE Date >= '2017-01-01' AND Date < '2018-01-01'")
union_sql = " UNION ALL ".join(cases)

result = union_sql

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_eyZAr58rsOSyvS0QCW3pHjjh': 'file_storage/call_eyZAr58rsOSyvS0QCW3pHjjh.json', 'var_call_CNkDai7HXIca35FpcmrySLw5': 'file_storage/call_CNkDai7HXIca35FpcmrySLw5.json'}

exec(code, env_args)
