code = """import json, pandas as pd, re

pub_path = var_call_z4PkV7FWRypH9YgYcVlPG11E
cpcdef_path = var_call_cLDtjpsBckPNwOfOX0LAhX3l

with open(pub_path, 'r') as f:
    pub_data = json.load(f)
with open(cpcdef_path, 'r') as f:
    cpcdef_data = json.load(f)

pub_df = pd.DataFrame(pub_data)

# Parse year

def parse_year(s):
    if not isinstance(s, str) or not s.strip():
        return None
    m = re.search(r'(19|20)\d{2}', s)
    if m:
        return int(m.group(0))
    return None

pub_df['year'] = pub_df['publication_date'].apply(parse_year)
pub_df = pub_df.dropna(subset=['year'])
pub_df['year'] = pub_df['year'].astype(int)

# Parse first CPC JSON to inspect keys safely
from itertools import islice

sample_raw = None
for val in pub_df['cpc']:
    if isinstance(val, str) and val.strip():
        sample_raw = val
        break

parsed = json.loads(sample_raw)
first = parsed[0] if isinstance(parsed, list) and parsed else {}
keys_list = list(first.keys())

import json as _json
out = _json.dumps({'sample_entry': first, 'keys': keys_list})
print("__RESULT__:")
print(out)"""

env_args = {'var_call_z4PkV7FWRypH9YgYcVlPG11E': 'file_storage/call_z4PkV7FWRypH9YgYcVlPG11E.json', 'var_call_cLDtjpsBckPNwOfOX0LAhX3l': 'file_storage/call_cLDtjpsBckPNwOfOX0LAhX3l.json'}

exec(code, env_args)
