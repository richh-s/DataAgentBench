code = """import json,re
# var_call_OaMFhbHUy84dNAZUPFnLnDty is available from storage
rows = var_call_OaMFhbHUy84dNAZUPFnLnDty

# rows is a list of dicts with keys: id, sample_repo_name, sample_path, repo_data_description
# Extract copies via regex
results = []
max_copies = -1
for r in rows:
    desc = r.get('repo_data_description') or ''
    m = re.search(r"(\d+)\s+times", desc)
    copies = None
    if m:
        copies = int(m.group(1))
    else:
        # try alternative phrases like 'copied 12' or 'duplicated 15'
        m2 = re.search(r"(\d+)\s+(?:copies|copied|duplicated|appearing|appears|appearing|seen|repeated)", desc)
        if m2:
            copies = int(m2.group(1))
    if copies is None:
        # fallback: set to 1
        copies = 1
    r2 = {'id': r.get('id'), 'sample_repo_name': r.get('sample_repo_name'), 'sample_path': r.get('sample_path'), 'copies': copies}
    results.append(r2)
    if copies > max_copies:
        max_copies = copies

# find ids with max copies
top = [r for r in results if r['copies'] == max_copies]
output = {'max_copies': max_copies, 'top_files': top}
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_7K1bXJP2G0UyR0Y2Q4WXXpVl': [], 'var_call_ngpxT4i42o3RM8axgD7Xrid6': 'file_storage/call_ngpxT4i42o3RM8axgD7Xrid6.json', 'var_call_OaMFhbHUy84dNAZUPFnLnDty': 'file_storage/call_OaMFhbHUy84dNAZUPFnLnDty.json', 'var_call_dNKHUkFuxwwBGMJoP0XLlc5a': [], 'var_call_C3BvqPZeyKCzgP9zRp8QbPFh': [{'id': 'be6be234f9d404b0251c9a3626d644104cfe359b', 'copies': '1'}]}

exec(code, env_args)
