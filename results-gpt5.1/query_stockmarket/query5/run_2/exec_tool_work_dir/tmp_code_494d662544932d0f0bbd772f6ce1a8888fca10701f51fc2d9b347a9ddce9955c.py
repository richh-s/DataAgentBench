code = """import json, duckdb

symbols_path = var_call_QAwVfKrVBs5C8l8aNFQoc8GY
with open(symbols_path, 'r') as f:
    symbols = json.load(f)

sym_list = [row['Symbol'] for row in symbols]
con = duckdb.connect(database='stocktrade_database', read_only=True)

placeholders = ','.join(["'" + s.replace("'","''") + "'" for s in sym_list])

query = "WITH tbls AS (SELECT table_name FROM information_schema.tables WHERE table_name IN (" + placeholders + ") ), ranges AS (" \
        " SELECT table_name AS Symbol, Date, Low, High, CASE WHEN Low > 0 THEN (High - Low) / Low ELSE NULL END AS range_pct " \
        " FROM tbls, LATERAL (SELECT Date, Low, High FROM "" || table_name || "" WHERE Date BETWEEN '2019-01-01' AND '2019-12-31') q" \
        "), counts AS (SELECT Symbol, COUNT(*) AS days_exceed FROM ranges WHERE range_pct > 0.2 GROUP BY Symbol) " \
        "SELECT Symbol, days_exceed FROM counts ORDER BY days_exceed DESC LIMIT 5;"

result = con.execute(query).fetchall()

out = [{"Symbol": r[0], "days_exceed": int(r[1])} for r in result]

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_c1MH5kbP7nb1lb58BD37nKsp': 'file_storage/call_c1MH5kbP7nb1lb58BD37nKsp.json', 'var_call_QAwVfKrVBs5C8l8aNFQoc8GY': 'file_storage/call_QAwVfKrVBs5C8l8aNFQoc8GY.json', 'var_call_iLn4YxTygeZxUKltbq3dBg8D': [{"'dummy'": 'dummy'}]}

exec(code, env_args)
