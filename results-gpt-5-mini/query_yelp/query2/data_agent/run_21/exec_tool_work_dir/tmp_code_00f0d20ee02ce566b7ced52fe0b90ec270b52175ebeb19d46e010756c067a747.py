code = """import json
import pandas as pd
import re

with open(var_call_K4j5EdaGbvL0F2JZCDZlMfb4, 'r') as f:
    businesses = json.load(f)

state_pattern = re.compile(r',\s*([A-Z]{2})\b')

def extract_state(desc):
    if not isinstance(desc, str):
        return None
    matches = state_pattern.findall(desc)
    return matches[-1] if matches else None

rows = []
for b in businesses[:50]:
    bid = b.get('business_id')
    desc = b.get('description')
    st = extract_state(desc)
    rows.append({'business_id': bid, 'description': desc, 'state': st})

# count non-null states
non_null = sum(1 for r in rows if r['state'] is not None)

out = {'sample_rows': rows, 'non_null_count_in_sample': non_null}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_G8hOykkC4hAZtPhL6yZt1uZ4': ['checkin', 'business'], 'var_call_G7tiMa5ecVnpHmEVAStpmLgn': ['review', 'tip', 'user'], 'var_call_K4j5EdaGbvL0F2JZCDZlMfb4': 'file_storage/call_K4j5EdaGbvL0F2JZCDZlMfb4.json', 'var_call_MC5PA2iXmKvLohsxZOLzSr5l': 'file_storage/call_MC5PA2iXmKvLohsxZOLzSr5l.json', 'var_call_AFjWY94ENbetQ3HDcnvZ5AGH': {'state': None, 'total_reviews': 0, 'average_rating': None}}

exec(code, env_args)
