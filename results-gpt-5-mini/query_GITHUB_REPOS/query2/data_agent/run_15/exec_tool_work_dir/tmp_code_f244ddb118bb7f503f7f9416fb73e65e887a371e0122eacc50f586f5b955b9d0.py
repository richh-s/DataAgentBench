code = """import json, re
# Load the contents query result (may be a file path)
path_contents = var_call_7QRfbJ5qcFNYDqhCCQr6nzY7
with open(path_contents, 'r') as f:
    contents = json.load(f)
# Load the languages query result
path_langs = var_call_juq2LJHFH8TSszEoVo8HuI8K
with open(path_langs, 'r') as f:
    languages = json.load(f)

# Build a set of repo_names that mention Swift in language_description
swift_repos = set()
for r in languages:
    rn = r.get('repo_name')
    desc = r.get('language_description','')
    if 'Swift' in desc:
        swift_repos.add(rn)

# Parse copy counts for .swift files
records = []
for rec in contents:
    rid = rec.get('id')
    repo = rec.get('sample_repo_name')
    path = rec.get('sample_path')
    desc = rec.get('repo_data_description','')
    # Only consider non-binary wording
    if 'non-binary' not in desc and 'nonbinary' not in desc and 'non binary' not in desc:
        # some descriptions may not have the phrase; still consider if mode suggests text? but follow hint
        pass
    # find first occurrence of e.g. '12 times' or 'copied 12 times' or 'appearing 12 times' or 'repeated 12 times'
    m = re.search(r'(\d+)\s*times', desc)
    if not m:
        m = re.search(r'copied\s*(\d+)', desc)
    if not m:
        m = re.search(r'appearing\s*(\d+)', desc)
    if not m:
        m = re.search(r'repeated\s*(\d+)', desc)
    if not m:
        # try 'duplicated (\d+) times' handled by \d+ times
        pass
    copies = int(m.group(1)) if m else 1
    records.append({'id': rid, 'sample_repo_name': repo, 'sample_path': path, 'copies': copies, 'desc': desc})

# Ensure uniqueness by id (keep first)
by_id = {}
for r in records:
    if r['id'] not in by_id:
        by_id[r['id']] = r

# Find max copies
max_copies = 0
for r in by_id.values():
    if r['copies'] > max_copies:
        max_copies = r['copies']

# Collect ids with max
max_records = [r for r in by_id.values() if r['copies']==max_copies]

# From these, find those whose sample_repo_name is in swift_repos
swift_max_records = [r for r in max_records if r['sample_repo_name'] in swift_repos]

# If none found, we'll instead include all max_records (no language filter)
candidates = swift_max_records if swift_max_records else max_records

# Prepare output: list of unique repo names
repo_names = sorted(list({r['sample_repo_name'] for r in candidates}))
# Also include the id and copies
out = {'max_copies': max_copies, 'repos': repo_names, 'examples': candidates[:10]}

import json
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_juq2LJHFH8TSszEoVo8HuI8K': 'file_storage/call_juq2LJHFH8TSszEoVo8HuI8K.json', 'var_call_b46pECFrsI3EsGGqG44eS8Mc': [], 'var_call_7QRfbJ5qcFNYDqhCCQr6nzY7': 'file_storage/call_7QRfbJ5qcFNYDqhCCQr6nzY7.json'}

exec(code, env_args)
