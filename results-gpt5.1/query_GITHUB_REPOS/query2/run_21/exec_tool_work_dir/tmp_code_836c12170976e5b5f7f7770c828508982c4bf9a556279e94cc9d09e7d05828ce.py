code = """import json, re, pandas as pd

swift_repos = pd.read_json(var_call_RvqgulSCVZgJE60swy0wV417)
contents = pd.read_json(var_call_cm87Hg5VRWUaXjKsRbxcVhRo)

swift_set = set(swift_repos['repo_name'])

def extract_copies(desc):
    m = re.search(r'(?:duplicated|appearing|copied|repeated|seen) (\d+) times', desc)
    return int(m.group(1)) if m else None

contents['copies'] = contents['repo_data_description'].apply(extract_copies)

swift_contents = contents[contents['sample_repo_name'].isin(swift_set)].copy()

idx = swift_contents['copies'].idxmax()
row = swift_contents.loc[idx]

result = {'repo_name': row['sample_repo_name'], 'file_id': row['id'], 'copies': int(row['copies'])}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_RvqgulSCVZgJE60swy0wV417': 'file_storage/call_RvqgulSCVZgJE60swy0wV417.json', 'var_call_cm87Hg5VRWUaXjKsRbxcVhRo': 'file_storage/call_cm87Hg5VRWUaXjKsRbxcVhRo.json'}

exec(code, env_args)
