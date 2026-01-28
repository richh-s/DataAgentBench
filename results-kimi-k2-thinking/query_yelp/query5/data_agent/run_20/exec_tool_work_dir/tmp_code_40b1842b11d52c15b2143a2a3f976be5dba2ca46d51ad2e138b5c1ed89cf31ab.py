code = """import json

# Get the PA business IDs from the previous result
pa_business_ids = locals()['var_functions.execute_python:14']['pa_wifi_business_ids']

# Convert business_id format to business_ref format
# businessid_XX -> businessref_XX
pa_business_refs = [bid.replace('businessid_', 'businessref_') for bid in pa_business_ids]

print('__RESULT__:')
print(json.dumps({
    'pa_business_refs': pa_business_refs
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:12': {'top_state': 'PA', 'top_state_count': 8, 'total_wifi_businesses': 21, 'state_counts': {'PA': 8, 'FL': 5, 'IN': 2, 'MO': 2, 'IL': 1, 'LA': 1, 'NV': 1, 'ID': 1}}, 'var_functions.execute_python:14': {'pa_wifi_business_ids': ['businessid_89', 'businessid_97', 'businessid_67', 'businessid_77', 'businessid_86', 'businessid_40', 'businessid_44', 'businessid_82'], 'count': 8}}

exec(code, env_args)
