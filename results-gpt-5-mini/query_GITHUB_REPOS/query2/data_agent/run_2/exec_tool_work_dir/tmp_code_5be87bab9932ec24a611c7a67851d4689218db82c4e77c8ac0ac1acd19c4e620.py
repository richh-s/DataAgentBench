code = """import json, re
# Load the contents query result from storage
data_var = var_call_UpL3MbiJCKJtLwGqt9WjyYHN
if isinstance(data_var, str):
    with open(data_var, 'r') as f:
        contents = json.load(f)
else:
    contents = data_var

# Filter Swift files and non-binary descriptions
swift_nonbinary = []
for rec in contents:
    path = rec.get('sample_path') or ''
    desc = rec.get('repo_data_description') or ''
    if path and path.lower().endswith('.swift') and 'non-binary' in desc.lower():
        # extract copy count
        m = re.search(r'(copied|duplicated|appears|appearing|appearing|appears|appearing|appearing|repeated|appearing)\s+(\d+)', desc, re.IGNORECASE)
        if m:
            count = int(m.group(2))
        else:
            # fallback: find any number followed by 'times' or 'occurrences' or standalone 'times'
            m2 = re.search(r'(\d+)\s+times', desc, re.IGNORECASE)
            if m2:
                count = int(m2.group(1))
            else:
                # try to find pattern like 'appearing N times' or 'seen N times'
                m3 = re.search(r'seen\s+(\d+)', desc, re.IGNORECASE)
                if m3:
                    count = int(m3.group(1))
                else:
                    # as last resort, try any number
                    m4 = re.search(r'(\d+)', desc)
                    count = int(m4.group(1)) if m4 else 1
        swift_nonbinary.append({'id': rec.get('id'), 'sample_repo_name': rec.get('sample_repo_name'), 'sample_path': path, 'copies': count, 'repo_data_description': desc})

# Find the max copies
if not swift_nonbinary:
    result = {'error': 'No Swift non-binary files found'}
else:
    max_copies = max(item['copies'] for item in swift_nonbinary)
    top_files = [item for item in swift_nonbinary if item['copies'] == max_copies]
    # we'll pick the first top file id (but return all top file ids to be safe)
    result = {'max_copies': max_copies, 'top_files': top_files}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_uIqHw6orIQTDDOyGowdNMRgh': 'file_storage/call_uIqHw6orIQTDDOyGowdNMRgh.json', 'var_call_UpL3MbiJCKJtLwGqt9WjyYHN': 'file_storage/call_UpL3MbiJCKJtLwGqt9WjyYHN.json', 'var_call_YIFV3dT5woYOTesJwbU1GoXI': [{'id': 'cc41f22d46f21f11c9e716b30cbaeb11f4ef80fc', 'copies': '1'}, {'id': '71a17ce92451858f3eb01aa8082551e48bc5550d', 'copies': '1'}]}

exec(code, env_args)
