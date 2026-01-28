code = """import json
with open(var_call_DYOmUKWQbTEskr11JQeVelj7, 'r', encoding='utf-8') as f:
    businesses = json.load(f)

# analyze keys and category values
key_counts = {}
sample = []
cat_values = set()
cat_nonnull = 0
for i, b in enumerate(businesses[:200]):
    for k in b.keys():
        key_counts[k] = key_counts.get(k, 0) + 1
    if 'categories' in b and b['categories'] is not None:
        cat_nonnull += 1
        v = b['categories']
        cat_values.add(str(v))
        if len(sample) < 10:
            sample.append({'business_id': b.get('business_id'), 'categories': b.get('categories')})

result = {
    'total_sampled': len(businesses[:200]),
    'key_counts_top': key_counts,
    'categories_nonnull_in_sample': cat_nonnull,
    'unique_category_value_examples_count': len(cat_values),
    'sample_items_with_categories': sample
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_AvP883aTMuAN0HLKUSywbHjl': ['business', 'checkin'], 'var_call_90pYhkxqqwG6X642xvBZDreX': ['review', 'tip', 'user'], 'var_call_DYOmUKWQbTEskr11JQeVelj7': 'file_storage/call_DYOmUKWQbTEskr11JQeVelj7.json', 'var_call_2m0iQ5foTc1FNVIoZVdOohmI': 'file_storage/call_2m0iQ5foTc1FNVIoZVdOohmI.json', 'var_call_zShDGF5WJoEBOSevaJFZQUi6': {'category': None, 'business_count': 0, 'average_rating': None}}

exec(code, env_args)
