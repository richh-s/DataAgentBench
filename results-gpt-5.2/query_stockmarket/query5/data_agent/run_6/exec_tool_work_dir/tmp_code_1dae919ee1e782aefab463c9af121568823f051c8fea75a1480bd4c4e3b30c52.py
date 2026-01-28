code = """import json, pandas as pd

# load stockinfo (NASDAQ Capital Market)
path_info = var_call_1M2WJBSzBWCBsrqxUcSSQvFy
with open(path_info, 'r') as f:
    info = json.load(f)
info_df = pd.DataFrame(info)

# load available trade tables
path_tbls = var_call_6zdVBkckwn2R8JwOU8xeyNkR
with open(path_tbls, 'r') as f:
    tbls = set(json.load(f))

# keep symbols that exist as tables
info_df = info_df[info_df['Symbol'].isin(tbls)].copy()
syms = info_df['Symbol'].tolist()

# create batches for SQL IN clause
batch_size = 120
batches = [syms[i:i+batch_size] for i in range(0, len(syms), batch_size)]

queries = []
for b in batches:
    union_parts = []
    for s in b:
        # ensure valid identifier for duckdb table; symbols include special chars rarely; skip if not alnum/underscore
        if not s.replace('_','').isalnum():
            continue
        union_parts.append(f"SELECT '{s}' AS Symbol, COUNT(*) AS cnt FROM {s} WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND Low > 0 AND (High - Low) / Low > 0.2")
    if union_parts:
        queries.append(" UNION ALL ".join(union_parts))

print('__RESULT__:')
print(json.dumps({'n_symbols': len(syms), 'n_queries': len(queries), 'queries': queries[:3]}))"""

env_args = {'var_call_1M2WJBSzBWCBsrqxUcSSQvFy': 'file_storage/call_1M2WJBSzBWCBsrqxUcSSQvFy.json', 'var_call_6zdVBkckwn2R8JwOU8xeyNkR': 'file_storage/call_6zdVBkckwn2R8JwOU8xeyNkR.json'}

exec(code, env_args)
