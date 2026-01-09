code = """import json, pandas as pd

path = var_call_3V4pDyazC1sjaV9hP91bTGvn
with open(path,'r',encoding='utf-8') as f:
    info = json.load(f)
syms = sorted({r['Symbol'] for r in info if r.get('Symbol')})

queries = []
for s in syms:
    # DuckDB: table names may need quoting
    q = f"SELECT '{s}' AS Symbol, COUNT(*) AS cnt FROM \"{s}\" WHERE Date >= '2019-01-01' AND Date < '2020-01-01' AND Low > 0 AND (High - Low) / Low > 0.2;"
    queries.append(q)

# chunk to avoid extremely long query
chunk_size = 200
union_chunks = []
for i in range(0, len(queries), chunk_size):
    union_chunks.append(" UNION ALL ".join(queries[i:i+chunk_size]))

final_query = "SELECT Symbol, SUM(cnt) AS days_over_20pct FROM (" + ") UNION ALL (".join(union_chunks) + ") GROUP BY Symbol ORDER BY days_over_20pct DESC, Symbol ASC LIMIT 5;"

print('__RESULT__:')
print(json.dumps({'final_query': final_query, 'n_symbols': len(syms)}))"""

env_args = {'var_call_3V4pDyazC1sjaV9hP91bTGvn': 'file_storage/call_3V4pDyazC1sjaV9hP91bTGvn.json'}

exec(code, env_args)
