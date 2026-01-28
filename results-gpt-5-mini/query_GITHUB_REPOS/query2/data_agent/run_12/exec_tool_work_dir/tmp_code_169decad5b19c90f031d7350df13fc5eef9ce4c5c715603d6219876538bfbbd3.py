code = """import json, re
# var_call_2QScgCh80adt2EDhXi21HyD6 is the path to the JSON file with the query result
path = var_call_2QScgCh80adt2EDhXi21HyD6
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# function to extract copies number from repo_data_description
def extract_copies(desc):
    if not desc:
        return None
    desc = desc.lower()
    # look for patterns like 'copied 12 times', 'appearing 8 times', 'duplicated 10 times', 'seen 21 times'
    m = re.search(r"(copied|appearing|duplicated|seen|repeated)\s+(\d+)\s+times", desc)
    if m:
        return int(m.group(2))
    m = re.search(r"(\d+)\s+times", desc)
    if m:
        return int(m.group(1))
    # fallback: look for 'appearing X times' alternative word order
    m = re.search(r"(\d+)\s+appearing", desc)
    if m:
        return int(m.group(1))
    # try 'repeated X times' or 'repeated X'
    m = re.search(r"repeated\s+(\d+)", desc)
    if m:
        return int(m.group(1))
    # try 'seen X times'
    m = re.search(r"seen\s+(\d+)\s+times", desc)
    if m:
        return int(m.group(1))
    return None

# annotate data
for rec in data:
    rec['copies_extracted'] = extract_copies(rec.get('repo_data_description',''))

# find max copies
copies_vals = [r['copies_extracted'] for r in data if r['copies_extracted'] is not None]
if not copies_vals:
    result = {"max_copies": None, "ids": [], "repo_names": [], "sample_paths": []}
else:
    max_c = max(copies_vals)
    max_records = [r for r in data if r.get('copies_extracted')==max_c]
    ids = sorted(list({r['id'] for r in max_records}))
    repo_names = sorted(list({r['sample_repo_name'] for r in max_records}))
    sample_paths = sorted(list({r['sample_path'] for r in max_records}))
    result = {"max_copies": max_c, "ids": ids, "repo_names": repo_names, "sample_paths": sample_paths}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_rpRyLsnE61cE1hAUP5ZVGwx1': [], 'var_call_2QScgCh80adt2EDhXi21HyD6': 'file_storage/call_2QScgCh80adt2EDhXi21HyD6.json'}

exec(code, env_args)
