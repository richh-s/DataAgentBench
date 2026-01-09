code = """import json, pandas as pd
from pathlib import Path

p = Path(var_call_xUiEcJs4fOvWp0uoX91Eu8bT)
recs = json.loads(p.read_text())
df = pd.DataFrame(recs)
syms = sorted(df['Symbol'].dropna().unique().tolist())

parts = []
for s in syms:
    t = s.replace('"','""')
    q = (
        "SELECT '" + t + "' AS Symbol, COUNT(*) AS days FROM \"" + t + "\" "
        "WHERE Date >= '2019-01-01' AND Date < '2020-01-01' "
        "AND Low IS NOT NULL AND High IS NOT NULL AND Low > 0 "
        "AND (High - Low) / Low > 0.2"
    )
    parts.append(q)
query = "\nUNION ALL\n".join(parts)

print('__RESULT__:')
print(json.dumps({'symbols_count': len(syms), 'query': query[:9000], 'query_length': len(query)}))"""

env_args = {'var_call_xUiEcJs4fOvWp0uoX91Eu8bT': 'file_storage/call_xUiEcJs4fOvWp0uoX91Eu8bT.json'}

exec(code, env_args)
