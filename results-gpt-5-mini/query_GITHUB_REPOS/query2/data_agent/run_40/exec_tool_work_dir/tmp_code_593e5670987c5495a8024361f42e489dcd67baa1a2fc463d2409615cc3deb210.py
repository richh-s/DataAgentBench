code = """import json
import re
from pathlib import Path

# Load large query results from storage file paths
contents_path = var_call_yWyTvYQK6blqCyWDrRwVk734
languages_path = var_call_uy7nBws4ayPcd0OI32156nyc

with open(contents_path, 'r', encoding='utf-8') as f:
    contents = json.load(f)
with open(languages_path, 'r', encoding='utf-8') as f:
    languages = json.load(f)

# Build languages mapping: repo_name -> language_description
lang_map = {r['repo_name']: r.get('language_description', '') for r in languages}

# Helper to parse language_description and determine primary language
def primary_language(desc):
    # Find all occurrences like 'Swift (1,234 bytes)'
    pairs = re.findall(r"([A-Za-z0-9+#\-]+)[^\d\(]*\(([0-9,]+)\s*bytes\)", desc)
    if not pairs:
        return None
    # Convert bytes to int and pick max
    parsed = [(name, int(b.replace(',', ''))) for name, b in pairs]
    parsed.sort(key=lambda x: x[1], reverse=True)
    return parsed[0][0]

# Process contents: filter .swift, non-binary, extract copy counts
id_info = {}
for rec in contents:
    path = rec.get('sample_path', '') or ''
    if not path.lower().endswith('.swift'):
        continue
    desc = rec.get('repo_data_description', '') or ''
    if 'non-binary' not in desc.lower():
        continue
    # Extract copy count: look for patterns like '123 times'
    m = re.search(r"(\d+)\s+times", desc)
    if not m:
        # try 'copied 12 times' or 'appearing 8 times' already covered; else try 'copied (\d+)'
        m2 = re.search(r"copied\s+(\d+)", desc)
        m = m2
    if not m:
        continue
    copies = int(m.group(1))
    fid = rec.get('id')
    repo = rec.get('sample_repo_name')
    # Track max copies per id and sample paths/repos
    if fid not in id_info:
        id_info[fid] = {'copies': copies, 'repos': set(), 'paths': set()}
    else:
        if copies > id_info[fid]['copies']:
            id_info[fid]['copies'] = copies
    if repo:
        id_info[fid]['repos'].add(repo)
    if path:
        id_info[fid]['paths'].add(path)

# Now filter ids where at least one sample_repo_name is primary Swift
swift_candidates = []
for fid, info in id_info.items():
    for repo in info['repos']:
        desc = lang_map.get(repo, '')
        prim = primary_language(desc)
        if prim and prim.lower() == 'swift':
            # record candidate with one of the Swift repos that contain the file
            swift_candidates.append({
                'id': fid,
                'copies': info['copies'],
                'repo': repo,
                'paths': list(info['paths'])
            })
            break

# If no candidates found, return empty
if not swift_candidates:
    out = {'repo': None, 'file_id': None, 'copies': 0, 'sample_path': None}
else:
    # pick candidate with max copies; if tie pick first
    swift_candidates.sort(key=lambda x: x['copies'], reverse=True)
    top = swift_candidates[0]
    out = {'repo': top['repo'], 'file_id': top['id'], 'copies': top['copies'], 'sample_path': top['paths'][0] if top['paths'] else None}

import json
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_n46FuiUiNEz83A9esOk9qSnt': ['commits', 'contents', 'files'], 'var_call_lkAj5CkwaK8CvQNvHeFIcUH5': ['languages', 'repos', 'licenses'], 'var_call_yWyTvYQK6blqCyWDrRwVk734': 'file_storage/call_yWyTvYQK6blqCyWDrRwVk734.json', 'var_call_uy7nBws4ayPcd0OI32156nyc': 'file_storage/call_uy7nBws4ayPcd0OI32156nyc.json'}

exec(code, env_args)
