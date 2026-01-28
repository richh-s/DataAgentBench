code = """import json

# Access previous execute_python result
data = var_call_TaOnEhAoB1Sb6u68swYExP0N

# If it's a string, try to parse
if isinstance(data, str):
    try:
        data = json.loads(data)
    except Exception:
        pass

# data should be a list of dicts
from collections import Counter
counts = Counter()
by_state = {}
for r in data:
    st = r.get('state')
    bref = r.get('business_ref')
    if st and bref:
        counts[st] += 1
        by_state.setdefault(st, []).append(bref)

if not counts:
    result = {'top_state': None, 'business_refs': []}
else:
    top_state, top_count = counts.most_common(1)[0]
    result = {'top_state': top_state, 'business_refs': by_state[top_state], 'count': top_count}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_2WlZ388LhmZXZkp6DMJW9hWz': 'file_storage/call_2WlZ388LhmZXZkp6DMJW9hWz.json', 'var_call_TaOnEhAoB1Sb6u68swYExP0N': [{'business_id': 'businessid_64', 'business_ref': 'businessref_64', 'state': 'MO', 'wifi_value': "u'free'"}, {'business_id': 'businessid_54', 'business_ref': 'businessref_54', 'state': 'FL', 'wifi_value': "u'free'"}, {'business_id': 'businessid_91', 'business_ref': 'businessref_91', 'state': 'LA', 'wifi_value': "u'free'"}, {'business_id': 'businessid_93', 'business_ref': 'businessref_93', 'state': 'IL', 'wifi_value': "u'free'"}, {'business_id': 'businessid_26', 'business_ref': 'businessref_26', 'state': 'FL', 'wifi_value': "u'free'"}, {'business_id': 'businessid_89', 'business_ref': 'businessref_89', 'state': 'PA', 'wifi_value': "u'free'"}, {'business_id': 'businessid_97', 'business_ref': 'businessref_97', 'state': 'PA', 'wifi_value': "u'free'"}, {'business_id': 'businessid_67', 'business_ref': 'businessref_67', 'state': 'PA', 'wifi_value': "u'free'"}, {'business_id': 'businessid_51', 'business_ref': 'businessref_51', 'state': 'FL', 'wifi_value': "u'free'"}, {'business_id': 'businessid_6', 'business_ref': 'businessref_6', 'state': 'NV', 'wifi_value': "'free'"}, {'business_id': 'businessid_55', 'business_ref': 'businessref_55', 'state': 'FL', 'wifi_value': "u'free'"}, {'business_id': 'businessid_77', 'business_ref': 'businessref_77', 'state': 'PA', 'wifi_value': "u'free'"}, {'business_id': 'businessid_86', 'business_ref': 'businessref_86', 'state': 'PA', 'wifi_value': "u'free'"}, {'business_id': 'businessid_40', 'business_ref': 'businessref_40', 'state': 'PA', 'wifi_value': "u'free'"}, {'business_id': 'businessid_44', 'business_ref': 'businessref_44', 'state': 'PA', 'wifi_value': "u'free'"}, {'business_id': 'businessid_43', 'business_ref': 'businessref_43', 'state': 'IN', 'wifi_value': "'free'"}, {'business_id': 'businessid_20', 'business_ref': 'businessref_20', 'state': 'FL', 'wifi_value': "'free'"}, {'business_id': 'businessid_25', 'business_ref': 'businessref_25', 'state': 'ID', 'wifi_value': "u'free'"}, {'business_id': 'businessid_82', 'business_ref': 'businessref_82', 'state': 'PA', 'wifi_value': "u'free'"}, {'business_id': 'businessid_12', 'business_ref': 'businessref_12', 'state': 'AB', 'wifi_value': "u'paid'"}, {'business_id': 'businessid_16', 'business_ref': 'businessref_16', 'state': 'IN', 'wifi_value': "u'free'"}, {'business_id': 'businessid_46', 'business_ref': 'businessref_46', 'state': 'MO', 'wifi_value': "u'free'"}]}

exec(code, env_args)
