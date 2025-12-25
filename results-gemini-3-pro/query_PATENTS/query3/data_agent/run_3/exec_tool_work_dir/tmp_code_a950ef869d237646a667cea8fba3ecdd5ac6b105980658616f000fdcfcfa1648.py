code = """import json
import re

# Load the UC patents result
with open(locals()['var_function-call-10411442442073960916'], 'r') as f:
    uc_data = json.load(f)

print(f"Loaded {len(uc_data)} UC patent records.")

uc_ids = set()
# Regex to extract publication number
# Patterns seen: "publication number US-11081687-B2.", "pub. number US-2022074631-A1.", "publication no. EP-1224461-B1."
# It seems the number is always at the end, before the trailing dot.
# Let's try to capture "publication number <ID>", "pub. number <ID>", "publication no. <ID>"
regex = re.compile(r'(?:publication number|pub\. number|publication no\.)\s+([A-Za-z0-9\-]+)')

for row in uc_data:
    info = row.get('Patents_info', '')
    match = regex.search(info)
    if match:
        uc_ids.add(match.group(1))

print(f"Extracted {len(uc_ids)} unique UC publication numbers.")
print("__RESULT__:")
print(json.dumps(list(uc_ids)[:10]))"""

env_args = {'var_function-call-15056912119011397630': 'file_storage/function-call-15056912119011397630.json', 'var_function-call-10236890153849732121': [{'COUNT(*)': '277813'}], 'var_function-call-10411442442073960916': 'file_storage/function-call-10411442442073960916.json'}

exec(code, env_args)
