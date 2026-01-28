code = """import json
with open(var_call_zbZVBzAf6L1maBUDhJpN84JT, 'r') as f:
    business_docs = json.load(f)
# collect first 30 business_id and description
sample = []
for d in business_docs[:30]:
    sample.append({"business_id": d.get('business_id'), "description": d.get('description')})
print("__RESULT__:")
print(json.dumps(sample))"""

env_args = {'var_call_zbZVBzAf6L1maBUDhJpN84JT': 'file_storage/call_zbZVBzAf6L1maBUDhJpN84JT.json', 'var_call_HtUP2QtCM4W2py1nVbQumg46': 'file_storage/call_HtUP2QtCM4W2py1nVbQumg46.json', 'var_call_kP6QKdhhBJzhUQVjqQaIP39F': {'state': None, 'review_count': 0, 'average_rating': None}, 'var_call_BDZxjFcyzaArh6TOcHLUE9Np': {'state_counts_sample': {}}}

exec(code, env_args)
