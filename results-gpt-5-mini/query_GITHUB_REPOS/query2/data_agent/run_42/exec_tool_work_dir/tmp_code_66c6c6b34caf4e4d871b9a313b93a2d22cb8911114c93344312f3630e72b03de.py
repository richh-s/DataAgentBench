code = """import json, re

# Load the query result from the artifacts query stored in storage variable
p = var_call_CgUdQ8ytJvrIQCOmv8Brmi2h
with open(p, 'r') as f:
    data = json.load(f)

results = []
for r in data:
    desc = r.get('repo_data_description') or ''
    # filter for non-binary
    if 'non-binary' not in desc.lower() and 'non binary' not in desc.lower():
        continue
    m = re.search(r"(\d+)\s+times", desc)
    if not m:
        # try 'duplicated (\d+) times' etc already captured, fallback to 1
        copies = 1
    else:
        copies = int(m.group(1))
    results.append({
        'id': r.get('id'),
        'sample_repo_name': r.get('sample_repo_name'),
        'sample_path': r.get('sample_path'),
        'copies': copies,
        'repo_data_description': desc
    })

# sort descending by copies
results_sorted = sorted(results, key=lambda x: x['copies'], reverse=True)
# take top 100
top100 = results_sorted[:100]

print("__RESULT__:")
print(json.dumps(top100))"""

env_args = {'var_call_CgUdQ8ytJvrIQCOmv8Brmi2h': 'file_storage/call_CgUdQ8ytJvrIQCOmv8Brmi2h.json'}

exec(code, env_args)
