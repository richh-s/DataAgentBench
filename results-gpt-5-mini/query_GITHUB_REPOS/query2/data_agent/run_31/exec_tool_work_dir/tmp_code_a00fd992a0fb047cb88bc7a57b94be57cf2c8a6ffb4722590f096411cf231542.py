code = """import json, re

# Load the contents query result from the storage file path
path = var_call_1L7UJ6UKvWrAguNX39s9kRNm
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Filter non-binary Swift entries
entries = []
for r in data:
    sp = r.get('sample_path','') or ''
    desc = r.get('repo_data_description','') or ''
    if not sp.lower().endswith('.swift'):
        continue
    if 'binary' in desc.lower():
        continue
    # extract copies via regex looking for '<num> times'
    m = re.search(r"(\d+)\s+times", desc)
    copies = None
    if m:
        copies = int(m.group(1))
    else:
        # fallback: look for 'copied N' or 'appearing N' or 'duplicated N' or 'repeated N' or 'seen N' or 'appears N'
        m2 = re.search(r"(?:copied|appearing|duplicated|repeated|seen|appears)\s+(\d+)", desc)
        if m2:
            copies = int(m2.group(1))
    if copies is None:
        # as last resort, find all integers and pick the smallest one under 1000 (likely copies)
        ints = [int(x) for x in re.findall(r"\d+", desc)]
        candidates = [x for x in ints if x < 1000]
        copies = min(candidates) if candidates else None
    if copies is None:
        continue
    entries.append({
        'id': r.get('id'),
        'sample_repo_name': r.get('sample_repo_name'),
        'sample_path': sp,
        'repo_data_description': desc,
        'copies': copies
    })

if not entries:
    result = {'max_copies': None, 'ids': []}
else:
    max_c = max(e['copies'] for e in entries)
    top = [e for e in entries if e['copies']==max_c]
    result = {'max_copies': max_c, 'ids': top}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_SDGQX18iUH8NYAOm5b9KcnF2': [], 'var_call_6rsNo2WRfbw8L1KylWqURcN9': [], 'var_call_39gQuW49foulPklZA7Mx8iO3': ['commits', 'contents', 'files'], 'var_call_JWQuMgg7VrdTv7VCwrisOm9A': [{'total_files': '1208'}], 'var_call_bT25wINgnqlapJwRt0hiNri1': [{'total_contents_swift': '105'}], 'var_call_1L7UJ6UKvWrAguNX39s9kRNm': 'file_storage/call_1L7UJ6UKvWrAguNX39s9kRNm.json'}

exec(code, env_args)
