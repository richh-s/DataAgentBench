code = """import json, re
import pandas as pd

def load_records(v):
    if isinstance(v, str):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pub = load_records(var_call_r6BfMH8uFQpVcarQ98anmSg7)
cpcdef = load_records(var_call_F202JETNOsuY4uV6uorGzZRJ)

df_pub = pd.DataFrame(pub)
df_cpc = pd.DataFrame(cpcdef)

sym2title = dict(zip(df_cpc['symbol'], df_cpc['titleFull']))

# map UC publications
uc_pubs = set()
for s in df_pub['Patents_info'].dropna().tolist():
    m = re.search(r'pub\. number\s+([A-Z]{2}-[0-9A-Z]+-[A-Z0-9]+)', s)
    if m:
        uc_pubs.add(m.group(1))

# load all publications for citation reverse lookup and assignee/cpc
# only need columns
# Query again not allowed here; using existing df_pub subset is only UC-assigned.
# Need entire table: cannot; so we'll answer based on available data? But query asked citing assignees; requires reverse citations across all patents.

result = {"error": "Insufficient data: only UC-assigned publications were queried; need all publications to find patents that cite UC patents."}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_r6BfMH8uFQpVcarQ98anmSg7': 'file_storage/call_r6BfMH8uFQpVcarQ98anmSg7.json', 'var_call_F202JETNOsuY4uV6uorGzZRJ': 'file_storage/call_F202JETNOsuY4uV6uorGzZRJ.json'}

exec(code, env_args)
