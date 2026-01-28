code = """import json, re

# Load the query result stored in var_call_VhFn2pRNKi2wKekTOzV677qp
path = var_call_VhFn2pRNKi2wKekTOzV677qp
with open(path, 'r') as f:
    data = json.load(f)

# data is a list of dicts
records = data

# function to extract copies count from repo_data_description
def extract_copies(desc):
    if not desc:
        return None
    # search for patterns like '123 times'
    m = re.search(r"(\d+)\s+times", desc)
    if m:
        return int(m.group(1))
    # other patterns
    m = re.search(r"copied\s+(\d+)", desc)
    if m:
        return int(m.group(1))
    m = re.search(r"appearing\s+(\d+)", desc)
    if m:
        return int(m.group(1))
    m = re.search(r"appears\s+(\d+)", desc)
    if m:
        return int(m.group(1))
    m = re.search(r"seen\s+(\d+)", desc)
    if m:
        return int(m.group(1))
    m = re.search(r"duplicated\s+(\d+)", desc)
    if m:
        return int(m.group(1))
    m = re.search(r"repeated\s+(\d+)", desc)
    if m:
        return int(m.group(1))
    # fallback: find all numbers and maybe the last one is copies? But risky.
    nums = re.findall(r"(\d+)", desc)
    if nums:
        # heuristics: if first number > 1000 it's bytes, copies likely later small number
        # choose the smallest number >1
        nums_int = [int(x) for x in nums]
        candidates = [n for n in nums_int if n>1 and n<1000]
        if candidates:
            return min(candidates)
        return nums_int[-1]
    return None

# aggregate by id
from collections import defaultdict
agg = {}
for r in records:
    _id = r.get('id')
    repo = r.get('sample_repo_name')
    pathp = r.get('sample_path')
    desc = r.get('repo_data_description')
    copies = extract_copies(desc)
    if _id not in agg:
        agg[_id] = {'id': _id, 'copies': copies if copies is not None else 1, 'repos': set(), 'paths': set(), 'repo_data_description': desc}
    else:
        # keep max copies
        if copies is not None:
            agg[_id]['copies'] = max(agg[_id]['copies'], copies)
    if repo:
        agg[_id]['repos'].add(repo)
    if pathp:
        agg[_id]['paths'].add(pathp)

# find max copies
max_copies = max([v['copies'] for v in agg.values()])
max_items = [v for v in agg.values() if v['copies']==max_copies]

# prepare output
out = {
    'max_copies': max_copies,
    'items': []
}
for it in max_items:
    out['items'].append({'id': it['id'], 'copies': it['copies'], 'sample_repos': sorted(list(it['repos']))[:50], 'sample_paths': sorted(list(it['paths']))[:50], 'repo_data_description': it.get('repo_data_description')})

import json
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_nVyzN5PxuChhGPK0EAwjI3Uv': [], 'var_call_VhFn2pRNKi2wKekTOzV677qp': 'file_storage/call_VhFn2pRNKi2wKekTOzV677qp.json'}

exec(code, env_args)
