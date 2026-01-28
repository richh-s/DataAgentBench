code = """import json, pandas as pd
from pathlib import Path

# load stockinfo symbols and names
recs = json.loads(Path(var_call_xUiEcJs4fOvWp0uoX91Eu8bT).read_text())
info = pd.DataFrame(recs)
info['Symbol'] = info['Symbol'].astype(str)

# load trade tables list
trade_tables = pd.DataFrame(json.loads(Path(var_call_KNptnrjiW3md2Ma7VRkatyug).read_text()))
trade_tables = trade_tables.rename(columns={'name':'Symbol'})
trade_tables['Symbol'] = trade_tables['Symbol'].astype(str)

# only those with trade data tables
syms = sorted(set(info['Symbol']).intersection(set(trade_tables['Symbol'])))

# escape for identifiers
parts = []
for t in syms:
    # double-quote escaping for identifier
    ident = '"' + t.replace('"','""') + '"'
    parts.append(
        "SELECT '" + t.replace("'","''") + "' AS Symbol, COUNT(*)::BIGINT AS days "
        "FROM " + ident + " "
        "WHERE Date >= '2019-01-01' AND Date < '2020-01-01' "
        "AND Low IS NOT NULL AND High IS NOT NULL AND Low > 0 "
        "AND (High - Low) / Low > 0.2"
    )

query = "\nUNION ALL\n".join(parts)

print('__RESULT__:')
print(json.dumps({'symbols_with_tables': len(syms), 'query_length': len(query)}))"""

env_args = {'var_call_xUiEcJs4fOvWp0uoX91Eu8bT': 'file_storage/call_xUiEcJs4fOvWp0uoX91Eu8bT.json', 'var_call_KNptnrjiW3md2Ma7VRkatyug': 'file_storage/call_KNptnrjiW3md2Ma7VRkatyug.json'}

exec(code, env_args)
