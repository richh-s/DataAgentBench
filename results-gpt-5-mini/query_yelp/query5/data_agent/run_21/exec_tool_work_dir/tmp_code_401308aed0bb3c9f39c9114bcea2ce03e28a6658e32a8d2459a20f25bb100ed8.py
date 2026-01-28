code = """import json
# Read wifi businesses from previous exec
wifi = var_call_ziEaYqeT6TC1A7rcoT0DSCoC
# List of US state codes including DC
us_states = {"AL","AK","AZ","AR","CA","CO","CT","DE","FL","GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC","ND","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VT","VA","WA","WV","WI","WY","DC"}

# Count by state
counts = {}
state_to_refs = {}
for b in wifi:
    st = b.get('state')
    if st not in us_states:
        continue
    counts[st] = counts.get(st, 0) + 1
    state_to_refs.setdefault(st, []).append(b['business_ref'])

if not counts:
    top_state = None
    top_count = 0
    refs = []
else:
    # pick state with max count; tie-breaker: alphabetical
    top_state = sorted(counts.items(), key=lambda x: (-x[1], x[0]))[0][0]
    top_count = counts[top_state]
    refs = state_to_refs[top_state]

out = {'top_state': top_state, 'count': top_count, 'business_refs': refs}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_ogAXyUAbzhdfA7wxn0QSesde': ['business', 'checkin'], 'var_call_GKBL2knORpUCjBgP3uUpLRSi': ['review', 'tip', 'user'], 'var_call_jMnTfOXhNhOpuKrxHpCUinQp': 'file_storage/call_jMnTfOXhNhOpuKrxHpCUinQp.json', 'var_call_ziEaYqeT6TC1A7rcoT0DSCoC': [{'business_id': 'businessid_64', 'business_ref': 'businessref_64', 'state': 'MO', 'wifi_raw': "u'free'"}, {'business_id': 'businessid_54', 'business_ref': 'businessref_54', 'state': 'FL', 'wifi_raw': "u'free'"}, {'business_id': 'businessid_91', 'business_ref': 'businessref_91', 'state': 'LA', 'wifi_raw': "u'free'"}, {'business_id': 'businessid_93', 'business_ref': 'businessref_93', 'state': 'IL', 'wifi_raw': "u'free'"}, {'business_id': 'businessid_26', 'business_ref': 'businessref_26', 'state': 'FL', 'wifi_raw': "u'free'"}, {'business_id': 'businessid_89', 'business_ref': 'businessref_89', 'state': 'PA', 'wifi_raw': "u'free'"}, {'business_id': 'businessid_97', 'business_ref': 'businessref_97', 'state': 'PA', 'wifi_raw': "u'free'"}, {'business_id': 'businessid_67', 'business_ref': 'businessref_67', 'state': 'PA', 'wifi_raw': "u'free'"}, {'business_id': 'businessid_51', 'business_ref': 'businessref_51', 'state': 'FL', 'wifi_raw': "u'free'"}, {'business_id': 'businessid_6', 'business_ref': 'businessref_6', 'state': 'NV', 'wifi_raw': "'free'"}, {'business_id': 'businessid_55', 'business_ref': 'businessref_55', 'state': 'FL', 'wifi_raw': "u'free'"}, {'business_id': 'businessid_77', 'business_ref': 'businessref_77', 'state': 'PA', 'wifi_raw': "u'free'"}, {'business_id': 'businessid_86', 'business_ref': 'businessref_86', 'state': 'PA', 'wifi_raw': "u'free'"}, {'business_id': 'businessid_40', 'business_ref': 'businessref_40', 'state': 'PA', 'wifi_raw': "u'free'"}, {'business_id': 'businessid_44', 'business_ref': 'businessref_44', 'state': 'PA', 'wifi_raw': "u'free'"}, {'business_id': 'businessid_43', 'business_ref': 'businessref_43', 'state': 'IN', 'wifi_raw': "'free'"}, {'business_id': 'businessid_20', 'business_ref': 'businessref_20', 'state': 'FL', 'wifi_raw': "'free'"}, {'business_id': 'businessid_25', 'business_ref': 'businessref_25', 'state': 'ID', 'wifi_raw': "u'free'"}, {'business_id': 'businessid_82', 'business_ref': 'businessref_82', 'state': 'PA', 'wifi_raw': "u'free'"}, {'business_id': 'businessid_12', 'business_ref': 'businessref_12', 'state': 'AB', 'wifi_raw': "u'paid'"}, {'business_id': 'businessid_16', 'business_ref': 'businessref_16', 'state': 'IN', 'wifi_raw': "u'free'"}, {'business_id': 'businessid_46', 'business_ref': 'businessref_46', 'state': 'MO', 'wifi_raw': "u'free'"}]}

exec(code, env_args)
