code = """import json, pandas as pd

# load symbols list from storage file
path = var_call_n1ZymEjBBqt5tg5fejoloOuJ
with open(path, 'r') as f:
    recs = json.load(f)

df = pd.DataFrame(recs)
symbols = sorted(df['Symbol'].dropna().unique().tolist())

# build union-all query to count days in 2019 where (High-Low) > 0.2*Low
parts = []
for sym in symbols:
    tbl = sym.replace('"','""')
    parts.append(
        f"SELECT '{sym}' AS Symbol, COUNT(*)::BIGINT AS days_gt20 FROM \"{tbl}\" WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND Low IS NOT NULL AND High IS NOT NULL AND Low > 0 AND (High - Low) > 0.2 * Low"
    )

query = "\nUNION ALL\n".join(parts)

print('__RESULT__:')
print(json.dumps({'query': query, 'n_symbols': len(symbols)}))"""

env_args = {'var_call_n1ZymEjBBqt5tg5fejoloOuJ': 'file_storage/call_n1ZymEjBBqt5tg5fejoloOuJ.json'}

exec(code, env_args)
