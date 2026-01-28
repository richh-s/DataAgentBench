code = """import json, pandas as pd

# load full results
with open(var_call_sPuptWK6vPMIEukyP6PhzyEY, 'r') as f:
    info = json.load(f)
with open(var_call_h1WcvUzmUip7YwjHzrIxBE7I, 'r') as f:
    tables = json.load(f)

info_df = pd.DataFrame(info)
info_df['Symbol'] = info_df['Symbol'].astype(str)

# only symbols that have price tables
tables_set = set(map(str, tables))
info_df = info_df[info_df['Symbol'].isin(tables_set)].copy()

# prepare list
symbols = info_df['Symbol'].tolist()

# chunk symbols for a UNION ALL query
chunks = [symbols[i:i+80] for i in range(0, len(symbols), 80)]
queries = []
for chunk in chunks:
    parts = []
    for sym in chunk:
        # quote table name (duckdb identifiers use double quotes)
        parts.append(
            f"SELECT '{sym}' AS Symbol,\n" \
            "       SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) AS up_days,\n" \
            "       SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) AS down_days\n" \
            f"FROM \"{sym}\"\n" \
            "WHERE Date >= '2017-01-01' AND Date < '2018-01-01'"
        )
    q = "\nUNION ALL\n".join(parts)
    queries.append(q)

result_rows = []
from pathlib import Path

# execute each chunk query
# We'll call query_db sequentially by printing queries list for outer tool use is not allowed, so compute within python is fine only for data. Here we cannot call query_db.
# Therefore, output queries to run next.
print('__RESULT__:')
print(json.dumps({'queries': queries, 'n_symbols': len(symbols)}))"""

env_args = {'var_call_sPuptWK6vPMIEukyP6PhzyEY': 'file_storage/call_sPuptWK6vPMIEukyP6PhzyEY.json', 'var_call_h1WcvUzmUip7YwjHzrIxBE7I': 'file_storage/call_h1WcvUzmUip7YwjHzrIxBE7I.json'}

exec(code, env_args)
