code = """import json, pandas as pd
from pathlib import Path

p = Path(var_call_SJDvuDlh3OpinUytl9I4duYD)
recs = json.loads(p.read_text())
df = pd.DataFrame(recs)
syms = sorted(df['Symbol'].dropna().unique().tolist())

parts = []
for s in syms:
    t = s.replace('"','')
    parts.append(
        "SELECT '" + t + "' AS Symbol, COUNT(*) AS days_cnt "
        + "FROM \"" + t + "\" "
        + "WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' "
        + "  AND Low IS NOT NULL AND Low > 0 "
        + "  AND High IS NOT NULL "
        + "  AND ((High - Low) / Low) > 0.2"
    )

query = "\nUNION ALL\n".join(parts)
out = {'n_symbols': int(len(syms)), 'sql': query[:5000], 'sql_len': len(query)}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_SJDvuDlh3OpinUytl9I4duYD': 'file_storage/call_SJDvuDlh3OpinUytl9I4duYD.json'}

exec(code, env_args)
