code = """import json
# re-open the full swift query result file
file_path = var_call_0VOBnn5GTHMqq1oquNfRoYxg
with open(file_path, 'r', encoding='utf-8') as f:
    records = json.load(f)

# find record with id 6f4cdb70f044b0486a24a07403600cb964a02672
target_id = '6f4cdb70f044b0486a24a07403600cb964a02672'
matches = [r for r in records if r.get('id') == target_id]

print('__RESULT__:')
print(json.dumps(matches))"""

env_args = {'var_call_zq1LXRXq5EVXyT4UuXqzpUBF': ['commits', 'contents', 'files'], 'var_call_ly0DXawkt3qY4h9EB126UEL7': [], 'var_call_9gYDXeVINOWiajbl0gNvwqEv': 'file_storage/call_9gYDXeVINOWiajbl0gNvwqEv.json', 'var_call_99rAooh2HoWqeFWvUAGqK2nY': [], 'var_call_jpy6veJbzBZV1g17WZ6awDVw': [], 'var_call_LkuEyUp3AP1ZT71yk1AM77iK': [{'id': '5fb353bfd251866214a3550d1f4bd33f2bc23333', 'repo_count': '1'}], 'var_call_0VOBnn5GTHMqq1oquNfRoYxg': 'file_storage/call_0VOBnn5GTHMqq1oquNfRoYxg.json', 'var_call_IzSWPviG1kjIk5XY79HKuqr9': 'file_storage/call_IzSWPviG1kjIk5XY79HKuqr9.json', 'var_call_mlgeQTpgBlYCGR5qfL33geAQ': {'error': 'no swift non-binary records found'}, 'var_call_GStqJ9PFYw8CK5ODC3bz5f3y': {'id': '6f4cdb70f044b0486a24a07403600cb964a02672', 'reported_copies': 38, 'occurrences': 1, 'distinct_repo_count': 1, 'distinct_repos': ['uacaps/PageMenu']}}

exec(code, env_args)
