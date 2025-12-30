code = """import json
import re

with open(locals()['var_function-call-5605292304546820245'], 'r') as f:
    docs = json.load(f)
text = docs[0]['text']

# Normalize text
norm_text = " ".join(text.split())

with open(locals()['var_function-call-3657045741871633664'], 'r') as f:
    funding_data = json.load(f)

print("__RESULT__:")
# Debug info
headers = []
for h in ["Capital Improvement Projects", "Disaster Recovery Projects"]:
    idx = norm_text.find(h)
    headers.append({h: idx})

# Check a few names
found_count = 0
examples = []
for item in funding_data[:10]:
    name = item['Project_Name']
    norm_name = " ".join(name.split())
    if norm_name in norm_text:
        found_count += 1
        examples.append(name)

print(json.dumps({"headers": headers, "found_count": found_count, "examples": examples}))"""

env_args = {'var_function-call-5605292304546820245': 'file_storage/function-call-5605292304546820245.json', 'var_function-call-3657045741871633664': 'file_storage/function-call-3657045741871633664.json', 'var_function-call-3095873966328679813': {'projects': [], 'total': 0}}

exec(code, env_args)
