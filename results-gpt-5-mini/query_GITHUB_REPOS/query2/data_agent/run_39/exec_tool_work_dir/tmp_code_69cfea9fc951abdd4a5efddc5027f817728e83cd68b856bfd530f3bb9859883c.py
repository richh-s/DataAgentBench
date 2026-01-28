code = """import json
import re

# Load the large query result from the artifacts query stored as a JSON file
path = var_call_IeZ7TUYdZwyyYsaee5e2mEoz
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Parse and extract copy counts from repo_data_description
rows = []
for r in data:
    desc = (r.get('repo_data_description') or '')
    desc_l = desc.lower()
    if 'non-binary' not in desc_l and 'nonbinary' not in desc_l:
        # skip binary or unknown
        continue
    m = re.search(r"(\d+)\s*(?:times|time)", desc_l)
    copies = None
    if m:
        copies = int(m.group(1))
    else:
        # fallback: look for 'copied N' or 'appearing N' or 'repeated N' or 'seen N'
        m = re.search(r"(?:copied|appearing|appears|repeated|seen)\s*(?:\w+\s*)?(\d+)", desc_l)
        if m:
            copies = int(m.group(1))
    if copies is None:
        # fallback to 1
        copies = 1
    rows.append({'id': r.get('id'), 'sample_repo_name': r.get('sample_repo_name'), 'sample_path': r.get('sample_path'), 'copies': copies})

# Find the maximum copies
if not rows:
    result = {'max_copies': 0, 'rows': []}
else:
    max_copies = max(r['copies'] for r in rows)
    max_rows = [r for r in rows if r['copies'] == max_copies]
    result = {'max_copies': max_copies, 'rows': max_rows}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_2cC1gVjU6DhoUTcrLkfSL8Mo': ['commits', 'contents', 'files'], 'var_call_IeZ7TUYdZwyyYsaee5e2mEoz': 'file_storage/call_IeZ7TUYdZwyyYsaee5e2mEoz.json'}

exec(code, env_args)
