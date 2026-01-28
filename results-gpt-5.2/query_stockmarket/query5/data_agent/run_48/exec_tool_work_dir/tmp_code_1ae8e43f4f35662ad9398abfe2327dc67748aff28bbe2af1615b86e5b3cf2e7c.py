code = """import json, pandas as pd
from pathlib import Path

recs = json.loads(Path(var_call_xUiEcJs4fOvWp0uoX91Eu8bT).read_text())
info = pd.DataFrame(recs)
trade_tables = pd.DataFrame(json.loads(Path(var_call_KNptnrjiW3md2Ma7VRkatyug).read_text())).rename(columns={'name':'Symbol'})

syms = sorted(set(info['Symbol'].astype(str)).intersection(set(trade_tables['Symbol'].astype(str))))

parts = []
for t in syms:
    ident = '"' + t.replace('"','""') + '"'
    sym_lit = t.replace("'","''")
    q = f"SELECT '{sym_lit}' AS Symbol, COUNT(*)::BIGINT AS days FROM {ident} WHERE Date >= '2019-01-01' AND Date < '2020-01-01' AND Low IS NOT NULL AND High IS NOT NULL AND Low > 0 AND (High - Low) / Low > 0.2"
    parts.append(q)

query = "\nUNION ALL\n".join(parts)

print('__RESULT__:')
print(json.dumps({'symbols_with_tables': len(syms), 'query_preview': query[:500]}))"""

env_args = {'var_call_xUiEcJs4fOvWp0uoX91Eu8bT': 'file_storage/call_xUiEcJs4fOvWp0uoX91Eu8bT.json', 'var_call_KNptnrjiW3md2Ma7VRkatyug': 'file_storage/call_KNptnrjiW3md2Ma7VRkatyug.json'}

exec(code, env_args)
