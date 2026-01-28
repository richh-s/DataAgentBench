code = """import json, re

# Load the large query result stored in the file path variable
file_path = var_call_0VOBnn5GTHMqq1oquNfRoYxg
with open(file_path, 'r', encoding='utf-8') as f:
    records = json.load(f)

# Function to extract copy count from repo_data_description
def extract_count(desc):
    if not desc:
        return None
    desc_low = desc.lower()
    if 'binary' in desc_low:
        return None
    # look for patterns like 'copied 12 times', 'appearing 8 times', 'duplicated 10 times', 'seen 15 times', 'repeated 15 times'
    m = re.search(r'(copied|appearing|duplicated|seen|repeated|appears|appearing|appearing)\s+(\d+)\s+times', desc_low)
    if m:
        return int(m.group(2))
    # sometimes written like 'appearing 8 times' or 'appearing 8 times,' covered above; also patterns like 'appearing 8 times with'
    m2 = re.search(r'(\d+)\s+times', desc_low)
    if m2:
        return int(m2.group(1))
    # fallback: look for 'copied 12' or 'duplicated 10' without 'times'
    m3 = re.search(r'(copied|duplicated|appearing|seen|repeated)\s+(\d+)', desc_low)
    if m3:
        return int(m3.group(2))
    return None

# collect counts
rows = []
for r in records:
    if not r.get('sample_path'):
        continue
    if not r['sample_path'].lower().endswith('.swift'):
        continue
    desc = r.get('repo_data_description','')
    count = extract_count(desc)
    rows.append({'id': r.get('id'), 'sample_repo_name': r.get('sample_repo_name'), 'sample_path': r.get('sample_path'), 'repo_data_description': desc, 'count': count})

# find max count
max_count = None
for rr in rows:
    if rr['count'] is None:
        continue
    if max_count is None or rr['count'] > max_count:
        max_count = rr['count']

# find ids with max_count
top_rows = [rr for rr in rows if rr['count'] == max_count]

# prepare output
output = {
    'top_count': max_count,
    'top_rows': top_rows,
    'candidate_repo_names': sorted(list({rr['sample_repo_name'] for rr in top_rows}))
}

import json
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_zq1LXRXq5EVXyT4UuXqzpUBF': ['commits', 'contents', 'files'], 'var_call_ly0DXawkt3qY4h9EB126UEL7': [], 'var_call_9gYDXeVINOWiajbl0gNvwqEv': 'file_storage/call_9gYDXeVINOWiajbl0gNvwqEv.json', 'var_call_99rAooh2HoWqeFWvUAGqK2nY': [], 'var_call_jpy6veJbzBZV1g17WZ6awDVw': [], 'var_call_LkuEyUp3AP1ZT71yk1AM77iK': [{'id': '5fb353bfd251866214a3550d1f4bd33f2bc23333', 'repo_count': '1'}], 'var_call_0VOBnn5GTHMqq1oquNfRoYxg': 'file_storage/call_0VOBnn5GTHMqq1oquNfRoYxg.json'}

exec(code, env_args)
