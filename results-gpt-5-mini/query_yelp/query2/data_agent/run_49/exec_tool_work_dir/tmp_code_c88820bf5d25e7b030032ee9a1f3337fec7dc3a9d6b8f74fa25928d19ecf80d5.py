code = """import json
import re

# load variables
from pathlib import Path

def load_var(v):
    if isinstance(v, str):
        with open(v, 'r') as f:
            return json.load(f)
    return v

business_records = load_var(var_call_2zESRXQokhF5Lf5iMBJbnpbn)
review_records = load_var(var_call_iTkaQoBL33XRjP3WrF6keht3)

states = set(['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY'])

bizref_to_state = {}
no_state = []
for b in business_records:
    bid = b.get('business_id')
    desc = b.get('description') or ''
    if bid.startswith('businessid_'):
        bref = 'businessref_' + bid.split('businessid_')[-1]
    else:
        bref = bid
    found = None
    # find two-letter uppercase tokens
    tokens = re.findall(r"\b([A-Z]{2})\b", desc)
    for t in tokens:
        if t in states:
            found = t
            break
    if found:
        bizref_to_state[bref] = found
    else:
        no_state.append({'business_id': bid, 'description': desc[:120]})

# collect some review refs
review_refs = [r.get('business_ref') for r in review_records[:200]]

out = {
    'total_business_records': len(business_records),
    'mapped_businesses': len(bizref_to_state),
    'sample_mapped_items': list(list(bizref_to_state.items())[:10]),
    'sample_no_state': no_state[:10],
    'sample_review_refs': review_refs[:20]
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_5WRzRpXAfI3DswmAJC6LyAJg': ['business', 'checkin'], 'var_call_TswX3NFH0hPFBvda8Rluvpwq': ['review', 'tip', 'user'], 'var_call_2YqDNDO27mXYKnAbO6OxgAPy': 'file_storage/call_2YqDNDO27mXYKnAbO6OxgAPy.json', 'var_call_2zESRXQokhF5Lf5iMBJbnpbn': 'file_storage/call_2zESRXQokhF5Lf5iMBJbnpbn.json', 'var_call_iTkaQoBL33XRjP3WrF6keht3': 'file_storage/call_iTkaQoBL33XRjP3WrF6keht3.json', 'var_call_vQpg8ij8b9x9OXwsuP3Q28Oq': {'state': None, 'total_reviews': 0, 'average_rating': None}}

exec(code, env_args)
