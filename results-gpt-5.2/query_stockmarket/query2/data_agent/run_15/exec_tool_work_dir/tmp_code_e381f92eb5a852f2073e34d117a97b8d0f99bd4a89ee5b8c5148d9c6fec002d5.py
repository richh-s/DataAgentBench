code = """import json

path = var_call_VGVpI3kO5XpwoFYTl8XTVeJE
with open(path, 'r') as f:
    arca_etfs = json.load(f)
syms = [r['Symbol'] for r in arca_etfs]

path2 = var_call_JIIwmBkuzTk3s1YN9hLJvjTA
with open(path2, 'r') as f:
    available = set(json.load(f))

syms = [s for s in syms if s in available]

parts = []
for s in syms:
    parts.append("SELECT '"+s+"' AS symbol, MAX(\"Adj Close\") AS max_adj_close FROM \""+s+"\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31'")

maxlen = 900000
chunks = []
chunk = []
curlen = 0
for p in parts:
    if curlen + len(p) + 11 > maxlen and chunk:
        chunks.append(chunk)
        chunk = [p]
        curlen = len(p)
    else:
        chunk.append(p)
        curlen += len(p)
if chunk:
    chunks.append(chunk)

queries = [" UNION ALL ".join(c) for c in chunks]

out = {"symbols": syms, "union_queries": queries, "n_symbols": len(syms), "n_chunks": len(queries)}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_VGVpI3kO5XpwoFYTl8XTVeJE': 'file_storage/call_VGVpI3kO5XpwoFYTl8XTVeJE.json', 'var_call_JIIwmBkuzTk3s1YN9hLJvjTA': 'file_storage/call_JIIwmBkuzTk3s1YN9hLJvjTA.json'}

exec(code, env_args)
