code = """import json

# Load the large JSON result stored in var_call_dL64AvuqXw3XjenQlJh9dxO3
path = var_call_dL64AvuqXw3XjenQlJh9dxO3
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Filter only .swift paths and non-binary (repo_data_description should not contain 'binary')
import re
records = []
for r in data:
    sp = r.get('sample_path','')
    if sp and sp.lower().endswith('.swift'):
        desc = r.get('repo_data_description','') or ''
        if 'binary' in desc.lower():
            continue
        # find number of times using regex searching for '\b(\d+)\s+times\b'
        m = re.search(r"(\d+)\s+times", desc)
        copies = None
        if m:
            copies = int(m.group(1))
        else:
            # fallback search for any number in description
            m2 = re.search(r"(\d+)", desc)
            if m2:
                copies = int(m2.group(1))
        if copies is None:
            continue
        records.append({
            'id': r.get('id'),
            'copies': copies,
            'sample_repo_name': r.get('sample_repo_name'),
            'sample_path': sp,
            'repo_data_description': desc
        })

if not records:
    result = {'max_records': []}
else:
    # find max copies
    max_c = max(r['copies'] for r in records)
    max_recs = [r for r in records if r['copies'] == max_c]
    result = {'max_copies': max_c, 'max_records': max_recs}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_mvAHZR8tVZZzIpwHmqBQ5V90': ['commits', 'contents', 'files'], 'var_call_yM2Hj3ouLvOpqlSsla4NxN9d': [], 'var_call_OIX3wuCs6rRuGbom6j3f4uBP': [{'id': 'cc41f22d46f21f11c9e716b30cbaeb11f4ef80fc', 'copies': '1', 'path': 'crashes-duplicates/22401-llvm-foldingset-swift-tupletype-nodeequals.swift'}, {'id': '71a17ce92451858f3eb01aa8082551e48bc5550d', 'copies': '1', 'path': 'validation-test/compiler_crashers_fixed/27485-swift-bracestmt-create.swift'}], 'var_call_dL64AvuqXw3XjenQlJh9dxO3': 'file_storage/call_dL64AvuqXw3XjenQlJh9dxO3.json', 'var_call_7Pz0Q5FMux6vesesm0vqGnVP': []}

exec(code, env_args)
