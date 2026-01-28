code = """import json, pandas as pd

biz = pd.DataFrame(var_call_fhgMPcu5RYXUwwT6cAwMseYg)
# map businessid_N -> businessref_N
biz['business_ref'] = biz['business_id'].str.replace('businessid_', 'businessref_', regex=False)
refs = biz['business_ref'].dropna().unique().tolist()
print('__RESULT__:')
print(json.dumps(refs))"""

env_args = {'var_call_yv4lmmnzL2S2tduqMOD5OljP': [{'avg_rating': 'nan'}], 'var_call_fhgMPcu5RYXUwwT6cAwMseYg': [{'business_id': 'businessid_52'}, {'business_id': 'businessid_84'}, {'business_id': 'businessid_76'}, {'business_id': 'businessid_87'}, {'business_id': 'businessid_65'}, {'business_id': 'businessid_94'}, {'business_id': 'businessid_90'}, {'business_id': 'businessid_16'}]}

exec(code, env_args)
