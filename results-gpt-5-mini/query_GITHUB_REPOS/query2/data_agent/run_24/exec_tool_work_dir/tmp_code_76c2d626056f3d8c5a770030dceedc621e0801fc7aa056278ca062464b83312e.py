code = """import json, re, os
# read the large JSON result file path
path = var_call_OaMFhbHUy84dNAZUPFnLnDty
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

results = []
max_copies = -1
for r in data:
    desc = r.get('repo_data_description') or ''
    copies = None
    # multiple patterns
    m = re.search(r"(\d+)\s+times", desc)
    if not m:
        m = re.search(r"copied\s*(\d+)", desc)
    if not m:
        m = re.search(r"duplicated\s*(\d+)", desc)
    if not m:
        m = re.search(r"appearing\s*(\d+)", desc)
    if not m:
        m = re.search(r"appears\s*(\d+)", desc)
    if not m:
        m = re.search(r"repeated\s*(\d+)", desc)
    if not m:
        m = re.search(r"seen\s*(\d+)", desc)
    if not m:
        m = re.search(r"(\d+)\s+copi", desc)
    if m:
        copies = int(m.group(1))
    else:
        # fallback: count number of occurrences of this id in data
        copies = sum(1 for x in data if x.get('id') == r.get('id'))
    results.append({'id': r.get('id'), 'sample_repo_name': r.get('sample_repo_name'), 'sample_path': r.get('sample_path'), 'repo_data_description': desc, 'copies': copies})
    if copies > max_copies:
        max_copies = copies

# collect top ids
top = [r for r in results if r['copies'] == max_copies]
# collate unique repos for these ids
top_ids = {}
for t in top:
    tid = t['id']
    if tid not in top_ids:
        top_ids[tid] = {'copies': t['copies'], 'sample_repos': set(), 'sample_paths': set(), 'repo_data_descriptions': set()}
    top_ids[tid]['sample_repos'].add(t['sample_repo_name'])
    top_ids[tid]['sample_paths'].add(t['sample_path'])
    top_ids[tid]['repo_data_descriptions'].add(t['repo_data_description'])

# convert sets to lists
output_list = []
for tid, info in top_ids.items():
    output_list.append({'id': tid, 'copies': info['copies'], 'sample_repos': sorted(list(info['sample_repos'])), 'sample_paths': sorted(list(info['sample_paths'])), 'repo_data_descriptions': sorted(list(info['repo_data_descriptions']))})

out = {'max_copies': max_copies, 'top_ids': output_list}
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_7K1bXJP2G0UyR0Y2Q4WXXpVl': [], 'var_call_ngpxT4i42o3RM8axgD7Xrid6': 'file_storage/call_ngpxT4i42o3RM8axgD7Xrid6.json', 'var_call_OaMFhbHUy84dNAZUPFnLnDty': 'file_storage/call_OaMFhbHUy84dNAZUPFnLnDty.json', 'var_call_dNKHUkFuxwwBGMJoP0XLlc5a': [], 'var_call_C3BvqPZeyKCzgP9zRp8QbPFh': [{'id': 'be6be234f9d404b0251c9a3626d644104cfe359b', 'copies': '1'}]}

exec(code, env_args)
