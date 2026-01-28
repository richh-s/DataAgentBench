code = """import json, pandas as pd
from pathlib import Path

# load symbols list
p = Path(var_call_SJDvuDlh3OpinUytl9I4duYD)
recs = json.loads(p.read_text())
df = pd.DataFrame(recs)
syms = sorted(df['Symbol'].dropna().unique().tolist())

# build SQL that unions per-ticker counts in 2019 where (High-Low)/Low > 0.2
parts = []
for s in syms:
    t = s.replace('"','')
    parts.append(
        f"SELECT '{t}' AS Symbol, COUNT(*) AS days_cnt "
        f"FROM \"{t}\" "
        f"WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' "
        f"  AND Low IS NOT NULL AND Low > 0 "
        f"  AND High IS NOT NULL "
        f"  AND ((High - Low) / Low) > 0.2"
    )

query = "\nUNION ALL\n".join(parts)
# Return query and also symbols count
out = {'n_symbols': len(syms), 'sql': query}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_SJDvuDlh3OpinUytl9I4duYD': 'file_storage/call_SJDvuDlh3OpinUytl9I4duYD.json'}

exec(code, env_args)
