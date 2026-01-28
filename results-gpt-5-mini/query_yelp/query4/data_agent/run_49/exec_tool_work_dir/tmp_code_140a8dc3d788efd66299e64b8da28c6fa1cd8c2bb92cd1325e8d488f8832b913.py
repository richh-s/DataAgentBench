code = """import json
from collections import Counter
with open(var_call_6nqTs8j0jeEpDA6Cqp0UwlOf, 'r', encoding='utf-8') as f:
    docs = json.load(f)
# Collect all top-level keys
key_counter = Counter()
attr_key_counter = Counter()
for d in docs:
    for k in d.keys():
        key_counter[k] += 1
    attrs = d.get('attributes')
    if isinstance(attrs, dict):
        for ak in attrs.keys():
            attr_key_counter[ak] += 1
# sample names
names = [d.get('name') for d in docs[:20]]
res = {'top_level_keys': key_counter.most_common(), 'attribute_keys': attr_key_counter.most_common(50), 'sample_names': names}
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_k7Hlv7AKTUJmYH5ofnVZthTS': ['checkin', 'business'], 'var_call_cn8vrQmfadYO7EE2IGbovTo1': ['review', 'tip', 'user'], 'var_call_6nqTs8j0jeEpDA6Cqp0UwlOf': 'file_storage/call_6nqTs8j0jeEpDA6Cqp0UwlOf.json', 'var_call_9mtxxbPNCG8ojm4K6oHPPUUw': 'file_storage/call_9mtxxbPNCG8ojm4K6oHPPUUw.json', 'var_call_tmmSUF2HgSpvWIQJ4E38A7xA': {'top_category': None, 'business_count': 0, 'average_rating': None}, 'var_call_ifyZujCDXpvxyAkwFmTQ1rms': {'info': {'columns': ['_id', 'business_id', 'name', 'attributes'], 'num_rows': 100}, 'categories_sample': [], 'possible_cols': {}, 'attributes_types': {'dict': 91, 'str': 9}}}

exec(code, env_args)
