code = """import json, re
# Load the large query result from the artifacts_database non-binary Swift file list
path = var_call_S0QNqxSOuc6ytXYBRJcc7H9R
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)

# Parse the duplication count from repo_data_description
def extract_count(desc):
    if not desc:
        return 0
    # look for patterns like 'repeated 25 times', 'duplicated 15 times', 'copied 35 times', 'appearing 12 times', 'seen 2 times'
    m = re.search(r'(?:repeated|duplicated|copied|appearing|appears|appearing|seen)\s+(\d+)\s+times', desc, re.IGNORECASE)
    if m:
        return int(m.group(1))
    m = re.search(r'(\d+)\s+times', desc, re.IGNORECASE)
    if m:
        return int(m.group(1))
    m = re.search(r'\b(\d+)\b', desc)
    if m:
        return int(m.group(1))
    return 0

for r in records:
    r['dup_count'] = extract_count(r.get('repo_data_description',''))

# Find max dup_count
max_count = max((r['dup_count'] for r in records), default=0)

# Get all ids with max_count
top = [ { 'id': r['id'], 'dup_count': r['dup_count'], 'any_repo': r.get('any_repo'), 'any_path': r.get('any_path'), 'repo_data_description': r.get('repo_data_description') } for r in records if r['dup_count']==max_count ]

output = { 'max_dup_count': max_count, 'top_ids': top }

import json
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_CV5p1OkwezpufdaYqYVJnwSp': [], 'var_call_tTqPndh0iuNPkL9Zm1VYsnGe': ['commits', 'contents', 'files'], 'var_call_8MSSqL22hS01DwprQB88cE0F': 'file_storage/call_8MSSqL22hS01DwprQB88cE0F.json', 'var_call_sBuZcJ491fJ70oaLBMWPYa37': [], 'var_call_qIrOAnMr22ezeXubE2KXD1BZ': [], 'var_call_S0QNqxSOuc6ytXYBRJcc7H9R': 'file_storage/call_S0QNqxSOuc6ytXYBRJcc7H9R.json'}

exec(code, env_args)
