code = """import json, pandas as pd
from pathlib import Path

# load tickers list from stored json file
path = Path(var_call_zikjTrYIGcj8qCHbWSACVlrs)
recs = json.loads(path.read_text())
df = pd.DataFrame(recs)
tickers = df['Symbol'].dropna().unique().tolist()

# Build union-all query for 2019 counts per ticker.
# condition: (High-Low)/Low > 0.2 and Low>0
parts = []
for t in tickers:
    parts.append(f"SELECT '{t}' AS Symbol, COUNT(*) AS days FROM \"{t}\" WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND Low > 0 AND (High - Low) / Low > 0.2")
query = "\nUNION ALL\n".join(parts)

out = json.dumps({'tickers': tickers, 'union_query': query})
print('__RESULT__:')
print(out)"""

env_args = {'var_call_zikjTrYIGcj8qCHbWSACVlrs': 'file_storage/call_zikjTrYIGcj8qCHbWSACVlrs.json'}

exec(code, env_args)
