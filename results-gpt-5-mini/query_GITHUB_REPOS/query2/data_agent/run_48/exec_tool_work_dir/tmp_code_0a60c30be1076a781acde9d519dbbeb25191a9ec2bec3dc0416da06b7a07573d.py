code = """import json, re
# Load the query result stored in var_call_24hdKOY9owE3p7a7mrHMkGZF (file path)
path = var_call_24hdKOY9owE3p7a7mrHMkGZF
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

results = []
for r in data:
    desc = r.get('repo_data_description','') or ''
    pathp = r.get('sample_path','') or ''
    if not pathp.lower().endswith('.swift'):
        continue
    if 'non-binary' not in desc.lower() and 'non binary' not in desc.lower():
        continue
    copies = None
    # try patterns: number followed by 'times'
    m = re.search(r"(\d+)\s+times", desc, flags=re.IGNORECASE)
    if m:
        copies = int(m.group(1))
    else:
        # try 'copied X times' or 'copied X'
        m = re.search(r"copied\s+(\d+)", desc, flags=re.IGNORECASE)
        if m:
            copies = int(m.group(1))
        else:
            # try 'appearing X times' or 'appearing X'
            m = re.search(r"appearing\s+(\d+)", desc, flags=re.IGNORECASE)
            if m:
                copies = int(m.group(1))
            else:
                # try 'repeated X times' or 'repeated X'
                m = re.search(r"repeated\s+(\d+)", desc, flags=re.IGNORECASE)
                if m:
                    copies = int(m.group(1))
                else:
                    # try 'duplicated X times' or 'duplicated X'
                    m = re.search(r"duplicat\w*\s+(\d+)", desc, flags=re.IGNORECASE)
                    if m:
                        copies = int(m.group(1))
    if copies is None:
        # fallback: find all numbers and try to pick the smaller one (likely copies vs size)
        nums = re.findall(r"(\d+)", desc)
        if nums:
            # choose the min positive below a threshold? copies typically <= 1000; sizes may be larger too
            cand = [int(x) for x in nums]
            # pick the last small number <= 10000
            cand_small = [x for x in cand if x <= 10000]
            if cand_small:
                copies = cand_small[-1]
            else:
                copies = cand[-1]
    results.append({
        'id': r.get('id'),
        'sample_repo_name': r.get('sample_repo_name'),
        'sample_path': r.get('sample_path'),
        'repo_data_description': desc,
        'copies': copies
    })

# find max copies
if not results:
    out = []
else:
    max_c = max(r['copies'] for r in results if r['copies'] is not None)
    top = [r for r in results if r['copies']==max_c]
    out = top

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_HId9LrzF6ITTY0wuF0Y2Pdd0': ['commits', 'contents', 'files'], 'var_call_R3MuW6JjLJ9hhCALrbV9yipt': ['languages', 'repos', 'licenses'], 'var_call_24hdKOY9owE3p7a7mrHMkGZF': 'file_storage/call_24hdKOY9owE3p7a7mrHMkGZF.json'}

exec(code, env_args)
