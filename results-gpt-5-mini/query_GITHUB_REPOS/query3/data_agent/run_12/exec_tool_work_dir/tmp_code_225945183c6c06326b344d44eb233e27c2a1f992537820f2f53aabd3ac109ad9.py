code = """import json

# Load list of repo_names from metadata query result stored in var_call_qyWRjskagdcuESIlgtQaMWJr
with open(var_call_qyWRjskagdcuESIlgtQaMWJr, 'r', encoding='utf-8') as f:
    repo_list = json.load(f)

# repo_list is a list of repo_name strings
repo_set = {r.lower() for r in repo_list}

# Load commits from artifacts query result stored in var_call_3tfiIRskEhHRrjWW9T8zfLPt
with open(var_call_3tfiIRskEhHRrjWW9T8zfLPt, 'r', encoding='utf-8') as f:
    commits = json.load(f)

count = 0
for c in commits:
    try:
        rname = c.get('repo_name', '')
        if not rname:
            continue
        if rname.lower() not in repo_set:
            continue
        msg = c.get('message')
        if not isinstance(msg, str):
            continue
        # message exists and shorter than 1000 characters
        if len(msg) >= 1000:
            continue
        # does not begin with 'merge', 'update', or 'test' (case-insensitive), ignoring leading whitespace
        if msg.lstrip().lower().startswith(('merge', 'update', 'test')):
            continue
        count += 1
    except Exception:
        continue

import json as _json
print("__RESULT__:")
print(_json.dumps(count))"""

env_args = {'var_call_6M31FDKP9tgPv9rO4QH7QbV3': 'file_storage/call_6M31FDKP9tgPv9rO4QH7QbV3.json', 'var_call_qyWRjskagdcuESIlgtQaMWJr': 'file_storage/call_qyWRjskagdcuESIlgtQaMWJr.json', 'var_call_3tfiIRskEhHRrjWW9T8zfLPt': 'file_storage/call_3tfiIRskEhHRrjWW9T8zfLPt.json'}

exec(code, env_args)
