code = """import json
import re
import pandas as pd

with open(var_call_29NbFVBLxVQw9DZ4jU0BHgZN, 'r') as f:
    business_data = json.load(f)

# show first 30 descriptions and try multiple extraction patterns
patterns = [re.compile(r'in\s+[^,]+,\s*([A-Z]{2})\b'), re.compile(r',\s*([A-Z]{2})\b'), re.compile(r'\b([A-Z]{2})\b')]

results = []
state_counts = {}
for i, b in enumerate(business_data[:1000]):
    desc = b.get('description', '')
    found = None
    for p in patterns:
        m = p.search(desc or '')
        if m:
            found = m.group(1)
            break
    results.append({'business_id': b.get('business_id'), 'description': desc, 'extracted_state': found})
    if found:
        state_counts[found] = state_counts.get(found, 0) + int(b.get('review_count') or 0)

# compute top states
if state_counts:
    sorted_states = sorted(state_counts.items(), key=lambda x: x[1], reverse=True)
else:
    sorted_states = []

out = {'sample_extraction': results[:30], 'state_counts_top10': sorted_states[:10], 'total_states_found': len(state_counts)}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_QVob1VqNPAgiofwEAKHrIiTr': ['checkin', 'business'], 'var_call_Pnw1vvitcoZD7CwhfWOMCoaw': ['review', 'tip', 'user'], 'var_call_29NbFVBLxVQw9DZ4jU0BHgZN': 'file_storage/call_29NbFVBLxVQw9DZ4jU0BHgZN.json', 'var_call_zJ3tUM6dqGmRVBAGwQKmuy8R': 'file_storage/call_zJ3tUM6dqGmRVBAGwQKmuy8R.json', 'var_call_usnmfw7OteypT5lIzS9eCHTL': {'state': None, 'total_reviews': 0, 'average_rating': None}}

exec(code, env_args)
