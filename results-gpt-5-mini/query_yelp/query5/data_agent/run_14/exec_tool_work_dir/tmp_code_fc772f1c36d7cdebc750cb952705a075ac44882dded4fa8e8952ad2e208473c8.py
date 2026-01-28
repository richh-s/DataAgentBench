code = """import json
# Use the variable from previous execute_python
data = var_call_GA2ZbbgiIX6go1wcdFD5Qkxf
wifi_businesses = data['wifi_businesses']
# Count per state
counts = {}
by_state = {}
for b in wifi_businesses:
    st = b['state']
    counts[st] = counts.get(st, 0) + 1
    by_state.setdefault(st, []).append(b['business_ref'])
# determine top state (if tie, pick one with lexicographically smallest state)
max_count = max(counts.values())
candidates = [st for st,c in counts.items() if c==max_count]
candidates.sort()
top_state = candidates[0]
result = {'top_state': top_state, 'count': max_count, 'business_refs': by_state[top_state]}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_64XhkT1xjnWS5IJk13AjtdSC': ['checkin', 'business'], 'var_call_2mQZXksl33KcC0GbmzZKG5d3': 'file_storage/call_2mQZXksl33KcC0GbmzZKG5d3.json', 'var_call_GA2ZbbgiIX6go1wcdFD5Qkxf': {'count_wifi_businesses': 22, 'wifi_businesses': [{'business_id': 'businessid_64', 'business_ref': 'businessref_64', 'state': 'MO', 'wifi_raw': "u'free'"}, {'business_id': 'businessid_54', 'business_ref': 'businessref_54', 'state': 'FL', 'wifi_raw': "u'free'"}, {'business_id': 'businessid_91', 'business_ref': 'businessref_91', 'state': 'LA', 'wifi_raw': "u'free'"}, {'business_id': 'businessid_93', 'business_ref': 'businessref_93', 'state': 'IL', 'wifi_raw': "u'free'"}, {'business_id': 'businessid_26', 'business_ref': 'businessref_26', 'state': 'FL', 'wifi_raw': "u'free'"}, {'business_id': 'businessid_89', 'business_ref': 'businessref_89', 'state': 'PA', 'wifi_raw': "u'free'"}, {'business_id': 'businessid_97', 'business_ref': 'businessref_97', 'state': 'PA', 'wifi_raw': "u'free'"}, {'business_id': 'businessid_67', 'business_ref': 'businessref_67', 'state': 'PA', 'wifi_raw': "u'free'"}, {'business_id': 'businessid_51', 'business_ref': 'businessref_51', 'state': 'FL', 'wifi_raw': "u'free'"}, {'business_id': 'businessid_6', 'business_ref': 'businessref_6', 'state': 'NV', 'wifi_raw': "'free'"}, {'business_id': 'businessid_55', 'business_ref': 'businessref_55', 'state': 'FL', 'wifi_raw': "u'free'"}, {'business_id': 'businessid_77', 'business_ref': 'businessref_77', 'state': 'PA', 'wifi_raw': "u'free'"}, {'business_id': 'businessid_86', 'business_ref': 'businessref_86', 'state': 'PA', 'wifi_raw': "u'free'"}, {'business_id': 'businessid_40', 'business_ref': 'businessref_40', 'state': 'PA', 'wifi_raw': "u'free'"}, {'business_id': 'businessid_44', 'business_ref': 'businessref_44', 'state': 'PA', 'wifi_raw': "u'free'"}, {'business_id': 'businessid_43', 'business_ref': 'businessref_43', 'state': 'IN', 'wifi_raw': "'free'"}, {'business_id': 'businessid_20', 'business_ref': 'businessref_20', 'state': 'FL', 'wifi_raw': "'free'"}, {'business_id': 'businessid_25', 'business_ref': 'businessref_25', 'state': 'ID', 'wifi_raw': "u'free'"}, {'business_id': 'businessid_82', 'business_ref': 'businessref_82', 'state': 'PA', 'wifi_raw': "u'free'"}, {'business_id': 'businessid_12', 'business_ref': 'businessref_12', 'state': 'AB', 'wifi_raw': "u'paid'"}, {'business_id': 'businessid_16', 'business_ref': 'businessref_16', 'state': 'IN', 'wifi_raw': "u'free'"}, {'business_id': 'businessid_46', 'business_ref': 'businessref_46', 'state': 'MO', 'wifi_raw': "u'free'"}]}}

exec(code, env_args)
