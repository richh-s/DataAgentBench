code = """import json
# read metadata repos list from earlier file
p = var_call_COm8Aw8kN260BreJqf2C2xDz
with open(p,'r') as f:
    meta = json.load(f)
meta_repos = set(r['repo_name'] for r in meta)
# read commits filtered list
p2 = var_call_XcMw5fmXVRhIG1dPnY6Luoc2
with open(p2,'r') as f:
    commits = json.load(f)
# filter commits to those repos in meta_repos
filtered = [c for c in commits if c.get('repo_name') in meta_repos]
count = len(filtered)
# also get distinct repos matched
matched_repos = sorted(set(c.get('repo_name') for c in filtered))
out = {'count': count, 'matched_repos_count': len(matched_repos), 'matched_repos_sample': matched_repos[:20]}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_COm8Aw8kN260BreJqf2C2xDz': 'file_storage/call_COm8Aw8kN260BreJqf2C2xDz.json', 'var_call_cmi9iKVzjejooAD4B3gfpXVU': "SELECT COUNT(*) AS count FROM commits WHERE repo_name IN () AND message IS NOT NULL AND message <> '' AND length(message) < 1000 AND lower(message) NOT LIKE 'merge%' AND lower(message) NOT LIKE 'update%' AND lower(message) NOT LIKE 'test%';", 'var_call_Hg5QnUaG1ogZUJOfkpKAvqZu': 'file_storage/call_Hg5QnUaG1ogZUJOfkpKAvqZu.json', 'var_call_mlcgYrrAALylwRu863N25x4l': [{'repo_name': 'facebook/react', 'cnt': '104'}, {'repo_name': 'tensorflow/tensorflow', 'cnt': '114'}, {'repo_name': 'twbs/bootstrap', 'cnt': '251'}, {'repo_name': 'apple/swift', 'cnt': '963'}, {'repo_name': 'torvalds/linux', 'cnt': '13413'}, {'repo_name': 'Microsoft/vscode', 'cnt': '171'}], 'var_call_zw98AkYxI4wUVMd3Ss7ugda9': 'file_storage/call_zw98AkYxI4wUVMd3Ss7ugda9.json', 'var_call_XcMw5fmXVRhIG1dPnY6Luoc2': 'file_storage/call_XcMw5fmXVRhIG1dPnY6Luoc2.json', 'var_call_CrMlm14kKsT3XqnaxoG73qdG': {'total_messages': 15016, 'unique_repos': 6, 'top10': [['torvalds/linux', 13413], ['apple/swift', 963], ['twbs/bootstrap', 251], ['Microsoft/vscode', 171], ['tensorflow/tensorflow', 114], ['facebook/react', 104]]}}

exec(code, env_args)
