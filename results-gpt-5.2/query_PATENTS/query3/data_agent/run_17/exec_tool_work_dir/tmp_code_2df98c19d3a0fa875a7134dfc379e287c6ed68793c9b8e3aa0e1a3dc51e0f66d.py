code = """import json, re, pandas as pd
from pathlib import Path

# load large result
p = Path(var_call_N4ojgkXEmX1Jc6eA1Rcu8Ai3)
recs = json.loads(p.read_text())

uc_pubs = set()
for r in recs:
    s = r.get('Patents_info') or ''
    m = re.search(r'pub\. number\s+([A-Z]{2}-[0-9A-Z]+-[A-Z0-9]+)', s)
    if m:
        uc_pubs.add(m.group(1))

# fetch all rows where citation contains US- and likely contains some uc pub, but can't search all; pull rows with non-empty citation
# We'll query DB for rows with citation not empty
print('__RESULT__:')
print(json.dumps({'uc_pub_count': len(uc_pubs), 'sample_uc_pubs': sorted(list(uc_pubs))[:20]}))"""

env_args = {'var_call_5AUI9b2HwVlqPgKeuUNmzwnA': ['publicationinfo'], 'var_call_fFL44BPQqFYmpSYenwLj41ss': ['cpc_definition'], 'var_call_aFHQuknr5izMKHWl3Wz6WmNM': [], 'var_call_N4ojgkXEmX1Jc6eA1Rcu8Ai3': 'file_storage/call_N4ojgkXEmX1Jc6eA1Rcu8Ai3.json'}

exec(code, env_args)
