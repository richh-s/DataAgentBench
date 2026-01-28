code = """import json, pandas as pd

# load stockinfo results
p_info = var_call_vtBADGPBhuCPaqDbRa2Ulwlx
with open(p_info, 'r') as f:
    info = json.load(f)
info_df = pd.DataFrame(info)

# load trade table list
p_tbls = var_call_YlueU3v832DyoXFN3JazX9wk
with open(p_tbls, 'r') as f:
    tbls = json.load(f)
tbls_set = set(tbls)

# restrict to tickers that exist in trade db
info_df = info_df[info_df['Symbol'].isin(tbls_set)].copy()
syms = info_df['Symbol'].tolist()

# build a single UNION ALL query over all relevant tables for 2019
parts = []
for s in syms:
    # quote table name for duckdb
    parts.append(
        f"SELECT '{s}' AS Symbol, COUNT(*) AS cnt FROM \"{s}\" WHERE Date >= '2019-01-01' AND Date < '2020-01-01' AND Low > 0 AND (High - Low) / Low > 0.2"
    )

# if no symbols, return empty
if not parts:
    out = json.dumps([])
    print('__RESULT__:')
    print(out)
else:
    union_query = "\nUNION ALL\n".join(parts)
    final_query = f"SELECT Symbol, cnt FROM (\n{union_query}\n) t ORDER BY cnt DESC, Symbol ASC LIMIT 5"
    out = json.dumps({'final_query': final_query, 'symbols_count': len(syms)})
    print('__RESULT__:')
    print(out)"""

env_args = {'var_call_vtBADGPBhuCPaqDbRa2Ulwlx': 'file_storage/call_vtBADGPBhuCPaqDbRa2Ulwlx.json', 'var_call_YlueU3v832DyoXFN3JazX9wk': 'file_storage/call_YlueU3v832DyoXFN3JazX9wk.json'}

exec(code, env_args)
