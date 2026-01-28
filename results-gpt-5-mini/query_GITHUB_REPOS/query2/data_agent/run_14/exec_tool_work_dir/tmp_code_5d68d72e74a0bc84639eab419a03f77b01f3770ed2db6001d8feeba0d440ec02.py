code = """import json
with open(var_call_wiXK2dUnX8Nkr7ByfryAiyjH, 'r') as f:
    data = json.load(f)

total = len(data)
paths = [r.get('sample_path') for r in data[:20]]
count_swift = sum(1 for r in data if isinstance(r.get('sample_path'), str) and r.get('sample_path').lower().endswith('.swift'))
count_nonbinary = sum(1 for r in data if isinstance(r.get('repo_data_description'), str) and 'binary' not in r.get('repo_data_description').lower())
count_both = sum(1 for r in data if isinstance(r.get('sample_path'), str) and r.get('sample_path').lower().endswith('.swift') and isinstance(r.get('repo_data_description'), str) and 'binary' not in r.get('repo_data_description').lower())
res = {'total_records_in_result': total, 'first_20_paths': paths, 'count_swift': count_swift, 'count_nonbinary': count_nonbinary, 'count_both': count_both}
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_4Lli0VwvimK3yhNbFzPxIx3w': [], 'var_call_IkcQkgcHm1L1a1uYPlBViuPg': ['commits', 'contents', 'files'], 'var_call_wiXK2dUnX8Nkr7ByfryAiyjH': 'file_storage/call_wiXK2dUnX8Nkr7ByfryAiyjH.json', 'var_call_9VQhqtQnbmz0F3KCW9Ac9Yyj': {'max_copies': 0, 'ids': [], 'candidate_sample_repos': []}}

exec(code, env_args)
