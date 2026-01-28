code = """import json, re
file_path = var_call_0VOBnn5GTHMqq1oquNfRoYxg
with open(file_path, 'r', encoding='utf-8') as f:
    records = json.load(f)

# select swift files
swift = [r for r in records if r.get('sample_path') and r['sample_path'].lower().endswith('.swift')]

# filter non-binary: check for 'non-binary' or 'non binary' or 'nonbinary' in description
def is_non_binary(desc):
    if not desc:
        return False
    d = desc.lower()
    return 'non-binary' in d or 'non binary' in d or 'nonbinary' in d

swift_nb = [r for r in swift if is_non_binary(r.get('repo_data_description',''))]

# extract copy counts
def extract(desc):
    if not desc:
        return None
    d = desc.lower()
    m = re.search(r'(\d+)\s+times', d)
    if m:
        return int(m.group(1))
    m2 = re.search(r'(copied|duplicated|appearing|seen|repeated)\s+(\d+)', d)
    if m2:
        return int(m2.group(2))
    return None

from collections import defaultdict
by_id = defaultdict(list)
for r in swift_nb:
    by_id[r['id']].append(r)

# compute max copy count from repo_data_description if available, otherwise use count of rows
results = []
for id_, items in by_id.items():
    counts = [c for c in (extract(i.get('repo_data_description','')) for i in items) if c is not None]
    count_val = max(counts) if counts else None
    distinct_repos = sorted(list({i.get('sample_repo_name') for i in items if i.get('sample_repo_name')}))
    results.append({'id': id_, 'reported_copies': count_val, 'occurrences': len(items), 'distinct_repo_count': len(distinct_repos), 'distinct_repos': distinct_repos})

# find id with largest reported_copies; tie-breaker: occurrences, then distinct_repo_count
valid = [r for r in results if r['reported_copies'] is not None]
if not valid:
    out = {'error':'no reported copy counts found'}
else:
    valid_sorted = sorted(valid, key=lambda x: (x['reported_copies'], x['occurrences'], x['distinct_repo_count']), reverse=True)
    top = valid_sorted[0]
    out = top

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_zq1LXRXq5EVXyT4UuXqzpUBF': ['commits', 'contents', 'files'], 'var_call_ly0DXawkt3qY4h9EB126UEL7': [], 'var_call_9gYDXeVINOWiajbl0gNvwqEv': 'file_storage/call_9gYDXeVINOWiajbl0gNvwqEv.json', 'var_call_99rAooh2HoWqeFWvUAGqK2nY': [], 'var_call_jpy6veJbzBZV1g17WZ6awDVw': [], 'var_call_LkuEyUp3AP1ZT71yk1AM77iK': [{'id': '5fb353bfd251866214a3550d1f4bd33f2bc23333', 'repo_count': '1'}], 'var_call_0VOBnn5GTHMqq1oquNfRoYxg': 'file_storage/call_0VOBnn5GTHMqq1oquNfRoYxg.json', 'var_call_IzSWPviG1kjIk5XY79HKuqr9': 'file_storage/call_IzSWPviG1kjIk5XY79HKuqr9.json', 'var_call_mlgeQTpgBlYCGR5qfL33geAQ': {'error': 'no swift non-binary records found'}}

exec(code, env_args)
