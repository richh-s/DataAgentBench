code = """import json, pandas as pd
from pathlib import Path

path = Path(var_call_zikjTrYIGcj8qCHbWSACVlrs)
recs = json.loads(path.read_text())
df = pd.DataFrame(recs)
tickers = df['Symbol'].dropna().unique().tolist()

parts = []
for t in tickers:
    parts.append('SELECT ' + "'" + t + "'" + ' AS Symbol, COUNT(*) AS days FROM ' + '"' + t + '"' + " WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND Low > 0 AND (High - Low) / Low > 0.2")
query = "\nUNION ALL\n".join(parts)

out = json.dumps({'tickers_count': len(tickers), 'union_query': query})
print('__RESULT__:')
print(out)"""

env_args = {'var_call_zikjTrYIGcj8qCHbWSACVlrs': 'file_storage/call_zikjTrYIGcj8qCHbWSACVlrs.json'}

exec(code, env_args)
