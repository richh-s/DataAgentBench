code = """import json, re

contents_path = var_call_yWyTvYQK6blqCyWDrRwVk734
languages_path = var_call_uy7nBws4ayPcd0OI32156nyc

with open(contents_path, 'r', encoding='utf-8') as f:
    contents = json.load(f)
with open(languages_path, 'r', encoding='utf-8') as f:
    languages = json.load(f)

lang_map = {r['repo_name']: r.get('language_description','') for r in languages}

# gather .swift non-binary and extract copies
id_info = {}
for rec in contents:
    path = rec.get('sample_path','') or ''
    if not path.lower().endswith('.swift'):
        continue
    desc = rec.get('repo_data_description','') or ''
    if 'non-binary' not in desc.lower():
        continue
    # extract copies
    m = re.search(r"(\d+)\s+times", desc)
    if not m:
        m = re.search(r"copied\s+(\d+)", desc)
    if not m:
        m = re.search(r"appearing\s+(\d+)", desc)
    if not m:
        m = re.search(r"repeated\s+(\d+)", desc)
    if not m:
        m = re.search(r"(\d+)\s+times", desc)
    if not m:
        continue
    copies = int(m.group(1))
    fid = rec.get('id')
    repo = rec.get('sample_repo_name')
    if fid not in id_info:
        id_info[fid] = {'copies': copies, 'repos': set(), 'paths': set()}
    else:
        if copies > id_info[fid]['copies']:
            id_info[fid]['copies'] = copies
    if repo:
        id_info[fid]['repos'].add(repo)
    if path:
        id_info[fid]['paths'].add(path)

# function to check if a repo's language_description contains 'Swift'
def repo_is_swift(repo):
    desc = lang_map.get(repo,'')
    return 'swift' in desc.lower()

# find candidates where any of the sample repos is Swift
candidates = []
for fid, info in id_info.items():
    for repo in info['repos']:
        if repo_is_swift(repo):
            candidates.append({'id': fid, 'copies': info['copies'], 'repo': repo, 'paths': list(info['paths'])})
            break

# if no candidates, try alternative: repo name contains 'swift' (heuristic)
if not candidates:
    for fid, info in id_info.items():
        for repo in info['repos']:
            if 'swift' in repo.lower():
                candidates.append({'id': fid, 'copies': info['copies'], 'repo': repo, 'paths': list(info['paths'])})
                break

# pick top by copies
if not candidates:
    out = {'repo': None, 'file_id': None, 'copies': 0, 'sample_path': None}
else:
    candidates.sort(key=lambda x: x['copies'], reverse=True)
    top = candidates[0]
    out = {'repo': top['repo'], 'file_id': top['id'], 'copies': top['copies'], 'sample_path': top['paths'][0] if top['paths'] else None}

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_n46FuiUiNEz83A9esOk9qSnt': ['commits', 'contents', 'files'], 'var_call_lkAj5CkwaK8CvQNvHeFIcUH5': ['languages', 'repos', 'licenses'], 'var_call_yWyTvYQK6blqCyWDrRwVk734': 'file_storage/call_yWyTvYQK6blqCyWDrRwVk734.json', 'var_call_uy7nBws4ayPcd0OI32156nyc': 'file_storage/call_uy7nBws4ayPcd0OI32156nyc.json', 'var_call_Lgo8snc4bcIVoptcX1FZDE5n': {'repo': None, 'file_id': None, 'copies': 0, 'sample_path': None}}

exec(code, env_args)
