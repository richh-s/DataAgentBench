code = """import json
import re

# Load the query results from storage file paths
with open(var_call_67PpPFbHhGgcI0IVqDHgSZgP, 'r') as f:
    contents = json.load(f)
with open(var_call_fqmFrk75IXRRjNaDrD68yNGF, 'r') as f:
    languages = json.load(f)

# Helper to extract copy count from repo_data_description
patterns = [r'copied\s*(\d+)', r'appearing\s*(\d+)', r'appears\s*(\d+)', r'duplicated\s*(\d+)', r'repeated\s*(\d+)', r'seen\s*(\d+)', r'(\d+)\s*times', r'appearing\s*(\d+)', r'appears\s*(\d+)']

def extract_count(text):
    if not text:
        return None
    text_lower = text.lower()
    for pat in patterns:
        m = re.search(pat, text_lower)
        if m:
            try:
                return int(m.group(1))
            except:
                continue
    return None

# Build list with counts
rows = []
for r in contents:
    cid = r.get('id')
    repo = r.get('sample_repo_name')
    path = r.get('sample_path')
    desc = r.get('repo_data_description')
    count = extract_count(desc)
    if count is not None:
        rows.append({'id': cid, 'sample_repo_name': repo, 'sample_path': path, 'count': count, 'repo_data_description': desc})

if not rows:
    result = {'error': 'No counts extracted'}
else:
    # Find max count
    max_count = max(r['count'] for r in rows)
    max_rows = [r for r in rows if r['count'] == max_count]
    # For each candidate, check if its sample_repo_name is in languages and is Swift
    lang_map = {entry['repo_name']: entry['language_description'] for entry in languages}
    swift_candidates = []
    for r in max_rows:
        repo = r['sample_repo_name']
        lang_desc = lang_map.get(repo)
        if lang_desc and 'swift' in lang_desc.lower():
            swift_candidates.append(r)
    # If none of the max_rows have sample_repo_name labeled Swift, still return the sample_repo_name of first max_row
    if swift_candidates:
        chosen = swift_candidates[0]
    else:
        chosen = max_rows[0]
    result = {'id': chosen['id'], 'sample_repo_name': chosen['sample_repo_name'], 'sample_path': chosen['sample_path'], 'count': chosen['count'], 'repo_data_description': chosen['repo_data_description']}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_K5lnMQ6VmZ46d5DbXVcKTykV': [], 'var_call_pMPdZu1ABYYE3szLpW6R1ei4': 'file_storage/call_pMPdZu1ABYYE3szLpW6R1ei4.json', 'var_call_fqmFrk75IXRRjNaDrD68yNGF': 'file_storage/call_fqmFrk75IXRRjNaDrD68yNGF.json', 'var_call_67PpPFbHhGgcI0IVqDHgSZgP': 'file_storage/call_67PpPFbHhGgcI0IVqDHgSZgP.json'}

exec(code, env_args)
