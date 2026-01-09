code = """import json, pandas as pd

# Load NYSE non-ETF symbols + names
info_path = var_call_mWeVT9tjW2gngHOT1VIsgXKN
with open(info_path, 'r') as f:
    info = json.load(f)
info_df = pd.DataFrame(info)
info_df['Symbol'] = info_df['Symbol'].astype(str)

# Load trade tables list
tables_path = var_call_qNgFYa91fi9ppy4VdWxc0kGu
with open(tables_path, 'r') as f:
    tables = json.load(f)
tables_set = set(tables)

# Only symbols that have price tables
symbols = sorted(set(info_df['Symbol']).intersection(tables_set))

# chunk to avoid huge SQL
chunks = [symbols[i:i+80] for i in range(0, len(symbols), 80)]
union_queries = []
for ch in chunks:
    parts = []
    for sym in ch:
        # DuckDB identifiers: wrap in double quotes
        parts.append(
            f"SELECT '{sym}' AS Symbol, "
            f"SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) AS up_days, "
            f"SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) AS down_days "
            f"FROM \"{sym}\" WHERE Date >= '2017-01-01' AND Date < '2018-01-01'"
        )
    union_queries.append(" UNION ALL ".join(parts))

final_sql = "SELECT Symbol, SUM(up_days) AS up_days, SUM(down_days) AS down_days FROM (" + (" UNION ALL ".join(union_queries)) + ") t GROUP BY Symbol HAVING SUM(up_days) > SUM(down_days) ORDER BY (SUM(up_days) - SUM(down_days)) DESC, SUM(up_days) DESC, Symbol ASC LIMIT 5;"

print('__RESULT__:')
print(json.dumps({'sql': final_sql, 'n_symbols': len(symbols)}))"""

env_args = {'var_call_mWeVT9tjW2gngHOT1VIsgXKN': 'file_storage/call_mWeVT9tjW2gngHOT1VIsgXKN.json', 'var_call_qNgFYa91fi9ppy4VdWxc0kGu': 'file_storage/call_qNgFYa91fi9ppy4VdWxc0kGu.json'}

exec(code, env_args)
