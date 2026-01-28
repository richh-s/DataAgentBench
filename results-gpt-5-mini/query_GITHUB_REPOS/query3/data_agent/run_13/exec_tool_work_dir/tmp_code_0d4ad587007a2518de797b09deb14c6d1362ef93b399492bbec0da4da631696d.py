code = """import json
path = var_call_IWQO2IvaXj5KXkB2Jim0xLEQ
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)
# We'll collect counts per repo
from collections import Counter
cnt = Counter()
for rec in data:
    repo = rec.get('repo_name')
    if repo:
        cnt[repo] += 1
# prepare output top 20
top20 = cnt.most_common(20)
out = {'total_unique_repos': len(cnt), 'total_messages': sum(cnt.values()), 'top20': top20}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_vuapnoTrPXdfuv1rlKyGpWql': 'file_storage/call_vuapnoTrPXdfuv1rlKyGpWql.json', 'var_call_0Xlo3m9MtKTK2R2NE7tJbqMt': 'file_storage/call_0Xlo3m9MtKTK2R2NE7tJbqMt.json', 'var_call_dQvBVxmg1ThVUS1XpEyXkWLp': 'file_storage/call_dQvBVxmg1ThVUS1XpEyXkWLp.json', 'var_call_ovYJG4Ds4HDCXsXbrEgBSYcg': [], 'var_call_IWQO2IvaXj5KXkB2Jim0xLEQ': 'file_storage/call_IWQO2IvaXj5KXkB2Jim0xLEQ.json'}

exec(code, env_args)
