code = """import json
with open(var_call_F4cpcLsVLk6o6bMKnniDw6Im, 'r') as f:
    businesses = json.load(f)

# Inspect keys and counts
total = len(businesses)
keys = set()
cat_present = 0
cat_samples = []
desc_present = 0
for b in businesses:
    keys.update(b.keys())
    if 'categories' in b and b['categories']:
        cat_present += 1
        cat_samples.append(b['categories'])
    if 'description' in b and b['description']:
        desc_present += 1

sample_keys = list(keys)
out = {
    'total_businesses': total,
    'sample_keys': sample_keys,
    'categories_non_null_count': cat_present,
    'categories_samples_first_10': cat_samples[:10],
    'description_non_null_count': desc_present
}
import json
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_JyUYVsueP42n2gO3CzQygFBv': ['business', 'checkin'], 'var_call_Q3QQtlxyfI0mIzMBvJQyUDgX': ['review', 'tip', 'user'], 'var_call_F4cpcLsVLk6o6bMKnniDw6Im': 'file_storage/call_F4cpcLsVLk6o6bMKnniDw6Im.json', 'var_call_qDys7vlegvauaC4FyvXgJxAV': 'file_storage/call_qDys7vlegvauaC4FyvXgJxAV.json', 'var_call_KTk26Lm0JhIt4M6RdDMgqOaU': {'category': None, 'business_count': 0, 'average_rating': None}}

exec(code, env_args)
