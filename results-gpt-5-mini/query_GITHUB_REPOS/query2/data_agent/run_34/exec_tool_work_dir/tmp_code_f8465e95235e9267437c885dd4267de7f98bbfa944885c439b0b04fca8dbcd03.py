code = """import json, re
# Load the large query result stored in var_call_Tj0ANcURuEyWx9KYIsA3ap9g (path to JSON file)
with open(var_call_Tj0ANcURuEyWx9KYIsA3ap9g, 'r') as f:
    data = json.load(f)

# Parse entries to extract non-binary swift files and their copy counts
rows = []
for r in data:
    desc = r.get('repo_data_description') or ''
    # consider only non-binary
    if 'non-binary' in desc or 'nonbinary' in desc or 'non binary' in desc:
        # search for patterns like 'duplicated 8 times', 'appearing 8 times', 'copied 12 times', 'seen 15 times', 'appearing 10 times'
        m = re.search(r"(duplicated|appearing|appears|appearing|copied|seen|repeated|appears|appeared)\s+(\d+)\s+times", desc)
        if not m:
            # try generic number before 'times'
            m = re.search(r"(\d+)\s+times", desc)
        if not m:
            # try 'appearing (\d+) times' alternative wordings handled above; try 'seen (\d+) times' handled
            pass
        count = int(m.group(2)) if m else None
        rows.append({'id': r.get('id'), 'sample_repo_name': r.get('sample_repo_name'), 'sample_path': r.get('sample_path'), 'copies': count, 'repo_data_description': desc})

# Filter to those with copies not None
rows = [r for r in rows if r['copies'] is not None]
# Find max copies
if not rows:
    result = {'error': 'no non-binary swift rows with copy counts found'}
else:
    max_copies = max(r['copies'] for r in rows)
    max_rows = [r for r in rows if r['copies']==max_copies]
    # Prepare result listing top ids and sample repos
    result = {'max_copies': max_copies, 'top_files': max_rows[:50]}  # limit

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_bgFR06hVPntYPptC56gRflBK': ['commits', 'contents', 'files'], 'var_call_Tj0ANcURuEyWx9KYIsA3ap9g': 'file_storage/call_Tj0ANcURuEyWx9KYIsA3ap9g.json'}

exec(code, env_args)
