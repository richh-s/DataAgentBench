code = """import json, re, pandas as pd, os
path = var_call_i8f0ntquBKF44rnfIAj0M0Uo
with open(path) as f: data = json.load(f)

def extract_copies(text):
    m = re.search(r"(duplicated|appearing|copied|repeated) (\d+) times", text)
    return int(m.group(2)) if m else None

for row in data:
    row['copies'] = extract_copies(row['repo_data_description'])

# ensure each id unique already; find max copies
max_copies = max(r['copies'] for r in data if r['copies'] is not None)
max_rows = [r for r in data if r['copies'] == max_copies]
# choose first (any) since question asks file uniquely by id, then repo
result_repo = max_rows[0]['sample_repo_name']
result = {'max_copies': max_copies, 'repo_name': result_repo, 'file_id': max_rows[0]['id']}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_i8f0ntquBKF44rnfIAj0M0Uo': 'file_storage/call_i8f0ntquBKF44rnfIAj0M0Uo.json'}

exec(code, env_args)
