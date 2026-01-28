code = """import json
with open(var_call_S2zuCHmhggl6c0g3JVnsCV3S, 'r') as f:
    businesses = json.load(f)

keys = set()
cats_examples = []
count_with_categories = 0
for i,b in enumerate(businesses[:50]):
    for k in b.keys():
        keys.add(k)
    if 'categories' in b:
        count_with_categories += 1
        cats_examples.append(b['categories'])

out = {
    'unique_keys_sample': sorted(list(keys)),
    'count_with_categories_in_first_50': count_with_categories,
    'cats_examples_first_10': cats_examples[:10]
}
print('__RESULT__:')
import json
print(json.dumps(out))"""

env_args = {'var_call_d7w2bomFdJCav34AlVZstfqh': ['business', 'checkin'], 'var_call_eZ7MDOj0Zdn0YwI5SRy8qChp': ['review', 'tip', 'user'], 'var_call_S2zuCHmhggl6c0g3JVnsCV3S': 'file_storage/call_S2zuCHmhggl6c0g3JVnsCV3S.json', 'var_call_yro9FRCCc3lUv55SCI5jPHkG': 'file_storage/call_yro9FRCCc3lUv55SCI5jPHkG.json', 'var_call_dE4HJh0hciMIKYUkYYNDB6yW': {'biz_len': 100, 'rev_len': 2000}, 'var_call_rnwohtD3Hil8vVqBV2wuTfIy': {'category': None, 'business_count': 0, 'average_rating': None}}

exec(code, env_args)
