code = """import json, pandas as pd

# load full lists if needed
stockinfo = var_call_SeXupNw6DsT1VNeUn1bKELw8
if isinstance(stockinfo, str):
    with open(stockinfo, 'r') as f:
        stockinfo = json.load(f)

tables = var_call_gpTwhozJJCqsFlGd5pxfoNdo
if isinstance(tables, str):
    with open(tables, 'r') as f:
        tables = json.load(f)

info_df = pd.DataFrame(stockinfo)
cap_syms = sorted(set(info_df['Symbol']).intersection(set(tables)))

# build union-all query to compute counts for 2019 where (High-Low)/Low > 0.2
parts = []
for sym in cap_syms:
    # DuckDB: table names may need quoting with double quotes
    parts.append(f"SELECT '{sym}' AS Symbol, COUNT(*) AS days_cnt FROM \"{sym}\" WHERE Date >= '2019-01-01' AND Date < '2020-01-01' AND Low IS NOT NULL AND Low > 0 AND (High - Low) / Low > 0.2")

# chunk to avoid overly large query strings
chunk_size = 200
queries = []
for i in range(0, len(parts), chunk_size):
    q = "\nUNION ALL\n".join(parts[i:i+chunk_size])
    q = f"SELECT Symbol, SUM(days_cnt) AS days_cnt FROM (\n{q}\n) t GROUP BY Symbol"
    queries.append(q)

print('__RESULT__:')
print(json.dumps({'cap_syms_count': len(cap_syms), 'queries_count': len(queries), 'first_query_preview': queries[0][:500]}))"""

env_args = {'var_call_SeXupNw6DsT1VNeUn1bKELw8': 'file_storage/call_SeXupNw6DsT1VNeUn1bKELw8.json', 'var_call_gpTwhozJJCqsFlGd5pxfoNdo': 'file_storage/call_gpTwhozJJCqsFlGd5pxfoNdo.json'}

exec(code, env_args)
