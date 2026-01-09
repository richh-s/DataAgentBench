code = """import json

src = var_call_WHVSnajTliQHiGgfimhz4muQ
if isinstance(src, str):
    with open(src,'r') as f:
        payload = json.load(f)
else:
    payload = src
symbols = payload['symbols_avail']

parts = []
for s in symbols:
    # quote table name for duckdb
    t = '"' + s.replace('"','""') + '"'
    parts.append(
        f"SELECT '{s}' AS symbol, COUNT(*) AS days FROM {t} WHERE Date >= '2019-01-01' AND Date < '2020-01-01' AND Low IS NOT NULL AND Low <> 0 AND (High - Low) / Low > 0.2"
    )

query = "\nUNION ALL\n".join(parts) + "\nORDER BY days DESC, symbol ASC\nLIMIT 5;"

print('__RESULT__:')
print(json.dumps({'query': query}))"""

env_args = {'var_call_5NexJwt9r8tmm7M3boorcoK4': 'file_storage/call_5NexJwt9r8tmm7M3boorcoK4.json', 'var_call_xlmV46fzXoRjDCNE5tWJWBSV': 'file_storage/call_xlmV46fzXoRjDCNE5tWJWBSV.json', 'var_call_p9dolxokJW8AiTJj0fYLpxbg': 'file_storage/call_p9dolxokJW8AiTJj0fYLpxbg.json', 'var_call_WHVSnajTliQHiGgfimhz4muQ': 'file_storage/call_WHVSnajTliQHiGgfimhz4muQ.json'}

exec(code, env_args)
