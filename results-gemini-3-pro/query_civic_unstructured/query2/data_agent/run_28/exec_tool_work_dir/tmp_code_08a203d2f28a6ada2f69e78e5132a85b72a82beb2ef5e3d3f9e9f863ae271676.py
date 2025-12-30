code = """import json
import re

with open(locals()['var_function-call-6964896026869671245'], 'r') as f:
    civic_docs = json.load(f)
full_text = chr(10).join([doc['text'] for doc in civic_docs])
full_text_lower = full_text.lower()

# Projects to check
check_list = ["Permanent Skate Park", "Bluffs Park Shade Structure", "Point Dume Walkway Repairs", "Broad Beach Road Water Quality Repair"]

print("__RESULT__:")
results = {}
for name in check_list:
    idx = full_text.find(name)
    if idx != -1:
        context = full_text[idx:idx+500]
        results[name] = context
    else:
        results[name] = "Not Found"

print(json.dumps(results))"""

env_args = {'var_function-call-6964896026869671245': 'file_storage/function-call-6964896026869671245.json', 'var_function-call-16721484954554461294': ['Funding'], 'var_function-call-867828661549977430': 'file_storage/function-call-867828661549977430.json', 'var_function-call-7895803557599904901': {'total_funding': 118000, 'projects': [{'name': 'Bluffs Park Shade Structure', 'amount': 21000}, {'name': 'Permanent Skate Park', 'amount': 97000}]}}

exec(code, env_args)
