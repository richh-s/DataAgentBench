code = """import json, re
import pandas as pd

# Load UC-assigned publications
src = var_call_OEmJzxa5Jx9sLttUfJ6cTZgf
if isinstance(src, str):
    with open(src, 'r', encoding='utf-8') as f:
        uc_rows = json.load(f)
else:
    uc_rows = src

uc_pub_numbers = set()
for r in uc_rows:
    pi = r.get('Patents_info','') or ''
    m = re.search(r'pub\. number\s+([A-Z]{2}-[0-9A-Z]+(?:-[A-Z0-9]+)?)', pi)
    if m:
        uc_pub_numbers.add(m.group(1))

# Find citing publications: those whose citation list includes any UC pub number
citing_rows = []
# SQLite can't easily search JSON text for each; do in python by scanning all records in chunks via SQL.
# Pull needed fields only.

# We'll query SQLite for all rows with non-empty citation to reduce volume.

print('__RESULT__:')
print(json.dumps({'uc_pub_count': len(uc_pub_numbers)}))"""

env_args = {'var_call_oUoC4rgo7IbazBh2tm5OHMVZ': ['publicationinfo'], 'var_call_vLBAdBWrOlxUIGlz8ODC2r8z': ['cpc_definition'], 'var_call_bjUAB8P289iqm7W76637sZG7': [], 'var_call_OEmJzxa5Jx9sLttUfJ6cTZgf': 'file_storage/call_OEmJzxa5Jx9sLttUfJ6cTZgf.json'}

exec(code, env_args)
