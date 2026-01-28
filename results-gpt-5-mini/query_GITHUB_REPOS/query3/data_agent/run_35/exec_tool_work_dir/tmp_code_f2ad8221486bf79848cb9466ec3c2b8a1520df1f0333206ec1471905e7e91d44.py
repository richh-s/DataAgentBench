code = """import json
p = var_call_XcMw5fmXVRhIG1dPnY6Luoc2
# load
with open(p, 'r') as f:
    records = json.load(f)
# count occurrences per repo
from collections import Counter
cnt = Counter(r['repo_name'] for r in records if 'repo_name' in r)
# total
total = sum(cnt.values())
# unique repos
unique = len(cnt)
# prepare top 10
top10 = cnt.most_common(10)
out = {'total_messages': total, 'unique_repos': unique, 'top10': top10}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_COm8Aw8kN260BreJqf2C2xDz': 'file_storage/call_COm8Aw8kN260BreJqf2C2xDz.json', 'var_call_cmi9iKVzjejooAD4B3gfpXVU': "SELECT COUNT(*) AS count FROM commits WHERE repo_name IN () AND message IS NOT NULL AND message <> '' AND length(message) < 1000 AND lower(message) NOT LIKE 'merge%' AND lower(message) NOT LIKE 'update%' AND lower(message) NOT LIKE 'test%';", 'var_call_Hg5QnUaG1ogZUJOfkpKAvqZu': 'file_storage/call_Hg5QnUaG1ogZUJOfkpKAvqZu.json', 'var_call_mlcgYrrAALylwRu863N25x4l': [{'repo_name': 'facebook/react', 'cnt': '104'}, {'repo_name': 'tensorflow/tensorflow', 'cnt': '114'}, {'repo_name': 'twbs/bootstrap', 'cnt': '251'}, {'repo_name': 'apple/swift', 'cnt': '963'}, {'repo_name': 'torvalds/linux', 'cnt': '13413'}, {'repo_name': 'Microsoft/vscode', 'cnt': '171'}], 'var_call_zw98AkYxI4wUVMd3Ss7ugda9': 'file_storage/call_zw98AkYxI4wUVMd3Ss7ugda9.json', 'var_call_XcMw5fmXVRhIG1dPnY6Luoc2': 'file_storage/call_XcMw5fmXVRhIG1dPnY6Luoc2.json'}

exec(code, env_args)
