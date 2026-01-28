code = """import json
# Read the stored contents query result
file_path = var_call_0VOBnn5GTHMqq1oquNfRoYxg
with open(file_path, 'r', encoding='utf-8') as f:
    records = json.load(f)

# Filter swift files and non-binary
rows = [r for r in records if r.get('sample_path') and r['sample_path'].lower().endswith('.swift')]
rows = [r for r in rows if r.get('repo_data_description') and 'binary' not in r['repo_data_description'].lower()]

# Group by id
from collections import defaultdict
group = defaultdict(list)
for r in rows:
    group[r['id']].append(r)

# Compute stats per id
stats = []
for id_, items in group.items():
    repos = set(i.get('sample_repo_name') for i in items if i.get('sample_repo_name'))
    stats.append({'id': id_, 'count_total': len(items), 'count_distinct_repos': len(repos), 'sample_repo_names': sorted(list(repos)), 'sample_paths': sorted(list({i.get('sample_path') for i in items if i.get('sample_path')}))})

# Find id with max distinct repos, then max total
if not stats:
    result = {'error': 'no swift non-binary records found'}
else:
    stats_sorted = sorted(stats, key=lambda x: (x['count_distinct_repos'], x['count_total']), reverse=True)
    top = stats_sorted[0]
    result = {'top_id': top['id'], 'count_distinct_repos': top['count_distinct_repos'], 'count_total': top['count_total'], 'sample_repo_names': top['sample_repo_names'], 'sample_paths': top['sample_paths']}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_zq1LXRXq5EVXyT4UuXqzpUBF': ['commits', 'contents', 'files'], 'var_call_ly0DXawkt3qY4h9EB126UEL7': [], 'var_call_9gYDXeVINOWiajbl0gNvwqEv': 'file_storage/call_9gYDXeVINOWiajbl0gNvwqEv.json', 'var_call_99rAooh2HoWqeFWvUAGqK2nY': [], 'var_call_jpy6veJbzBZV1g17WZ6awDVw': [], 'var_call_LkuEyUp3AP1ZT71yk1AM77iK': [{'id': '5fb353bfd251866214a3550d1f4bd33f2bc23333', 'repo_count': '1'}], 'var_call_0VOBnn5GTHMqq1oquNfRoYxg': 'file_storage/call_0VOBnn5GTHMqq1oquNfRoYxg.json', 'var_call_IzSWPviG1kjIk5XY79HKuqr9': 'file_storage/call_IzSWPviG1kjIk5XY79HKuqr9.json'}

exec(code, env_args)
